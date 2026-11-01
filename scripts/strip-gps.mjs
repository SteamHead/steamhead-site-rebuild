#!/usr/bin/env node
// Remove GPS location from every image under the given folders, in place.
//
// Why: phone photos record where they were taken, and this site and its repo
// are public (issue #52, decided by James 2026-10-31). Originals are kept as
// backups elsewhere, so nothing is lost.
//
// What it does: in JPEG, PNG and WebP files it empties the EXIF GPS block and
// blanks GPS fields in XMP, without changing the file's length or anything
// else. The capture date, orientation and the image itself are untouched.
// It runs before every build (`prebuild` in package.json), so images added
// through the CMS are cleaned before they are published.
//
// Usage:
//   node scripts/strip-gps.mjs [--check] FOLDER...
//   --check   change nothing; exit 1 if any image still has GPS
//
// It also exits 1 for a format it cannot clean (HEIC, AVIF, TIFF): convert
// those to JPEG or WebP first. No dependencies, so it runs on Cloudflare's
// build image as well as on Splinter.

import { readFileSync, writeFileSync, readdirSync, statSync } from "node:fs";
import { join, extname } from "node:path";
import { crc32 } from "node:zlib";

const CLEANABLE = new Set([".jpg", ".jpeg", ".png", ".webp"]);
const UNCLEANABLE = new Set([".heic", ".heif", ".avif", ".tif", ".tiff"]);
const GPS_IFD_TAG = 0x8825;
const TYPE_SIZE = { 1: 1, 2: 1, 3: 2, 4: 4, 5: 8, 6: 1, 7: 1, 8: 2, 9: 4, 10: 8, 11: 4, 12: 8 };

class Unreadable extends Error {}

// --- EXIF (a TIFF structure) ------------------------------------------------

/** Empty the GPS IFD inside the TIFF block buf[start..end). Returns true if it held any GPS. */
function stripTiffGps(buf, start, end, write) {
  const len = end - start;
  if (len < 8) throw new Unreadable("EXIF block too short");
  const order = buf.toString("latin1", start, start + 2);
  const le = order === "II";
  if (!le && order !== "MM") throw new Unreadable("EXIF block has no byte order");
  const u16 = (o) => {
    if (o < 0 || o + 2 > len) throw new Unreadable("EXIF offset out of range");
    return le ? buf.readUInt16LE(start + o) : buf.readUInt16BE(start + o);
  };
  const u32 = (o) => {
    if (o < 0 || o + 4 > len) throw new Unreadable("EXIF offset out of range");
    return le ? buf.readUInt32LE(start + o) : buf.readUInt32BE(start + o);
  };

  const ifd0 = u32(4);
  const n0 = u16(ifd0);
  let gps = null;
  for (let i = 0; i < n0; i++) {
    const e = ifd0 + 2 + 12 * i;
    if (u16(e) === GPS_IFD_TAG) gps = u32(e + 8);
  }
  if (gps === null) return false;

  const n = u16(gps);
  if (n === 0) return false;
  // Check every bound before changing a byte, so a damaged file is left whole.
  // The count, every entry and the next-IFD pointer.
  const zero = [[gps, gps + 2 + 12 * n + 4]];
  for (let i = 0; i < n; i++) {
    const e = gps + 2 + 12 * i;
    const size = (TYPE_SIZE[u16(e + 2)] ?? 1) * u32(e + 4);
    if (size > 4) {
      const off = u32(e + 8);
      if (off + size > len) throw new Unreadable("GPS value out of range");
      zero.push([off, off + size]);
    }
  }
  if (zero[0][1] > len) throw new Unreadable("GPS block out of range");
  if (write) {
    for (const [a, b] of zero) buf.fill(0, start + a, start + b);
    // The count is now 0 and the entries and next-IFD pointer are zeroed:
    // an empty, valid IFD that IFD0 still points to.
  }
  return true;
}

// --- XMP (text) -------------------------------------------------------------

// GPS fields in XMP, as attributes (exif:GPSLatitude="...") or elements.
const XMP_GPS = [
  /\s[\w.-]+:GPS[A-Za-z]*\s*=\s*"[^"]*"/g,
  /\s[\w.-]+:GPS[A-Za-z]*\s*=\s*'[^']*'/g,
  /<([\w.-]+:GPS[A-Za-z]*)\b[^>]*?(?:\/>|>[\s\S]*?<\/\1\s*>)/g,
];

/** Blank GPS fields in the XMP text buf[start..end) with spaces of equal length. */
function stripXmpGps(buf, start, end, write) {
  const text = buf.toString("latin1", start, end); // 1 byte per char, so offsets match
  let found = false;
  for (const re of XMP_GPS) {
    for (const m of text.matchAll(re)) {
      found = true;
      if (write) buf.fill(0x20, start + m.index, start + m.index + m[0].length);
    }
  }
  return found;
}

// --- containers -------------------------------------------------------------

const EXIF_HEADER = Buffer.from("Exif\0\0", "latin1");
const XMP_HEADER = Buffer.from("http://ns.adobe.com/xap/1.0/\0", "latin1");

function jpeg(buf, write) {
  if (buf[0] !== 0xff || buf[1] !== 0xd8) throw new Unreadable("not a JPEG");
  let found = false;
  let p = 2;
  while (p + 4 <= buf.length) {
    if (buf[p] !== 0xff) throw new Unreadable("JPEG segment marker missing");
    const marker = buf[p + 1];
    if (marker === 0xd9 || marker === 0xda) break; // end of image / start of scan
    if (marker === 0xff) { p += 1; continue; } // fill byte
    if ((marker >= 0xd0 && marker <= 0xd7) || marker === 0x01) { p += 2; continue; }
    const segLen = buf.readUInt16BE(p + 2);
    const body = p + 4;
    const end = p + 2 + segLen;
    if (segLen < 2 || end > buf.length) throw new Unreadable("JPEG segment out of range");
    if (marker === 0xe1) {
      if (buf.subarray(body, body + 6).equals(EXIF_HEADER)) {
        found = stripTiffGps(buf, body + 6, end, write) || found;
      } else if (buf.subarray(body, body + XMP_HEADER.length).equals(XMP_HEADER)) {
        found = stripXmpGps(buf, body + XMP_HEADER.length, end, write) || found;
      }
    }
    p = end;
  }
  return found;
}

function png(buf, write) {
  if (buf.toString("latin1", 1, 4) !== "PNG") throw new Unreadable("not a PNG");
  let found = false;
  let p = 8;
  while (p + 12 <= buf.length) {
    const len = buf.readUInt32BE(p);
    const type = buf.toString("latin1", p + 4, p + 8);
    const data = p + 8;
    const end = data + len;
    if (end + 4 > buf.length) throw new Unreadable("PNG chunk out of range");
    let hit = false;
    if (type === "eXIf") {
      hit = stripTiffGps(buf, data, end, write);
    } else if (type === "iTXt" && buf.toString("latin1", data, data + 18) === "XML:com.adobe.xmp\0") {
      hit = stripXmpGps(buf, data, end, write);
    }
    if (hit && write) buf.writeUInt32BE(crc32(buf.subarray(p + 4, end)), end);
    found = hit || found;
    if (type === "IEND") break;
    p = end + 4;
  }
  return found;
}

function webp(buf, write) {
  if (buf.toString("latin1", 0, 4) !== "RIFF" || buf.toString("latin1", 8, 12) !== "WEBP") {
    throw new Unreadable("not a WebP");
  }
  let found = false;
  let p = 12;
  while (p + 8 <= buf.length) {
    const type = buf.toString("latin1", p, p + 4);
    const len = buf.readUInt32LE(p + 4);
    const data = p + 8;
    const end = data + len;
    if (end > buf.length) throw new Unreadable("WebP chunk out of range");
    if (type === "EXIF") {
      const skip = buf.subarray(data, data + 6).equals(EXIF_HEADER) ? 6 : 0;
      found = stripTiffGps(buf, data + skip, end, write) || found;
    } else if (type === "XMP ") {
      found = stripXmpGps(buf, data, end, write) || found;
    }
    p = end + (len % 2);
  }
  return found;
}

const HANDLERS = { ".jpg": jpeg, ".jpeg": jpeg, ".png": png, ".webp": webp };

// --- main -------------------------------------------------------------------

function* walk(dir) {
  for (const name of readdirSync(dir).sort()) {
    const path = join(dir, name);
    if (statSync(path).isDirectory()) yield* walk(path);
    else yield path;
  }
}

const args = process.argv.slice(2);
const check = args.includes("--check");
const roots = args.filter((a) => a !== "--check");
if (roots.length === 0) {
  console.error("usage: node scripts/strip-gps.mjs [--check] FOLDER...");
  process.exit(2);
}

let scanned = 0, stripped = 0;
const problems = [];
for (const root of roots) {
  for (const path of walk(root)) {
    const ext = extname(path).toLowerCase();
    if (UNCLEANABLE.has(ext)) {
      problems.push(`${path}: cannot remove GPS from ${ext} files; convert it to JPEG or WebP`);
      continue;
    }
    if (!CLEANABLE.has(ext)) continue;
    scanned++;
    const buf = readFileSync(path);
    try {
      const handler = HANDLERS[ext];
      if (!handler(buf, false)) continue;
      if (check) {
        problems.push(`${path}: has GPS location`);
        continue;
      }
      handler(buf, true);
      if (handler(buf, false)) throw new Unreadable("GPS still present after stripping");
      writeFileSync(path, buf);
      stripped++;
      console.log(`strip-gps: removed GPS from ${path}`);
    } catch (err) {
      if (!(err instanceof Unreadable)) throw err;
      problems.push(`${path}: ${err.message}; not changed`);
    }
  }
}

console.log(`strip-gps: ${scanned} images checked, ${stripped} cleaned${check ? " (check only)" : ""}.`);
if (problems.length) {
  for (const p of problems) console.error(`strip-gps: ${p}`);
  console.error(`strip-gps: ${problems.length} problem(s); failing so nothing with a location is published.`);
  process.exit(1);
}
