// @ts-check
import { defineConfig } from 'astro/config';
import cloudflare from '@astrojs/cloudflare';

// https://astro.build/config
export default defineConfig({
	// Deploys as a Cloudflare Worker (see wrangler.jsonc, which points its
	// `main` at this adapter's server entrypoint). Pages are prerendered
	// static by default; the Worker serves them via the ASSETS binding.
	adapter: cloudflare(),
	// Final production domain — used for canonical URLs, sitemap, and RSS.
	// The site is built/reviewed on workers.dev first; this points at where
	// it will ultimately live.
	site: 'https://steamhead.space',
});
