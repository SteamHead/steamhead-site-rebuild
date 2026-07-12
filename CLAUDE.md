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

## Content schema (locked 2026-07-10)

Blog frontmatter is enforced by strict zod schemas in `src/content.config.ts`
— a malformed or unknown field fails the build instead of publishing broken.
Blog fields: `title`, `date`, `description`, `author`, `program`,
`categories`, `tags`, `image?`, `imageAlt?`, `event?`, `media`, `draft`.
A separate `people` collection holds Team/Resident profiles (never shown in
the blog). Filename = URL slug: posts render at `/blog/<filename>/`.
See MIGRATION.md for the full locked migration decisions. Keep `config.yml`
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
4. **Design tokens**: all colors, shadows, and font sizes come from the
   `:root` tokens in `src/styles/global.css` (sourced from the brand guide,
   `public/downloads/2021_SteamHead_Brand_Guide.pdf`). Don't introduce ad-hoc
   hex values in pages/components — add or reuse a token. Sole exception:
   the categorical badge-pathway colors in `maker-badges.astro`.

## Pointers

- `CMS-SETUP.md` — Sveltia OAuth setup (auth Worker, GitHub OAuth app,
  secrets) and local CMS development.
- `reference/` — converted Markdown of every old WordPress page, the SteamHead
  brand guide PDF, and the 2022 MakeFashion Edu combined guide. Source
  material for content and design-token work; not served by the site.
- `blog-post-inventory.md` — curation checklist of all 176 old blog posts
  (163 published + 13 drafts); mark keepers `[x]` before migration.

## New machine setup

Everything needed to continue lives in this repo except two things:

1. **Cloudflare API token** — create a `.env` in the repo root (gitignored):
   ```
   CLOUDFLARE_API_TOKEN=<token>
   CLOUDFLARE_ACCOUNT_ID=068bd0bae77f7c068677cd14996466fe
   ```
   Token lives in the team password manager, or mint a new one at
   dash.cloudflare.com → My Profile → API Tokens ("Edit Cloudflare Workers"
   template, scoped to James's account only). Wrangler reads `.env`
   automatically. Never commit it.
2. **WordPress export XML** (`steamhead.WordPress.2026-07-11.xml`, ~3.6 MB,
   migration source for the old blog) — archived in the SteamHead Google
   Drive. Do NOT commit it to this repo: it's gitignored deliberately
   because the repo is intended to go public and a raw WordPress export
   can contain non-public data (draft posts, commenter emails).

Then: `npm install && npm run dev`. Deploys happen automatically on push to
main (Workers Builds); manual fallback is `npm run deploy`.
