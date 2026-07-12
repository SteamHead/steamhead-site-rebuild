# Site TODO

Working list, kept current by Blake's Claude sessions. GitHub issues mirror
the items teammates need visibility on.

## Waiting on Blake

- [ ] **The 5 missing videos** — upload to the SteamHead Productions YouTube
      channel, then hand the YouTube URLs to Claude (posts auto-embed
      YouTube links). Source files, by original name:
      1. `1514.mp4` (Mar 2021) — MG Space Cardboard Engineering post
      2. `1515.mp4` (Mar 2021) — MG Space Cardboard Engineering post
      3. `1516.mp4` (Mar 2021) — Inventing Pinball post
      4. `03-未来城市-复盘-双语字幕-low… .mov` (Jan 2025) — bilingual-subtitle
         recap video
      5. `output2.mp4` (Mar 2026, 96 MB) — Snow Drop Grade 2 post
      Must be done before domain cutover (their old-site URLs die then).
- [ ] **Carrie's origin-story voice memo** — polish "Born in Shenzhen" when
      it arrives; keep the heritage copy file word-for-word identical.

## Queued work

- [ ] **Alt-text pass** (~300 migrated images) — GitHub issue #8. Next up.
- [ ] **Design Immersion Curriculum + Maker Badges pages** — the media kit's
      Certification section links these on the old site; need homes or
      redirects before domain cutover.
- [ ] **People section design** — 41 Team/Resident profiles migrated and
      waiting; pages vs. popups is a design discussion with Mapet.
- [ ] **MFEdu course-sequence build** — sequential Astro pages with
      localStorage progress; then repoint the course CTAs (flagged in
      makefashion-edu.astro) from /shelf/ to the real course landing.
- [ ] **Design-token pass** from the brand guide + Mapet design review.
- [ ] **Ben: heritage page on WordPress** — paste-ready copy in
      reference/makefashion-ca-edu-heritage-copy.md.

## Domain cutover checklist (target: by Sept 1, HostPresto renewal Sept 7)

- [ ] Videos re-hosted (above)
- [ ] Old-site links resolved: certification pages, any remaining
      steamhead.space/wp-content references
- [ ] Add steamhead.space zone to James's Cloudflare account; attach custom
      domain to the Worker
- [ ] Update GitHub OAuth app homepage URL
- [ ] Final WordPress export archived in Drive; decline HostPresto renewal
- [ ] Repo public flip (secrets scan already clean) — optional, any time
