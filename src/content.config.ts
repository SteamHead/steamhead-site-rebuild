// Astro Content Collections schema (Astro 5 Content Layer API)
// Defines the shape of every Markdown file the CMS can read/write.
// Astro validates frontmatter against these schemas at build time,
// so a typo in a content file becomes a clear error rather than a silent bug.
//
// The blog and people schemas are LOCKED for the WordPress migration —
// see MIGRATION.md before changing them. `.strict()` makes unknown
// frontmatter keys a build error, so AI-drafted posts can't sneak in
// malformed fields.

import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Blog posts — "Great Things Blog".
// Filename = URL slug (posts render at /blog/<filename>/), so migrated
// posts keep their WordPress post-name as the filename.
const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title:       z.string(),
    date:        z.coerce.date(),
    description: z.string(),
    // Human author, or "Blake" for AI-drafted posts (which arrive via PR).
    author:      z.string(),
    // Which program the post belongs to; drives future filtering.
    program:     z.enum(['makefashion-edu', 'neighborhood-earth', 'system-upgrade', 'general']).default('general'),
    // Original WordPress categories/tags, preserved verbatim for future
    // use (per-person pages, program filters, the RAG pipeline).
    categories:  z.array(z.string()).default([]),
    tags:        z.array(z.string()).default([]),
    image:       z.string().optional(),
    imageAlt:    z.string().optional(),
    // Optional pointers for the AI publishing pipeline: the event a post
    // covers and the source media (YouTube/Drive URLs) it draws on.
    event:       z.string().optional(),
    media:       z.array(z.string()).default([]),
    // Drafts are kept in the repo but never built into the site.
    draft:       z.boolean().default(false),
  }).strict(),
});

// People — SteamHead Team & Residents profiles. Migrated from the old
// blog's "SteamHead Team" / "SteamHead Residents" category posts; these
// never appear in the blog index. Presentation (pages/popups) is TBD.
const people = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/people' }),
  schema: z.object({
    name:        z.string(),
    role:        z.enum(['team', 'resident']),
    // Original post title, when it was more than just the person's name.
    title:       z.string().optional(),
    date:        z.coerce.date(),
    description: z.string().optional(),
    image:       z.string().optional(),
    imageAlt:    z.string().optional(),
    draft:       z.boolean().default(false),
  }).strict(),
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

// MakeFashion Edu subsite pages (runway shows, Run the Program steps,
// partners) — migrated from makefashion.ca/edu; rendered under
// /makefashion-edu/<slug>/ with the MFEdu section nav.
const mfedu = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/mfedu' }),
  schema: z.object({
    title:       z.string(),
    section:     z.enum(['runway-shows', 'run-the-program', 'about']),
    order:       z.number(),
    description: z.string().optional(),
  }).strict(),
});

// Long-form resource guides (course guides, activity guides, etc.)
const guides = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/guides' }),
  schema: z.object({
    title:       z.string(),
    description: z.string(),
  }),
});

// Course lessons — sequential self-paced courses. Lessons render at
// /courses/<course>/<filename>/ with prev/next navigation and
// localStorage progress (no accounts). `order` drives the sequence;
// `section` is the grouping label shown on the course landing page.
const courses = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/courses' }),
  schema: z.object({
    title:       z.string(),
    course:      z.enum(['mfedu-intro', 'mfedu-2026']),
    order:       z.number(),
    section:     z.string(),
    description: z.string().optional(),
    // Maker Badges pathway this lesson feeds (2026 course) — shown as a
    // chip linking to /maker-badges/.
    badge:       z.string().optional(),
  }).strict(),
});

export const collections = { blog, people, pages, settings, guides, mfedu, courses };
