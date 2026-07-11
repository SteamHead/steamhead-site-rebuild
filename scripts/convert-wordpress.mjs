// WordPress XML → content collections converter.
// Implements the locked decisions in MIGRATION.md. Rerunnable: wipes and
// regenerates src/content/blog/, src/content/people/, public/_redirects.
//
//   node scripts/convert-wordpress.mjs <path-to-export.xml> [--download-images]
//
// Outputs a conversion report to scripts/migration-report.md and the
// people slug map to scripts/people-slug-map.json.

import { readFileSync, writeFileSync, mkdirSync, rmSync, existsSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import TurndownService from 'turndown';
import { gfm } from 'turndown-plugin-gfm';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const XML_PATH = process.argv[2];
const DOWNLOAD = process.argv.includes('--download-images');
if (!XML_PATH) { console.error('usage: node scripts/convert-wordpress.mjs <export.xml> [--download-images]'); process.exit(1); }

const AUTHOR_MAP = {
  admin: 'James Simpson',
  catherineyang920: 'Catherine Yang',
  // 'Angry Duck' stays 'Angry Duck' by request.
};
const PROFILE_CATS = new Set(['SteamHead Team', 'SteamHead Residents']);
const OLD_HOSTS = /https?:\/\/(www\.)?steamhead\.space/g;

// ---------------------------------------------------------------------------
// XML parsing (regex-free structural parse via a tiny stack-less scan is
// fragile; the export is well-formed, so lean on the platform: split items).
// Node has no DOM built in, so parse the few fields we need with targeted
// extraction from each <item> block. CDATA-aware.
// ---------------------------------------------------------------------------
const xml = readFileSync(XML_PATH, 'utf8').replace(/\r\n?/g, '\n');
const items = xml.split('<item>').slice(1).map(s => s.split('</item>')[0]);

const unesc = s => s.replaceAll('&amp;', '&').replaceAll('&lt;', '<').replaceAll('&gt;', '>').replaceAll('&quot;', '"').replaceAll('&#039;', "'");
function field(block, tag) {
  const m = block.match(new RegExp(`<${tag}[^>]*>(?:<!\\[CDATA\\[([\\s\\S]*?)\\]\\]>|([\\s\\S]*?))</${tag}>`));
  if (!m) return '';
  return m[1] !== undefined ? m[1] : unesc(m[2] ?? '');
}
function categories(block, domain) {
  const out = [];
  const re = /<category domain="([^"]+)"[^>]*><!\[CDATA\[([\s\S]*?)\]\]><\/category>/g;
  let m; while ((m = re.exec(block))) if (m[1] === domain) out.push(m[2]);
  return out;
}
function postmeta(block, key) {
  const re = /<wp:postmeta>[\s\S]*?<wp:meta_key><!\[CDATA\[([\s\S]*?)\]\]><\/wp:meta_key>\s*<wp:meta_value><!\[CDATA\[([\s\S]*?)\]\]><\/wp:meta_value>[\s\S]*?<\/wp:postmeta>/g;
  let m; while ((m = re.exec(block))) if (m[1] === key) return m[2];
  return '';
}

// Attachment id → URL map, for featured images and [gallery] ids.
const attachments = {};
for (const it of items) {
  if (field(it, 'wp:post_type') !== 'attachment') continue;
  attachments[field(it, 'wp:post_id')] = field(it, 'wp:attachment_url');
}

// ---------------------------------------------------------------------------
// HTML/shortcode → markdown
// ---------------------------------------------------------------------------
const td = new TurndownService({ headingStyle: 'atx', codeBlockStyle: 'fenced', bulletListMarker: '-' });
td.use(gfm);
td.keep(['iframe']); // rare embeds; visible in spot-check rather than silently dropped

function attrsOf(shortcode) {
  const out = {};
  const re = /(\w+)="([^"]*)"/g;
  let m; while ((m = re.exec(shortcode))) out[m[1]] = m[2];
  return out;
}

function preprocess(html) {
  let s = html;
  // Gutenberg comments (a handful of posts have stray ones)
  s = s.replace(/<!-- \/?wp:[\s\S]*?-->/g, '');
  // Divi
  s = s.replaceAll('[et_pb_line_break_holder]', '\n');
  // et_pb_image → img
  s = s.replace(/\[et_pb_image([^\]]*)\][\s\S]*?\[\/et_pb_image\]|\[et_pb_image([^\]]*)\/?\]/g, (_, a1, a2) => {
    const a = attrsOf(a1 ?? a2 ?? '');
    return a.src ? `<img src="${a.src}" alt="${a.alt ?? ''}">` : '';
  });
  // et_pb_video → bare URL on its own line (embed handling is a design-phase decision)
  s = s.replace(/\[et_pb_video([^\]]*)\][\s\S]*?\[\/et_pb_video\]|\[et_pb_video([^\]]*)\/?\]/g, (_, a1, a2) => {
    const a = attrsOf(a1 ?? a2 ?? '');
    return a.src ? `\n\n${a.src}\n\n` : '';
  });
  // et_pb_gallery → imgs from attachment ids
  s = s.replace(/\[et_pb_gallery([^\]]*)\/?\](?:\[\/et_pb_gallery\])?/g, (_, attrs) => {
    const ids = (attrsOf(attrs).gallery_ids ?? '').split(',').filter(Boolean);
    return ids.map(id => attachments[id] ? `<img src="${attachments[id]}" alt="">` : '').join('\n');
  });
  // [gallery ids=...] (classic)
  s = s.replace(/\[gallery([^\]]*)\]/g, (_, attrs) => {
    const ids = (attrsOf(attrs).ids ?? '').split(',').filter(Boolean);
    return ids.map(id => attachments[id] ? `<img src="${attachments[id]}" alt="">` : '').join('\n');
  });
  // [caption]...<img>...caption text[/caption] → img + em text
  s = s.replace(/\[caption[^\]]*\]([\s\S]*?)\[\/caption\]/g, (_, inner) => {
    const img = inner.match(/<img[^>]*>/)?.[0] ?? '';
    const text = inner.replace(/<img[^>]*>/, '').replace(/<[^>]+>/g, '').trim();
    return `${img}\n\n${text ? `*${text}*\n\n` : ''}`;
  });
  // [embed]url[/embed] → bare URL
  s = s.replace(/\[embed[^\]]*\]([\s\S]*?)\[\/embed\]/g, '\n\n$1\n\n');
  // [video mp4="..."] → bare URL (videos are never hosted in the repo —
  // these must move to YouTube/Drive; the report lists them)
  s = s.replace(/\[video([^\]]*)\](?:\[\/video\])?/g, (_, attrs) => {
    const a = attrsOf(attrs);
    const src = a.mp4 ?? a.src ?? a.m4v ?? a.mov ?? '';
    return src ? `\n\n${src}\n\n` : '';
  });
  // [button ...]text[/button] → keep the inner text, drop the wrapper
  s = s.replace(/\[button[^\]]*\]([\s\S]*?)\[\/button\]/g, '$1');
  // Remaining Divi structural shortcodes: unwrap (keep inner content)
  s = s.replace(/\[\/?et_pb_[a-z_]+[^\]]*\]/g, '\n');
  // Draft.js / editor junk divs get unwrapped by turndown automatically.
  return wpautop(s);
}

// WordPress stores classic-editor paragraphs as bare double newlines and
// renders them via wpautop(); without this, an HTML parser collapses them
// to spaces and whole posts become one paragraph. Lite emulation: chunks
// split on blank lines become <p>, single newlines become <br>.
function wpautop(s) {
  return s.split(/\n{2,}/).map(chunk => {
    const c = chunk.trim();
    if (!c) return '';
    // leave chunks that already start with a block element alone
    if (/^<\/?(p|div|h[1-6]|ul|ol|li|blockquote|figure|table|pre|iframe|img|hr)\b/i.test(c)) return c;
    return `<p>${c.replace(/\n/g, '<br>')}</p>`;
  }).join('\n');
}

function toMarkdown(html) {
  let md = td.turndown(preprocess(html));
  md = md.replace(/\n{3,}/g, '\n\n').trim();
  // The page renders the post title as the <h1>; body h1s would compete
  // with it (and render huge), so demote them one level.
  md = md.replace(/^# /gm, '## ');
  return md;
}

// ---------------------------------------------------------------------------
// Collect posts
// ---------------------------------------------------------------------------
const slugify = t => t.toLowerCase().replace(/['’]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '') || 'untitled';
const posts = [];
for (const it of items) {
  if (field(it, 'wp:post_type') !== 'post') continue;
  const status = field(it, 'wp:status');
  if (!['publish', 'draft', 'pending', 'private'].includes(status)) continue;
  posts.push({
    title: field(it, 'title').trim() || '(untitled)',
    slug: field(it, 'wp:post_name'),
    status,
    date: field(it, 'wp:post_date'),
    modified: field(it, 'wp:post_modified'),
    creator: field(it, 'dc:creator'),
    cats: categories(it, 'category'),
    tags: categories(it, 'post_tag'),
    excerpt: field(it, 'excerpt:encoded').trim(),
    body: field(it, 'content:encoded'),
    thumbId: postmeta(it, '_thumbnail_id'),
  });
}

// Slug assignment: published posts first so they always keep their real slug.
posts.sort((a, b) => (a.status === 'publish' ? 0 : 1) - (b.status === 'publish' ? 0 : 1));
const used = new Set();
for (const p of posts) {
  let s = p.slug || slugify(p.title);
  let base = s, n = 2;
  while (used.has(s)) s = `${base}-${n++}`;
  used.add(s);
  p.finalSlug = s;
}

// ---------------------------------------------------------------------------
// Image URL handling
// ---------------------------------------------------------------------------
const imageRefs = new Map(); // remote URL → local path
const videoRefs = new Set(); // videos stay remote — re-host on YouTube/Drive
function localizeImageUrl(url) {
  const m = url.match(/\/wp-content\/uploads\/(\d{4})\/(\d{2})\/([^"'\s)?]+)/);
  if (!m) return url; // external image — leave alone
  if (/\.(mp4|mov|m4v|avi|webm)$/i.test(m[3])) {
    const abs = url.startsWith('http') ? url : `https://steamhead.space${url}`;
    videoRefs.add(abs);
    return abs;
  }
  const local = `/images/${m[1]}/${m[2]}/${decodeURIComponent(m[3])}`;
  imageRefs.set(url.startsWith('http') ? url : `https://steamhead.space${url}`, local);
  return local;
}

function rewriteUrls(md, blogSlugs, peopleSlugs) {
  // images first (uploads paths), then internal post links, then any
  // remaining old-domain links become root-relative.
  md = md.replace(/https?:\/\/(?:www\.)?steamhead\.space\/wp-content\/uploads\/[^\s"')]+|\/wp-content\/uploads\/[^\s"')]+/g, localizeImageUrl);
  md = md.replace(/https?:\/\/(?:www\.)?steamhead\.space\/([a-z0-9-]+)\/?(?=[\s"')]|$)/g, (full, slug) => {
    if (blogSlugs.has(slug)) return `/blog/${slug}/`;
    if (peopleSlugs.has(slug)) return `/people/${slug}/`;
    return full.replace(OLD_HOSTS, '');
  });
  return md;
}

// ---------------------------------------------------------------------------
// Emit
// ---------------------------------------------------------------------------
const yq = s => `"${String(s).replace(/\\/g, '\\\\').replace(/"/g, '\\"')}"`;
const blogDir = join(ROOT, 'src/content/blog');
const peopleDir = join(ROOT, 'src/content/people');
rmSync(blogDir, { recursive: true, force: true });
rmSync(peopleDir, { recursive: true, force: true });
mkdirSync(blogDir, { recursive: true });
mkdirSync(peopleDir, { recursive: true });

const isProfile = p => p.cats.some(c => PROFILE_CATS.has(c));
const blogSlugs = new Set(posts.filter(p => !isProfile(p)).map(p => p.finalSlug));
const peopleSlugs = new Set(posts.filter(isProfile).map(p => p.finalSlug));

const report = { blog: 0, people: 0, drafts: 0, guessedDesc: [], emptyBody: [], keptIframes: [], externalImgs: new Set() };
const peopleMap = {};
const redirects = [];

for (const p of posts) {
  const draft = p.status !== 'publish';
  const author = AUTHOR_MAP[p.creator] ?? p.creator ?? 'SteamHead';
  const date = /^\d{4}-\d{2}-\d{2}/.test(p.date) && !p.date.startsWith('0000')
    ? p.date.slice(0, 10) : (p.modified?.slice(0, 10) || '2026-07-10');
  const program =
    p.cats.includes('MakeFashion Edu') ? 'makefashion-edu' :
    p.cats.includes('Neighborhood Earth') ? 'neighborhood-earth' : 'general';

  let md = p.body.trim() ? toMarkdown(p.body) : '';
  md = rewriteUrls(md, blogSlugs, peopleSlugs);
  if (!md) report.emptyBody.push(p.finalSlug);
  if (md.includes('<iframe')) report.keptIframes.push(p.finalSlug);
  for (const m of md.matchAll(/!\[[^\]]*\]\((https?:\/\/[^)]+)\)/g)) report.externalImgs.add(m[1]);

  let description = p.excerpt.replace(/<[^>]+>/g, '').trim();
  if (!description) {
    const text = md.replace(/!\[[^\]]*\]\([^)]*\)/g, '').replace(/https?:\/\/\S+/g, '').replace(/<[^>]+>/g, '').replace(/[#*_>\[\]]/g, '').replace(/\s+/g, ' ').trim();
    // End on a sentence boundary: accumulate whole sentences up to ~180
    // chars; a first sentence longer than that gets cut at a word + ellipsis.
    const sentences = text.split(/(?<=[.!?])\s+/);
    let out = '';
    for (const sent of sentences) {
      if (out && (out + ' ' + sent).length > 180) break;
      out = out ? `${out} ${sent}` : sent;
      if (out.length > 180) break;
    }
    if (out.length > 200) out = out.slice(0, 180).replace(/\s+\S*$/, '') + '…';
    description = out || p.title;
    if (text) report.guessedDesc.push(p.finalSlug);
  }

  const thumb = p.thumbId && attachments[p.thumbId] ? localizeImageUrl(attachments[p.thumbId]) : '';
  const firstImg = md.match(/!\[[^\]]*\]\((\/images\/[^)]+)\)/)?.[1] ?? '';
  const image = thumb || firstImg;

  if (isProfile(p)) {
    const role = p.cats.includes('SteamHead Team') ? 'team' : 'resident';
    const fm = [
      `name: ${yq(p.title)}`,
      `role: ${role}`,
      `date: ${date}`,
      description ? `description: ${yq(description)}` : null,
      image ? `image: ${yq(image)}` : null,
      image ? `imageAlt: ${yq(p.title)}` : null,
      draft ? 'draft: true' : null,
    ].filter(Boolean).join('\n');
    writeFileSync(join(peopleDir, `${p.finalSlug}.md`), `---\n${fm}\n---\n\n${md}\n`);
    peopleMap[p.finalSlug] = { name: p.title, role, oldUrl: `/${p.slug}/` };
    report.people++;
  } else {
    const fm = [
      `title: ${yq(p.title)}`,
      `date: ${date}`,
      `description: ${yq(description)}`,
      `author: ${yq(author)}`,
      `program: ${program}`,
      p.cats.length ? `categories:\n${p.cats.map(c => `  - ${yq(c)}`).join('\n')}` : 'categories: []',
      p.tags.length ? `tags:\n${p.tags.map(t => `  - ${yq(t)}`).join('\n')}` : null,
      image ? `image: ${yq(image)}` : null,
      image ? `imageAlt: ${yq(p.title)}` : null,
      draft ? 'draft: true' : null,
    ].filter(Boolean).join('\n');
    writeFileSync(join(blogDir, `${p.finalSlug}.md`), `---\n${fm}\n---\n\n${md}\n`);
    report.blog++;
    if (!draft && p.slug) redirects.push(`/${p.slug}/ /blog/${p.finalSlug}/ 301`);
  }
  if (draft) report.drafts++;
}

writeFileSync(join(ROOT, 'public/_redirects'), redirects.sort().join('\n') + '\n');
writeFileSync(join(ROOT, 'scripts/people-slug-map.json'), JSON.stringify(peopleMap, null, 2) + '\n');

// ---------------------------------------------------------------------------
// Image download
// ---------------------------------------------------------------------------
let downloaded = 0, skipped = 0;
const failed = [];
if (DOWNLOAD) {
  const entries = [...imageRefs.entries()];
  console.log(`downloading ${entries.length} images…`);
  const CONC = 8;
  for (let i = 0; i < entries.length; i += CONC) {
    await Promise.all(entries.slice(i, i + CONC).map(async ([remote, local]) => {
      const dest = join(ROOT, 'public', local);
      if (existsSync(dest)) { skipped++; return; }
      try {
        let res = await fetch(remote, { redirect: 'follow' });
        if (!res.ok) {
          // scaled variant gone? try the original file
          const orig = remote.replace(/-\d+x\d+(\.[a-z]+)$/i, '$1');
          if (orig !== remote) res = await fetch(orig, { redirect: 'follow' });
        }
        if (!res.ok) { failed.push(`${res.status} ${remote}`); return; }
        mkdirSync(dirname(dest), { recursive: true });
        writeFileSync(dest, Buffer.from(await res.arrayBuffer()));
        downloaded++;
      } catch (e) { failed.push(`ERR ${remote} (${e.message})`); }
    }));
  }
}

// ---------------------------------------------------------------------------
// Report
// ---------------------------------------------------------------------------
const rpt = `# Migration conversion report

- Blog posts written: ${report.blog} (${redirects.length} redirects)
- People written: ${report.people}
- Drafts (across both): ${report.drafts}
- Images referenced: ${imageRefs.size}${DOWNLOAD ? ` — downloaded ${downloaded}, already present ${skipped}, FAILED ${failed.length}` : ' (run with --download-images to fetch)'}
- Descriptions auto-generated from body text: ${report.guessedDesc.length}
- Posts with EMPTY body: ${report.emptyBody.join(', ') || 'none'}
- Posts with kept <iframe> embeds (check rendering): ${report.keptIframes.join(', ') || 'none'}
- External (non-steamhead) images left remote: ${report.externalImgs.size}
- VIDEOS left pointing at the old site — must move to YouTube/Drive before
  domain cutover: ${videoRefs.size ? '\n' + [...videoRefs].map(v => `  - ${v}`).join('\n') : 'none'}

## Failed image downloads
${failed.length ? failed.map(f => `- ${f}`).join('\n') : '- none'}
`;
writeFileSync(join(ROOT, 'scripts/migration-report.md'), rpt);
console.log(rpt);
