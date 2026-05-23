// Astro Content Collections schema (Astro 5 Content Layer API)
// Defines the shape of every Markdown file the CMS can read/write.
// Astro validates frontmatter against these schemas at build time,
// so a typo in a content file becomes a clear error rather than a silent bug.

import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Blog posts — created and managed by staff via the CMS
const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title:       z.string(),
    date:        z.coerce.date(),
    description: z.string(),
    image:       z.string().optional(),
    imageAlt:    z.string().optional(),
  }),
});

// Individual page content files — one per page, edited via CMS
const pages = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/pages' }),
  schema: z.object({}).passthrough(),
});

// Global site settings
const settings = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/settings' }),
  schema: z.object({}).passthrough(),
});

// Long-form resource guides (course guides, activity guides, etc.)
const guides = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/guides' }),
  schema: z.object({
    title:       z.string(),
    description: z.string(),
  }),
});

export const collections = { blog, pages, settings, guides };
