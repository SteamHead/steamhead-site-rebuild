# Blog Migration Plan — WordPress → Content Collections

Locked decisions for migrating the old steamhead.space WordPress blog into
this repo. The source is `steamhead.WordPress.2026-07-11.xml` (archived in
the SteamHead Google Drive; NOT in this repo — see CLAUDE.md). Schema lock
date: 2026-07-10.

## Locked decisions

1. **All 176 posts migrate** (163 published + 13 drafts). No curation cut.
   `blog-post-inventory.md` lists them.
2. **Blog URLs move to `/blog/<post-name>/`.** Old WordPress permalinks were
   root-level (`steamhead.space/<post-name>/`, permalink setting "post name").
   The converter generates a `public/_redirects` file that 301s every old
   published-post URL to its `/blog/` home. Workers static assets serve
   `_redirects` natively.
3. **Filename = URL slug.** Each post becomes
   `src/content/blog/<post-name>.md`, keeping the WordPress `post_name`
   verbatim so the redirect map is one-to-one. No date prefixes.
4. **Profile posts become people, not blog posts.** The 41 posts categorized
   `SteamHead Team` (14) or `SteamHead Residents` (27) convert into
   `src/content/people/` with `role: team | resident`. They never appear in
   the blog index. Their old URLs get redirects once the people section
   exists (presentation — pages vs. popups — is a design decision for later;
   keep a slug→person mapping in the converter output so those redirects
   can be generated then).
5. **Drafts convert with `draft: true`** and are excluded from every build
   (index and post pages) by the collection filters.
6. **Frontmatter carries everything forward**: original categories and tags
   verbatim, author from `dc:creator` (James ×146, Carrie, Mike, Mapet,
   Avery, plus `admin`/`catherineyang920`/`Angry Duck` → map to real names
   or "SteamHead" during conversion), and `program` derived from categories
   (`MakeFashion Edu` → makefashion-edu, `Neighborhood Earth` →
   neighborhood-earth, else general — there is no System Upgrade category
   in the old data).
7. **Schemas are strict** (`content.config.ts`): unknown frontmatter keys
   fail the build. Change the schema deliberately, not ad hoc, and keep
   `public/admin/config.yml` in sync.

## Converter checklist (the mechanical pass)

- [ ] Parse XML → markdown via a script tuned to the schema above
      (turndown/pandoc for HTML→MD, or `wordpress-export-to-markdown`
      as a starting point — but the frontmatter must match exactly).
- [ ] `description`: WordPress posts have no meta description — generate
      from the excerpt if present, else first ~25 words of body text.
- [ ] **10 posts have empty slugs and 9 have duplicate slugs** (mostly
      drafts): generate slugs from titles, suffix duplicates (`-2`).
- [ ] Media: download referenced images from the live site while it's still
      up, rewrite URLs to `/images/...` repo paths (the repo already has
      `public/images/<year>/<month>/` mirroring the WP uploads layout).
      Keep YouTube/Drive embeds as embeds — never download those.
- [ ] Generate `public/_redirects`: `/<old-slug>/ /blog/<old-slug>/ 301`
      for each published blog post (NOT people, NOT drafts).
- [ ] Emit `people-slug-map.json` (old slug → person) for the future
      people-section redirects.
- [ ] Spot-check: a human reads ~10 converted posts against the live site
      before the import PR merges.
- [ ] The import lands as ONE pull request, not a direct push, so the diff
      is reviewable and the preview build can be checked.

## Out of scope for the migration (design discussions for later)

People presentation (pages/popup/both), blog index pagination and program
filters, per-person pages from the person-name categories, comments (old
post comments are archived in the XML but not migrated), and anything
visual. New ideas discovered mid-migration go here, not into the critical
path:

### Parking lot

- **4 videos must move to YouTube/Drive before domain cutover** — they're
  currently linked at their old steamhead.space/wp-content URLs, which die
  when the domain moves. List in `scripts/migration-report.md` (three 2021
  clips and the 96 MB `output2.mp4` from the Snow Drop post — too big for
  Workers assets even if we wanted to host it). The fifth, a 2025 .mov in
  the MG Space Cardboard Engineering post, was unrecoverable (already gone
  from the dead server) — that post was removed instead, see TODO.md.
- 4 images 404'd on the live site during download (see report) — posts
  reference them but the originals are already gone; decide fix or remove.
- 4 posts kept raw `<iframe>` embeds — check they render acceptably:
  friendship-team-moralture…, htm-photo-studio-final-review-2,
  home-automation-project, fuse33-lidar-scan.
- 22 external (non-steamhead) images left hotlinked — fine for now, but
  they can rot; consider localizing the important ones.
- Author "James" vs "James Simpson" (from `admin`) are currently two
  distinct author strings — unify if they're the same person.
