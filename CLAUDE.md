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

**Fixed 2026-08-15.** Pushing to `main` now auto-deploys the live site. The
history below explains a confusion that persisted for a week — read it before
trusting any older note about deploys.

- **`steamhead` is the only Worker.** It serves `steamhead.space` and
  `www.steamhead.space` (custom domains, both enabled) and now has the
  git-connected Workers Builds pipeline on `main`.
- **`steamhead-astro-scaffold` was deleted 2026-08-15.** It never held a custom
  domain or route and carried no production traffic — but it owned the *only*
  build pipeline. So from 2026-08-08 to 2026-08-15 every push built and deployed
  a Worker nobody could reach, while the public site updated only when someone
  ran `npm run deploy` by hand. The live site looked current purely because
  nobody pushed between Aug 9 and Aug 15.
- **Build settings:** build `npm run build`, deploy `npx wrangler deploy`, root
  `/`, branch `main`. Do NOT set the deploy command to `npm run deploy` — that
  script is `npm run build && wrangler deploy`, so it would build twice.
- **`.nvmrc` pins Node 22 and must stay.** Astro 6 requires >=22.12, declared in
  `package.json` engines — which Workers Builds does not read. Without `.nvmrc`
  a build can fail on whatever Node version Cloudflare happens to default to.
- Deploys go to **James's Cloudflare account**, account ID
  `068bd0bae77f7c068677cd14996466fe`. **Caveat: `wrangler login` can see two
  accounts** — always confirm you are targeting this account ID before any
  manual `wrangler deploy` or dashboard work.
- Manual deploy remains the fallback: `npm run deploy` with
  `CLOUDFLARE_API_TOKEN` in `.env` (gitignored, so absent from fresh clones).
- Local preview of the Worker build: `npm run preview`.

⚠️ **To verify which Worker a build actually targeted**, read the GitHub
check-run's `output.summary` — it names the script explicitly:
`gh api repos/SteamHead/steamhead-site-rebuild/commits/main/check-runs`.
On 2026-08-15 Cloudflare's AI dashboard assistant reported "no build
configuration" on both Workers *while the scaffold pipeline was actively
building*. It was right about domains and wrong about build config. Trust the
check-run over the assistant.

⚠️ **Pushing to `main` publishes to the public site immediately.** There is no
staging step and no review gate. Preview with `npm run dev -- --host` and check
`http://splinter:4321` before you push.

## Content schema (locked 2026-07-10)

Blog frontmatter is enforced by strict zod schemas in `src/content.config.ts`
— a malformed or unknown field fails the build instead of publishing broken.
Blog fields: `title`, `date`, `description`, `author`, `program`,
`categories`, `tags`, `image?`, `imageAlt?`, `event?`, `media`, `draft`.
A separate `people` collection holds Team/Resident profiles (never shown in
the blog). Filename = URL slug: posts render at `/blog/<filename>/`.
See MIGRATION.md for the full locked migration decisions. Keep `config.yml`
(CMS fields) and `content.config.ts` (build validation) in sync when the
schema changes. The `mfedu`, `guides`, and `courses` collections are
repo-edited (not exposed in the CMS).

## Sections built on top of the migration

- **People** (`src/content/people/` + `src/lib/people.ts`): card grids on
  /about-us; profiles WITH body content get pages at /people/<slug>/ with
  build-time "blog mentions" (name-matched across all posts, nickname-aware).
  Frontmatter-only profiles are cards without links — that's intentional.
- **Courses** (`src/content/courses/<course>/*.md`): two live courses —
  the 2022 original at /courses/mfedu-intro/ (worksheet PDFs in
  /downloads/mfedu-course/) and Blake's 2026 rewrite "Advocacy by Design"
  at /courses/mfedu-2026/ (printable web worksheets under
  .../worksheets/, SVG illustrations in /images/courses/mfedu-2026/).
  Progress is localStorage per course ('course-progress:<course>');
  lessons auto-complete on visit. Lesson files live in per-course
  subfolders; pages derive the URL slug via `id.split('/').pop()`.

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

Everything needed to continue lives in this repo except a few things:

1. **Cloudflare API token** — create a `.env` in the repo root (gitignored):
   ```
   CLOUDFLARE_API_TOKEN=<token>
   CLOUDFLARE_ACCOUNT_ID=068bd0bae77f7c068677cd14996466fe
   ```
   Token lives in the team password manager, or mint a new one at
   dash.cloudflare.com → My Profile → API Tokens ("Edit Cloudflare Workers"
   template, scoped to James's account only). Wrangler reads `.env`
   automatically. Never commit it. **Already set up on Blake's machine**
   as of 2026-08-08 — token is Workers-scoped only (no Zone/DNS permission,
   so it can't read or edit DNS records; attaching a custom domain to a
   Worker also needs to be done by hand in the dashboard, not via API).
2. **Node.js >=22.12.0 is required** (Astro 6 refuses to build on anything
   older — v20 fails with "Node.js v20.x.x is not supported by Astro!").
   If a machine/sandbox has no Node, or an older one, and there's no sudo
   for a system install, a portable no-sudo install works fine:
   ```
   curl -sL -o node.tar.xz https://nodejs.org/dist/v22.12.0/node-v22.12.0-linux-x64.tar.xz
   tar -xJf node.tar.xz --strip-components=1 -C <some local dir>
   export PATH="<that dir>/bin:$PATH"
   ```
   Then `npm install && npm run build` works normally. (Used on 2026-08-08
   in a sandbox with no Node at all, downloaded straight into the session's
   scratch dir — not persistent, so redo it if it's gone next session.)
3. **WordPress export XML** (`steamhead.WordPress.2026-07-11.xml`, ~3.6 MB,
   migration source for the old blog) — archived in the SteamHead Google
   Drive. Do NOT commit it to this repo: it's gitignored deliberately
   because the repo is intended to go public and a raw WordPress export
   can contain non-public data (draft posts, commenter emails).
4. **Full WordPress media backup** (UpdraftPlus, taken 2026-08-08 11pm,
   covers everything the migration script didn't — see the video re-hosting
   item in TODO.md) — saved to the "shmac" laptop and SteamHead's OneDrive,
   not in this repo or Drive.

Then: `npm install && npm run dev`. **Deploys are NOT fully automatic right
now** — see "Deploy path" above for the `steamhead` vs
`steamhead-astro-scaffold` split; manual deploy is `npm run deploy`.
