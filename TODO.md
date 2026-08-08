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
- [ ] **Missing 2022-course assets** — the Croquis worksheet Drive file is
      dead (404; a rebuilt web version ships with the 2026 course), and the
      Student Handout, Paper Sewing Guides, and "Design Process" video were
      never linked in the guide. Recover from the MFEdu Intro 2022 Drive
      folder if wanted for the original course at /courses/mfedu-intro/.
- [ ] **People photos** — 4 profiles share an LED-strip placeholder image
      (Emma, Marco Bartsch, Olivier, Kaspar) and 4 use cartoon avatars
      (Julia, Lauren Sassoubre, Maria Ellena Villagomez, Mapet Enriquez).
      Also thats-a-wrap.md has a near-black photo worth replacing.

## Reviews to schedule

- [ ] **Mapet token review** — how-to guide in tokenreview.md. Open items
      for her: badge-pathway pill colors, token-pass contrast fixes, people
      cards / "Read profile" indicator.
- [ ] **Mapet + Blake course review** — read-through of Advocacy by Design
      (/courses/mfedu-2026/, live): tone, pedagogy, teacher callouts. After
      review, decide whether sitewide course CTAs flip from the 2022 original
      to the 2026 edition (currently they point at /courses/mfedu-intro/;
      The Shelf offers both).

## Done (recent)

- [x] **Alt-text pass** — PR #13 (issue #8): ~440 images described.
- [x] **Design-token pass** — PR #14: all colors/shadows/sizes from
      global.css tokens; rule added to CLAUDE.md.
- [x] **People section** — PR #15: /about-us grids, 30 profile pages with
      build-time blog mentions, old profile URLs redirected.
- [x] **MFEdu Introduction Course (2022)** — PR #16: /courses/mfedu-intro/,
      14 lessons, localStorage progress, 11 worksheet PDFs mirrored.
- [x] **Advocacy by Design (2026)** — PR #17: /courses/mfedu-2026/, Blake's
      17-lesson rewrite (project arc + Level Up module, 9 printable web
      worksheets, 4 SVG illustrations, Maker Badges tie-ins).
- [x] **Supporters & Friends page** — partner logos de-greened, logo wall
      with org names; /shelf → /theshelf; System Upgrade rework.
- [x] **Ben: heritage page on WordPress** — live and verified.

## Domain cutover checklist (target: by Sept 1, HostPresto renewal Sept 7)

- [ ] Videos re-hosted (see "last missing video" above)
- [ ] Old-site links resolved: any remaining steamhead.space/wp-content
      references (certification pages done: /design-immersion-overview/ and
      /maker-badges/ are live top-level pages — the overview URL is cited in
      academic papers and must never move)
- [ ] **Launches from Earth (PR #18, live under Neighborhood Earth)**:
      confirm the live Launch Library API call and its CORS behavior work
      from the real `steamhead.space` origin, not just the
      `*.workers.dev` preview/production Worker URL — flip to the bundled
      snapshot fallback if the API rejects the custom domain. Verify the
      "View on GitHub" link resolves to `github.com/SteamHead/earth-launches`
      (repo now transferred from boomtown001) and that the
      `/images/2024/04/neighborhoodearth.jpg` card image renders.
- [ ] Add steamhead.space zone to James's Cloudflare account; attach custom
      domain to the Worker
- [ ] Update GitHub OAuth app homepage URL
- [ ] Final WordPress export archived in Drive; decline HostPresto renewal
- [ ] Repo public flip (secrets scan already clean) — optional, any time
