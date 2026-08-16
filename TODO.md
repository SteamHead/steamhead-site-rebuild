# Site TODO

Working list, kept current by Blake's Claude sessions. GitHub issues mirror
the items teammates need visibility on.

## Waiting on Blake

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

- [x] **Earth-launches transferred to the SteamHead org** — was
      `boomtown001/earth-launches`, now `SteamHead/earth-launches`. PR #18
      added its project page under Neighborhood Earth and merged.
- [x] **Worker renamed to `steamhead`** and manually deployed/verified live
      at `steamhead.james-068.workers.dev` — see "Deploy path" in CLAUDE.md
      for the auto-deploy gap this created (not yet fixed).
- [x] **MG Space Cardboard Engineering post removed** — its recap video
      (bilingual-subtitle .mov) was already gone from the dead WordPress
      server with no other source found, so the post was cut rather than
      published with a dead video. Redirect for its old permalink removed
      from `public/_redirects` too.
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

**Status as of 2026-08-09**: Blake emailed HostPresto to change
`steamhead.space`'s nameservers to Cloudflare's (`addilyn.ns.cloudflare.com`
/ `lars.ns.cloudflare.com`) — the Cloudflare zone already exists and is
`status: pending`, waiting on that. Expect at least a day for the email to
be processed and DNS to propagate; live nameservers were still HostPresto's
(`ns[1-4].hpdns.net`) as of this check. Full WordPress backup (see "New
machine setup" above) is done, so it's safe to proceed once DNS clears.
Next concrete steps, in order:

1. Re-check nameservers (`dig NS steamhead.space`) / the Cloudflare zone
   status until it flips to `active`.
2. Workers & Pages → `steamhead` → Settings → Domains & Routes → Add Custom
   Domain → `steamhead.space` (and `www.steamhead.space`). This was tried
   on 2026-08-08 while still pending and Cloudflare showed
   "steamhead.space (pending)" — expected, not stuck; retry once the zone
   is active. (Not doable via the API token in use — it's Workers-scoped
   only, no Zone/DNS permission, and Claude Code's own safety classifier
   blocks any `workers/domains` API call outright, read or write — this
   step needs a human in the dashboard.)
3. Verify the live site on the real domain: homepage, blog, a person page,
   `/neighborhood-earth/launches-from-earth/`, `/admin/` CMS login.
4. Update the GitHub OAuth app's Homepage URL (Developer Settings → OAuth
   Apps) to `https://steamhead.space`.
5. Only after 3 and 4 check out: decline the HostPresto renewal (due
   Sept 7).
6. Once `steamhead` is confirmed solid: delete the old
   `steamhead-astro-scaffold` Worker (see "Deploy path" above — it's still
   the one auto-deploying on every push right now, `steamhead` is not).

MX record check: Cloudflare's initial zone scan already copied the existing
Google Workspace MX/SPF records over automatically — confirmed fine,
no manual re-entry needed.

- [ ] **Videos re-hosted** — three 2021 clips + the 96MB `output2.mp4`
      (Snow Drop post) still point at dead `steamhead.space/wp-content/...`
      URLs. Should be recoverable from the 2026-08-08 UpdraftPlus backup
      (see memory) rather than re-sourced externally — check "shmac" /
      OneDrive for the originals, then upload to YouTube/Drive and
      re-point the posts.
- [x] Old-site links resolved: 13 dead `?attachment_id=` links and 15
      images hotlinked via WordPress's Jetpack Photon CDN
      (`i0.wp.com`/`i2.wp.com`) fixed — all pointed at images already
      mirrored locally under `public/images/`. Citation links to
      `steamhead.space/design-immersion-overview/` are intentional (cited
      in academic papers, must never move) and left alone. `/shop/` and
      `/support-us/` resolved: `/shop/`'s purpose is fully replicated by
      `/theshelf/` itself (confirmed by Blake) — `theshelf.astro`'s book
      fallback link now points at the existing Amazon collection link
      instead; `/support-us/` was an unused template (the `support_url`
      field was never referenced anywhere in the site code) — deleted
      from `settings/general.md`. "SHTEAM Labs 1" **Get It** button now
      points at its real Canva share link (confirmed by Blake).
- [ ] **Launches from Earth (PR #18, live under Neighborhood Earth)**:
      confirm the live Launch Library API call and its CORS behavior work
      from the real `steamhead.space` origin, not just the
      `*.workers.dev` preview/production Worker URL — flip to the bundled
      snapshot fallback if the API rejects the custom domain. Verify the
      "View on GitHub" link resolves to `github.com/SteamHead/earth-launches`
      (repo now transferred from boomtown001) and that the
      `/images/2024/04/neighborhoodearth.jpg` card image renders.
- [x] `steamhead.space` zone added to James's Cloudflare account (status:
      pending as of 2026-08-09, awaiting nameserver propagation) — see
      status block above for the custom-domain-attachment follow-up.
- [ ] Update GitHub OAuth app homepage URL
- [ ] Final WordPress export archived in Drive; decline HostPresto renewal
- [x] **Set up git-connected Workers Build for `steamhead`** — done
      2026-08-15. Pushes to `main` now auto-deploy the live site.
- [x] **Deleted `steamhead-astro-scaffold`** — 2026-08-15. It held no domain
      or route and took the misdirected build pipeline with it.
- [ ] Repo public flip (secrets scan already clean) — optional, any time
