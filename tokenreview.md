# The Mapet Token Review — What & How

## What it is

A design QA session made cheap by the design-token system. Every color, font,
text size, spacing step, and shadow on steamhead.space flows from ~25 CSS
variables at the top of `src/styles/global.css`. That means a designer's
feedback becomes one-line edits that restyle the entire site at once, instead
of page-by-page fixes.

Mapet looks at the live site next to the brand guide and judges whether the
site *feels* like the brand — are the yellows right, is the type hierarchy
working, do the buttons read as SteamHead. Anything she wants changed maps to
a token: "headings feel small" → bump `--text-3xl`; "that teal button is
washed out" → change `--color-cta-bg`; "everything feels cramped" → adjust
the `--space-*` scale.

## How to conduct it

1. **Prep** — send Mapet the live site plus the brand guide PDF
   (`/downloads/2021_SteamHead_Brand_Guide.pdf`, linked on the Media Kit
   page). No other setup needed.

2. **Walk 5–6 representative pages together** (~30–45 min): the homepage,
   `/about-us/` (people grids), a blog post, `/makefashion-edu/` (dark
   scattered hero), `/theshelf/`, and `/maker-badges/`. Those cover every
   visual pattern the site has — light/dark sections, cards, buttons, grids,
   galleries.

3. **Let her speak in design language, not CSS.** Capture feedback as plain
   notes ("the yellow headings on white are hard to read", "buttons should
   be rounder"). Don't translate live.

4. **Ask her the banked open questions:**
   - The **badge-pathway pill colors** on `/maker-badges/` — five hues
     intentionally outside the brand palette so the pathways stay
     distinguishable. Bless or redesign?
   - The **contrast fixes** from the token pass (muted labels darkened
     `#888`→`#666`, footer copyright brightened `#555`→`#aaa`). Do they look
     right to her eye?
   - The **people cards** and the yellow "Read profile" indicator on
     `/about-us/` — pages vs. popups was her design call, so she should see
     how it landed.

5. **Hand the notes to a Claude session.** They get translated into token
   edits (plus normal page edits for anything tokens can't reach), shipped
   as one PR with a branch-preview link. Mapet does a second look on the
   preview before merge.

## The boundary

Tokens control the *system* — colors, type, and spacing everywhere. They
don't control *layouts* (how the MFEdu hero is composed, which photo the
About page uses). Mapet can flag layout things too; they just become
per-page edits in the same PR rather than token changes.

Practically: one screen-share, a list of notes, one session to land it all.
