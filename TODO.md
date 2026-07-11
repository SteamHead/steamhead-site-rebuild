# Site TODO

Requests captured during review. Header/footer items from 2026-07-10
(blog link, Programs dropdown, logo graphic, media kit link, favicon) were
implemented in PR #9 — see GitHub issues #3–#7.

## Content

- [ ] **Blake to provide the 5 missing videos** — 5 videos couldn't be pulled
      from the old site during migration (list in `scripts/migration-report.md`
      + MIGRATION.md parking lot, incl. the 96 MB `output2.mp4` from the Snow
      Drop post). Blake has the source files; once provided, upload to YouTube
      and replace the old-site URLs in the affected posts. Must happen before
      domain cutover. (Logged 2026-07-11 — Blake asked not to be allowed to
      forget this.)
- [ ] **Alt text for all images** — migrated post images currently reuse the
      post title as alt text; real descriptive alt text should be generated
      (AI-assisted pass over ~300 images) or hand-written for the important
      ones. Accessibility item from the evaluation's week-6 pass.
      (Blake, 2026-07-11)
- [ ] **Media kit page** — footer currently links the old-site URL
      (`steamhead.space/media_kit/`); needs a home here before domain cutover.
- [ ] **makefashion.ca/edu mirror** — static snapshot under
      `/makefashion-edu/site/`, original stays up. Planned as its own work
      chain after the current PR deploys. (Blake, 2026-07-11)
- [ ] **Instagram content/photos on MakeFashion Edu page** — the old page
      had a "Follow us on Instagram" section with photos; the new page has
      neither. Needs a design decision: live embed (third-party script) vs.
      a curated static photo grid linking to the account. (Carrie's review,
      2026-07-11)
