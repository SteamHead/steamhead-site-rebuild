# Site TODO

Requests captured during review — not part of the blog migration. Design
discussions happen before implementing where noted.

## Header / footer

- [ ] **Add Blog link to header and footer nav** — /blog/ is currently only
      reachable by direct URL. (Blake, 2026-07-10)
- [ ] **Collapse the three program links into a "Programs" dropdown** —
      MakeFashion Edu, Neighborhood Earth, and System Upgrade make the
      header too long, and Blog/People links are coming. (Blake, 2026-07-10)
- [ ] **Use the SteamHead logo graphic instead of the text "SteamHead"** in
      the header. Get the proper mark from `reference/SteamHead Brand
      Guide.pdf` (a clean SVG/PNG, not the old JPEG in
      `public/images/2018/08/`). (Blake, 2026-07-10)
- [ ] **Add media kit link to the footer** — old URL is
      `https://steamhead.space/media_kit/`. Note: that's a WordPress *page*;
      at domain cutover the media kit needs a new home on this site (or its
      own redirect). Until then the footer link can point at the old URL.
      (Blake, 2026-07-10)

## Content

- [ ] **Alt text for all images** — migrated post images currently reuse the
      post title as alt text; real descriptive alt text should be generated
      (AI-assisted pass over ~300 images) or hand-written for the important
      ones. Accessibility item from the evaluation's week-6 pass.
      (Blake, 2026-07-11)

## Bugs

- [ ] **Favicon not showing** — `public/favicon.svg` exists; check that
      BaseLayout.astro emits the `<link rel="icon">` tag and that the SVG
      isn't a placeholder. Consider deriving it from the real logo.
      (Blake, 2026-07-10)
