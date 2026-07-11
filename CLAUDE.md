# CLAUDE.md — SteamHead Site Rebuild

Rebuild of steamhead.space. The old WordPress site is being retired; this repo
is the surviving source of truth (the machine that did the earlier work died).

## Stack

- **Astro 6** static-first site, **@astrojs/cloudflare** adapter, deployed as a
  **Cloudflare Worker** (NOT Cloudflare Pages — ignore any doc that says Pages).
- **Sveltia CMS** at `/admin/` (config in `public/admin/config.yml`) so
  non-technical staff edit content in the browser; saves become git commits.
- Content is Markdown in `src/content/` (blog, pages, settings, guides),
  validated by zod schemas in `src/content.config.ts`.
- No database, no LMS, no hosted media: courses are sequential Astro pages with
  localStorage progress; video/docs are embedded or linked from YouTube and
  Google Drive, never hosted in this repo.

## Deploy path

- Push to `main` on GitHub (`SteamHead/steamhead-site-rebuild`) → Cloudflare
  Workers Builds auto-builds and deploys the Worker (`steamhead-astro-scaffold`
  per `wrangler.jsonc`).
- Deploys go to **James's Cloudflare account**, account ID
  `068bd0bae77f7c068677cd14996466fe`. **Caveat: `wrangler login` can see two
  accounts** — always confirm you're targeting this account ID before any
  manual `wrangler deploy` or dashboard work.
- Manual deploy: `npm run deploy` (build + `wrangler deploy`).
  Local preview of the Worker: `npm run preview`.

## Content schema plan

Blog frontmatter is enforced by zod in `src/content.config.ts` — a malformed
post fails the build instead of publishing broken. Current fields: `title`,
`date`, `description`, `image?`, `imageAlt?`. Planned additions (keep strict):
`author`, `program` (Neighborhood Earth / System Upgrade / MakeFashion Edu /
general), event reference, media list, `draft` flag. Keep `config.yml`
(CMS fields) and `content.config.ts` (build validation) in sync when the
schema changes.

## Rules

1. **AI-drafted posts arrive as pull requests, never direct commits to
   `main`.** Pipeline-drafted posts carry `author: Blake` (SteamHead's
   openly-disclosed, human-reviewed AI teammate). A human reads the diff and
   merges. Do not bypass this even for "trivial" posts.
2. **`local_backend: true` must never be committed** in
   `public/admin/config.yml`. It's for local CMS dev only (see CMS-SETUP.md);
   committed, it breaks CMS login on the live site.
3. The RAG/drafting pipeline is a separate project. This site only exposes the
   interface: strict schema + PR review gate.

## Pointers

- `CMS-SETUP.md` — Sveltia OAuth setup (auth Worker, GitHub OAuth app,
  secrets) and local CMS development.
- `reference/` — converted Markdown of every old WordPress page, the SteamHead
  brand guide PDF, and the 2022 MakeFashion Edu combined guide. Source
  material for content and design-token work; not served by the site.
