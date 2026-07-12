# Site TODO

Working list, kept current by Blake's Claude sessions. GitHub issues mirror
the items teammates need visibility on.

## Waiting on Blake

- [ ] **The last missing video** — 4 of 5 are on YouTube and embedded
      (Inventing Pinball ×3, Snow Drop ×1). Remaining: the bilingual-subtitle
      class recap `.mov` in the MG Space Cardboard Engineering post — its
      old-site URL already 404s, so the file is gone from the server. It's
      actually three concatenated recap videos (01 Pen Holder Project /
      02 Future Robots / 03 Future City, 复盘-双语字幕-low). Likely sources:
      the DingTalk doc linked in that post, or Hardi Huang (MG Space).
## Queued work

- [x] **Alt-text pass** — done in PR #13 (issue #8): ~440 images described;
      no student names; galleries verified image-by-image. Flagged for later:
      4 people profiles share an LED-strip placeholder photo, 4 use cartoon
      avatars, and thats-a-wrap.md has a near-black photo worth replacing.
- [ ] **People section design** — 41 Team/Resident profiles migrated and
      waiting; pages vs. popups is a design discussion with Mapet.
- [ ] **MFEdu course-sequence build** — sequential Astro pages with
      localStorage progress; then repoint the course CTAs (flagged in
      makefashion-edu.astro) from /shelf/ to the real course landing.
- [ ] **Design-token pass** from the brand guide + Mapet design review.
- [x] **Ben: heritage page on WordPress** — live on makefashion.ca/edu and
      verified (wording matches reference/makefashion-ca-edu-heritage-copy.md,
      2015 date fixed on both sides).

## Domain cutover checklist (target: by Sept 1, HostPresto renewal Sept 7)

- [ ] Videos re-hosted (above)
- [ ] Old-site links resolved: any remaining steamhead.space/wp-content
      references (certification pages done: /design-immersion-overview/ and
      /maker-badges/ are live top-level pages — the overview URL is cited in
      academic papers and must never move)
- [ ] Add steamhead.space zone to James's Cloudflare account; attach custom
      domain to the Worker
- [ ] Update GitHub OAuth app homepage URL
- [ ] Final WordPress export archived in Drive; decline HostPresto renewal
- [ ] Repo public flip (secrets scan already clean) — optional, any time
