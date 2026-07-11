// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
	// Final production domain — used for canonical URLs, sitemap, and RSS.
	// The site is built/reviewed on workers.dev first; this points at where
	// it will ultimately live.
	site: 'https://steamhead.space',
});
