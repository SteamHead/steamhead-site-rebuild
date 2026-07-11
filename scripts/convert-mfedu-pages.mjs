// makefashion.ca/edu subsite pages → src/content/mfedu/ markdown.
// Converts the Runway Shows tree, Run the Program pages, Resources, and
// Partners from reference/makefashionedu.WordPress.2026-07-11.xml.
// Rerunnable; wipes and regenerates src/content/mfedu/.
//
//   node scripts/convert-mfedu-pages.mjs <export.xml> [--download-images]

import { readFileSync, writeFileSync, mkdirSync, rmSync, existsSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import TurndownService from 'turndown';
import { gfm } from 'turndown-plugin-gfm';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const XML_PATH = process.argv[2];
const DOWNLOAD = process.argv.includes('--download-images');

// slug -> [section, order, display title override]
const PAGES = {
  'runwayshows':                        ['runway-shows', 0, 'Runway Shows'],
  'tucson2022':                         ['runway-shows', 1, 'Tucson 2022'],
  'tucson2021':                         ['runway-shows', 2, 'Tucson 2021'],
  'tucson2020':                         ['runway-shows', 3, 'Tucson 2020'],
  'tucson2019':                         ['runway-shows', 4, 'Tucson 2019'],
  'sanmarcos2020s2':                    ['runway-shows', 5, 'San Marcos 2020 S2'],
  'sanmarcos2020s1':                    ['runway-shows', 6, 'San Marcos 2020 S1'],
  'shenzhen2019':                       ['runway-shows', 7, 'Shenzhen 2019'],
  'shenzhen2018':                       ['runway-shows', 8, 'Shenzhen 2018'],
  'calgary2019':                        ['runway-shows', 9, 'Calgary 2019'],
  'mfedu-program-benefits':             ['run-the-program', 1, 'Program Benefits'],
  'mfedu-get-ready':                    ['run-the-program', 2, 'Get Ready'],
  'mfedu-facilitate-the-curriculum':    ['run-the-program', 3, 'Facilitate the Curriculum'],
  'mfedu-exhibit-the-results':          ['run-the-program', 4, 'Exhibit the Results'],
  'mfedu-publish-with-makefashion-edu': ['run-the-program', 5, 'Publish with MakeFashion Edu'],
  'resources':                          ['run-the-program', 6, 'Resources'],
  'partners':                           ['about', 1, 'Our Partners'],
};

const xml = readFileSync(XML_PATH, 'utf8').replace(/\r\n?/g, '\n');
const items = xml.split('<item>').slice(1).map(s => s.split('</item>')[0]);
const unesc = s => s.replaceAll('&amp;', '&').replaceAll('&lt;', '<').replaceAll('&gt;', '>').replaceAll('&quot;', '"').replaceAll('&#039;', "'");
function field(block, tag) {
  const m = block.match(new RegExp(`<${tag}[^>]*>(?:<!\\[CDATA\\[([\\s\\S]*?)\\]\\]>|([\\s\\S]*?))</${tag}>`));
  if (!m) return '';
  return m[1] !== undefined ? m[1] : unesc(m[2] ?? '');
}

const attachments = {};
for (const it of items) {
  if (field(it, 'wp:post_type') !== 'attachment') continue;
  attachments[field(it, 'wp:post_id')] = field(it, 'wp:attachment_url');
}

const td = new TurndownService({ headingStyle: 'atx', codeBlockStyle: 'fenced', bulletListMarker: '-' });
td.use(gfm);
td.keep(['iframe']);

function attrsOf(sc) {
  const out = {}; const re = /(\w+)="([^"]*)"/g; let m;
  while ((m = re.exec(sc))) out[m[1]] = m[2];
  return out;
}

function preprocess(html) {
  let s = html;
  s = s.replace(/<!-- \/?wp:[\s\S]*?-->/g, '');
  s = s.replaceAll('[et_pb_line_break_holder]', '\n');
  s = s.replace(/\[et_pb_image([^\]]*)\][\s\S]*?\[\/et_pb_image\]|\[et_pb_image([^\]]*)\/?\]/g, (_, a1, a2) => {
    const a = attrsOf(a1 ?? a2 ?? '');
    return a.src ? `<img src="${a.src}" alt="${a.alt ?? ''}">` : '';
  });
  s = s.replace(/\[et_pb_video([^\]]*)\][\s\S]*?\[\/et_pb_video\]|\[et_pb_video([^\]]*)\/?\]/g, (_, a1, a2) => {
    const a = attrsOf(a1 ?? a2 ?? '');
    return a.src ? `\n\n${a.src}\n\n` : '';
  });
  s = s.replace(/\[et_pb_gallery([^\]]*)\/?\](?:\[\/et_pb_gallery\])?/g, (_, attrs) => {
    const ids = (attrsOf(attrs).gallery_ids ?? '').split(',').filter(Boolean);
    return '\n<div class="page-gallery">\n' +
      ids.map(id => attachments[id] ? `<img src="${attachments[id]}" alt="">` : '').join('\n') +
      '\n</div>\n';
  });
  s = s.replace(/\[gallery([^\]]*)\]/g, (_, attrs) => {
    const ids = (attrsOf(attrs).ids ?? '').split(',').filter(Boolean);
    return '\n<div class="page-gallery">\n' +
      ids.map(id => attachments[id] ? `<img src="${attachments[id]}" alt="">` : '').join('\n') +
      '\n</div>\n';
  });
  s = s.replace(/\[et_pb_button([^\]]*)\/?\](?:\[\/et_pb_button\])?/g, (_, attrs) => {
    const a = attrsOf(attrs);
    return a.button_url ? `\n\n[${a.button_text ?? 'Learn More'}](${a.button_url})\n\n` : '';
  });
  s = s.replace(/\[et_pb_toggle([^\]]*)\]([\s\S]*?)\[\/et_pb_toggle\]/g, (_, attrs, inner) => {
    const a = attrsOf(attrs);
    return `\n\n### ${a.title ?? ''}\n\n${inner}\n\n`;
  });
  s = s.replace(/\[caption[^\]]*\]([\s\S]*?)\[\/caption\]/g, (_, inner) => {
    const img = inner.match(/<img[^>]*>/)?.[0] ?? '';
    const text = inner.replace(/<img[^>]*>/, '').replace(/<[^>]+>/g, '').trim();
    return `${img}\n\n${text ? `*${text}*\n\n` : ''}`;
  });
  s = s.replace(/\[embed[^\]]*\]([\s\S]*?)\[\/embed\]/g, '\n\n$1\n\n');
  s = s.replace(/\[instagram-feed[^\]]*\]/g, '');
  s = s.replace(/\[wpforms[^\]]*\]/g, '');
  s = s.replace(/\[\/?et_pb_[a-z_]+[^\]]*\]/g, '\n');
  // wpautop-lite
  return s.split(/\n{2,}/).map(chunk => {
    const c = chunk.trim();
    if (!c) return '';
    if (/^<\/?(p|div|h[1-6]|ul|ol|li|blockquote|figure|table|pre|iframe|img|hr)\b/i.test(c)) return c;
    return `<p>${c.replace(/\n/g, '<br>')}</p>`;
  }).join('\n');
}

const imageRefs = new Map();
function localize(url) {
  const m = url.match(/\/edu\/wp-content\/uploads\/(\d{4})\/(\d{2})\/([^"'\s)?]+)/);
  if (!m) return url;
  if (/\.(mp4|mov|m4v|avi|webm)$/i.test(m[3])) return url;
  const local = `/images/mfedu/${m[1]}/${m[2]}/${decodeURIComponent(m[3])}`;
  imageRefs.set(url.startsWith('http') ? url : `http://www.makefashion.ca${url}`, local);
  return local;
}

function rewrite(md) {
  md = md.replace(/https?:\/\/(?:www\.)?makefashion\.ca\/edu\/wp-content\/uploads\/[^\s"')]+/g, localize);
  md = md.replace(/https?:\/\/(?:www\.)?makefashion\.ca\/edu\/([a-z0-9-]+)\/?(?=[\s"')]|$)/g,
    (full, slug) => PAGES[slug] ? `/makefashion-edu/${slug}/` : full);
  md = md.replace(/https?:\/\/(?:www\.)?makefashion\.ca\/edu\/?(?=[\s"')]|$)/g, '/makefashion-edu/');
  md = md.replace(/https?:\/\/(?:www\.)?steamhead\.space\/steamhead-online-learning\/?/g, '/shelf/');
  md = md.replace(/https?:\/\/(?:www\.)?makefashion\.org\/edu\/?(?=[\s"')]|$)/g, '/makefashion-edu/');
  return md;
}

const outDir = join(ROOT, 'src/content/mfedu');
rmSync(outDir, { recursive: true, force: true });
mkdirSync(outDir, { recursive: true });

const report = [];
for (const it of items) {
  if (field(it, 'wp:post_type') !== 'page') continue;
  const slug = field(it, 'wp:post_name');
  if (!(slug in PAGES)) continue;
  const [section, order, title] = PAGES[slug];
  let md = td.turndown(preprocess(field(it, 'content:encoded')));
  md = md.replace(/\n{3,}/g, '\n\n').replace(/^# /gm, '## ').trim();
  md = rewrite(md);
  const yq = s => `"${String(s).replace(/"/g, '\\"')}"`;
  writeFileSync(join(outDir, `${slug}.md`),
    `---\ntitle: ${yq(title)}\nsection: ${section}\norder: ${order}\n---\n\n${md}\n`);
  report.push(`${slug} (${md.length} chars)`);
}

console.log(`converted ${report.length} pages:`);
report.forEach(r => console.log(' ', r));
console.log(`images referenced: ${imageRefs.size}`);

if (DOWNLOAD) {
  let ok = 0, skip = 0; const failed = [];
  const entries = [...imageRefs.entries()];
  const CONC = 4;
  for (let i = 0; i < entries.length; i += CONC) {
    await Promise.all(entries.slice(i, i + CONC).map(async ([remote, local]) => {
      const dest = join(ROOT, 'public', local);
      if (existsSync(dest)) { skip++; return; }
      try {
        let res = await fetch(remote, { redirect: 'follow', signal: AbortSignal.timeout(90000) });
        if (!res.ok) {
          const orig = remote.replace(/-\d+x\d+(\.[a-z]+)$/i, '$1');
          if (orig !== remote) res = await fetch(orig, { redirect: 'follow', signal: AbortSignal.timeout(90000) });
        }
        if (!res.ok) { failed.push(`${res.status} ${remote}`); return; }
        mkdirSync(dirname(dest), { recursive: true });
        writeFileSync(dest, Buffer.from(await res.arrayBuffer()));
        ok++;
      } catch (e) { failed.push(`ERR ${remote} (${e.message})`); }
    }));
    if (i % 40 === 0) console.log(`  ...${Math.min(i + CONC, entries.length)}/${entries.length}`);
  }
  console.log(`downloaded ${ok}, already present ${skip}, FAILED ${failed.length}`);
  failed.forEach(f => console.log('  FAIL', f));
  writeFileSync(join(ROOT, 'scripts/mfedu-pages-report.txt'),
    report.join('\n') + `\n\nimages: ${imageRefs.size}, downloaded ${ok}, failed ${failed.length}\n` + failed.join('\n') + '\n');
}
