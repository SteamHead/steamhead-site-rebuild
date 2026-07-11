// @ts-check
import { defineConfig } from 'astro/config';
import cloudflare from '@astrojs/cloudflare';
import { visit } from 'unist-util-visit';

// Markdown paragraphs that are just a bare YouTube URL become responsive
// embeds. Content stays a plain URL (easy for the CMS and the converter);
// presentation happens here. Styles: .video-embed in global.css.
function remarkYouTubeEmbed() {
  const ytId = url =>
    url.match(/^https?:\/\/(?:www\.)?(?:youtube\.com\/(?:watch\?v=|embed\/)|youtu\.be\/)([\w-]{6,20})/)?.[1];
  return tree => {
    visit(tree, 'paragraph', node => {
      if (node.children.length !== 1) return;
      const child = node.children[0];
      const url = child.type === 'link' ? child.url
        : child.type === 'text' ? child.value.trim() : '';
      const id = url && !/\s/.test(url) ? ytId(url) : undefined;
      if (!id) return;
      node.type = 'html';
      node.children = undefined;
      node.value =
        `<div class="video-embed"><iframe src="https://www.youtube-nocookie.com/embed/${id}" ` +
        `title="YouTube video" loading="lazy" allowfullscreen ` +
        `allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"></iframe></div>`;
    });
  };
}

// https://astro.build/config
export default defineConfig({
	markdown: {
		remarkPlugins: [remarkYouTubeEmbed],
	},
	// Deploys as a Cloudflare Worker (see wrangler.jsonc, which points its
	// `main` at this adapter's server entrypoint). Pages are prerendered
	// static by default; the Worker serves them via the ASSETS binding.
	adapter: cloudflare(),
	// Final production domain — used for canonical URLs, sitemap, and RSS.
	// The site is built/reviewed on workers.dev first; this points at where
	// it will ultimately live.
	site: 'https://steamhead.space',
});
