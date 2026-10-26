# Blog review: remove, highlight, timeline

Reviewed 2026-10-26 against `src/content/blog/`. That folder is the source of
https://steamhead.space/blog/, which lists every post where `draft` is not set.
**152 files: 141 published, 11 drafts.** Nothing has been deleted or changed
yet. This document is a set of recommendations for a person to decide on.

Legend: **Remove** = delete the file. **Merge** = fold into another post or page,
then delete the file and add a `_redirects` rule. **Archive** = keep it, but stop
linking it from anywhere prominent. Every post URL is `/blog/<slug>/`.

> Before deleting a published post, add a 301 in `public/_redirects` pointing to
> the closest surviving page. Old links from WordPress and Wix still arrive.

---

## 1. Candidates to remove or consolidate

### 1a. Unpublished drafts (11). Safe to remove

None of these appear on the live site. They are leftover clutter from the
WordPress export.

| Slug | Why |
|------|-----|
| `snow-drop-jane` | Empty (0 words) |
| `a-maker-teachers-perspective-on-disability` | Empty (0 words) |
| `snow-drop-with-microblocks` | Superseded by the published `snow-drop-grade-2-robotics-and-coding`. Body is mostly pasted WordPress CSS |
| `snow-drop-with-microblocks-2` | Same as above, a second copy |
| `new-video-upload-makefashion-edu-tucson-2020-highlights` | Covered by the published `make-fashion-edu-tucson-2020-student-production-video`. Could be folded into it if the highlights video is wanted |
| `dream-dream-dream` | Student outfit write-up that was never published. Keep only if it gets a home in the MFEdu showcase (see 1d) |
| `lets-connect-steamheads-lightning-node-2` | Lightning node invitation. Verify the node still exists; most likely it doesn't |
| `freier-and-brunner-chatgpt-summaries` | Raw ChatGPT output |
| `navigating-tech-education-teachers-as-guides-not-tech-gurus` | Unfinished. Could be completed and published as a new post |
| `differentiating-depth-vs-breadth` | Unfinished reading response. Same option as above |
| `model-imf-club` | Unfinished idea. Same option as above |

### 1b. Duplicates. Merge, keep one

| Remove | Keep | Notes |
|--------|------|-------|
| `dragon-heart-daniel-zeng-shenzhen-makefashion-edu-2018` | `dragon-heart` | Identical text |
| `friendship-team-moralture-shezhen-makefashion-edu-2018` | `friendship_dress` | Same outfit and same description ("Shezhen" is also misspelled) |
| `makefashion-tucson-behind-the-scenes-documentary` | `mfedu-az-docu` | Both cover the 2019 Tucson documentary |
| `badge-levels` (25 words, one Sheets link) | `badge-levels-2` | Better still, merge both with `what-are-open-badges` and `maker-badges` into the `/maker-badges/` page, which already exists |
| `shenzhen-2019-runway-highlights-makefashion-edu` | `shenzhen-2019-runway-full` | Optional. Put both videos in one post |

### 1c. Outdated or no longer in use (links and offers that are dead)

| Slug | Why it's stale | Suggestion |
|------|----------------|------------|
| `steamhead-community-taobao` | Taobao shop and student-product listing process from the Shenzhen era | Remove |
| `taobaolist` | OneDrive purchase list, "WeChat me" instructions | Remove |
| `steamhead-s-resident-room` | Airbnb listing and OneDrive guidelines for the Shekou room (38 words) | Remove, or merge into a residency history page |
| `steamhead-education-services` | 2017 "Maker Ed Empower / PBL Connect" service offer | Archive. Not a current offer |
| `led-bling`, `make-it-move`, `vr-architects` | 2017 Shekou course listings, read like current sign-ups | Archive. Could merge into one "2017 workshop catalogue" post |
| `desert-trip` (48 words) | One-paragraph annual trip note | Merge into `blue-house-hub` |
| `steamhead-courses-in-learnworlds` | Says courses live on "The Shelf". Courses are now at `/courses/` | Remove and redirect to `/courses/mfedu-2026/`, or update the text |
| `whats-new-in-steamhead-space` | Announces the 2021 site redesign, which this rebuild replaced | Archive (history), or remove |
| `makefashion-edu-website-gets-a-fresh-update` | 2021 MFEdu site refresh | Archive. Verify the external site still exists, and remove if it doesn't |
| `school-maker-faire` | 2019 "one week left to sign up" call for makers | Remove. `steamhead-at-the-4th-nanshan-school-maker-faire` is the better record |
| `htta-hacker-trip-through-asia-great-events` | 2019 announcement. `conclusion-of-the-eight-week-htta-tour` covers the outcome | Merge into the conclusion post |
| `maker-convening` | Event-day post for 3 Oct 2020 with a Discord invite | Verify the Discord is alive. Otherwise remove the invite and keep the talk video |
| `bailey-hu-at-technode-features-maker-ed` | Fine, but check that the TechNode link still resolves | Keep if the link works |

### 1d. Thin posts (under ~60 words, or just a video or link)

These add little as individual posts. Most of the MFEdu ones are worth keeping
as **content**, but they'd work better as a single *MakeFashion Edu runway and
video gallery* page under `/makefashion-edu/` than as separate blog entries.

| Slug | Words | Suggestion |
|------|------:|------------|
| `calgary-robots-are-fun-beauty-beneath` | 1 | Bare YouTube link. Merge into the gallery |
| `makefashion-edu-led-diffusion-for-wearables` | 1 | Tutorial video. Merge into gallery or guides |
| `virtual-maker-exhibition-steamhead-teacher-tour` | 1 | Merge both VME posts into one post with context |
| `virtual-maker-exhibition-how-to-start-educator-guide-part-1` | 1 | As above |
| `18-things-every-beginning-woodworker-should-know` | 25 | Third-party video, no SteamHead content. **Remove** |
| `7-ways-the-iste` | 304 | Third-party ISTE video plus standards text. **Remove** |
| `home-automation-project` | 25 | Bilibili embed. Merge into a Hardi / makerspace projects round-up |
| `student-stories-spring-formal` | 27 | Merge into gallery |
| `how-to-makefashion-fuse-plastic-bags-to-create-fabric` | 40 | Merge into gallery or guides |
| `how-to-makefashion-3-ways-to-attach-flexi-bits-to-a-wearable` | 44 | As above |
| `makefashion-edu-at-glow-spectrum` | 40 | Merge into gallery |
| `helens-community-meetups-2` | 42 | Merge into the `helen-steer` people profile |
| `how-to-walk` | 59 | Merge into gallery or guides |
| `thats-a-wrap` | 71 | Photos only. Keep it, but add a sentence on *where and when* the first show happened |
| `3d-printer-revived`, `nfc-powered-lights`, `ar-sandbox-linux-setup` | 65–86 | 2019 makerspace micro-updates. Merge into one "SteamHead Shekou makerspace, autumn 2019" post |
| `visiting-sticker-factory-in-shenzhen-great-things`, `the-htta-2019-residency`, `steamhead-tour-of-m5-2`, `qiu-and-paul-tour-the-x-factory-maker-space-3`, `soldering-led-boards-3` | 65–129 | Paul's 2019 residency in five fragments. Merge into one residency post |
| `opcb` | 147 | Personal note. Archive or remove |

### 1e. Keep, but needs a policy or quality check (not removal)

- **AI-written posts without disclosure in the title.** `student-groupwork`
  says "(ai generated)" in its title, and the three Carrie posts from January 2023
  (`online-events-together-while-apart`, `donations-critical-contributions`,
  `donations-material-matters`) open with "Written by ChatGPT, Prompt/Edit by
  Carrie". That is disclosed, which is good. `chatgpt4-please-eli5-...` is fine
  as an explicit AI experiment. No action needed beyond keeping the disclosures.
- **Photos of identifiable students** (the MFEdu outfit posts and the school visits)
  stay all rights reserved per `LICENSE-MEDIA`. Before reusing any of these in
  other documents or grant reports, get permission (james@steamhead.space).
- `the-impact-of-organization-classroom-seating` and
  `seating-arrangements-for-students-with-disabilities` overlap. Consider
  cross-linking them.

**Net effect if everything above is adopted:** about 11 drafts and 12–15 published
posts deleted, and about 25 thin posts folded into 4–5 consolidated pages. The
blog drops from 141 listed posts to roughly 100, and every one that remains has
real content.

---

## 2. Posts to highlight

These best show what SteamHead is and does. Use them for a "Featured" strip on
`/blog/`, for program pages, funder reports and the media kit.

### Origin and identity
- `themake-club-becomes-steamhead`: the founding story (theMake.club → SteamHead, Shenzhen + San Francisco)
- `themake-club-gets-its-name`: the 2014 founding moment
- `innovation-is-a-skill`: the tagline that still defines SteamHead
- `james-maker-ed-milestones`: James's path, from 2011 to SteamHead
- `goodbye-wix-hello-wordpress`: the Shekou makerspace era in one post

### MakeFashion Edu (flagship program)
- `thats-a-wrap` → `tucson-makefashion-edu` → `shenzhen-2019-runway-full`: first shows and growth across countries
- `mfedu-az-docu`: behind-the-scenes documentary, Tucson 2019
- `fashion-tech-teaching-plan`: the 6-step design model (d.school-based)
- `see-it-in-action-fashion-elements`: Carrie's online course for teachers
- `makefashion-edus-metacognition`: the pedagogy behind the program
- `makefashion-edu-paper-dresses`: low-cost, accessible materials
- `maker-camp-live-light-up-dino-spikes-class`: partnership with Make Media
- `epipen-project`: a university student's advocacy-driven wearable
- `digital-literacy-accelerator`: **accepted to a US Department of Education–supported accelerator (2021)**, the strongest credibility post on the blog
- `deeper-learning-conference`: national conference presentation (2021)

### Curriculum and educator resources
- `design-immersion-curriculum`: the SteamHead Design Immersion Curriculum (1,800 words, multi-author); pairs with `/design-immersion-overview/`
- `what-are-open-badges` and `badge-levels-2`: the Maker Badges system
- `mentoring-in-a-pandemic`: remote tech-integration support, 2020
- `new-resource-for-remote-teachers-learn-camera-techniques-and-obs`: practical help for remote teaching
- `snow-drop-grade-2-robotics-and-coding`: **best recent classroom story (2026)**: MicroBlocks, micro:bit, OctoStudio and cross-grade mentorship
- The JamesEd essay series (2020 to 2023) is a coherent body of educator writing. Best entry points: `classroom-management-in-i-b-and-pbl-settings`, `creating-rules-procedures-with-students`, `progressivism-in-my-classroom`, `curriculum_empathy`, `international-baccalaureate-idu`

### SteamBeans (financial literacy and systems thinking)
- `monetary-policy-ledgers-in-a-classroom` → `nano-classroom-economy` → `nano-classroom-economy-in-a-makerspace` → `quadratic-voting-in-the-classroom` → `field-trip-quadratic-voting`: a distinctive and fairly unusual strand, worth packaging as a series
- `desert-solar-journey`: energy independence as systems thinking

### Community, events and people
- `themake-club-maker-faire-2015` and `steamhead-at-the-4th-nanshan-school-maker-faire`: maker faires in Shenzhen
- `ein`: the bilingual Educators Meetup (community partner)
- `hello-hello-shenzhen`: British Council residency (Helen Steer)
- `conclusion-of-the-eight-week-htta-tour`: Hackers Tour Through Asia
- `xian-ed`: Diane Kern Hamilton on the Xi'an maker scene
- `in-depth-look-at-our-3d-printing-class-at-dongwan-elementary`: local public-school partnership
- `chicago`: Christy Wang's mask-making during COVID
- `avery-kuo`: student advocacy profile
- `getting-to-know-the-steamhead-team-carrie-leung` and `...-twila-busby`: team profiles
- `donations-critical-contributions` and `donations-material-matters`: how SteamHead runs on donated time and materials (useful for funders)
- `learning-happens-everywhere-if-we-let-it`: the 2026 return to blogging (FabLab Bangkok and informal learning)

---

## 3. Timeline and year-by-year summary

Counts are **published** posts per year.

| Year | Posts | Summary |
|------|------:|---------|
| **2014** | 1 | **theMake.club founded** (11 June) by Ben (James) Simpson and Carrie Leung, after both worked in San Francisco tech before moving to Shenzhen. |
| **2015** | 4 | theMake.club exhibits at **Shenzhen Maker Faire** (10 student presentation spaces, June). It starts teaching at **Litchee Lab**, Shenzhen High Tech Park. Tagline: *"Innovation is a skill. Start practicing."* |
| **2016** | 2 | Club skills framework published (ages 9 to 16+). **theMake.club becomes SteamHead** (February). |
| **2017** | 11 | **Shekou makerspace** on Wix: resident room, kids' workshops (LED Bling, Make it Move, VR Architects), school services, **Maker Badges** released on GitHub. **Blue House Hub** in the Mojave Desert. Community partner of the **EIN** educators meetup. Hosts the British Council *Hello Shenzhen* resident (Helen Steer). |
| **2018** | 16 | Moves to WordPress. **MakeFashion Edu launches**: Shenzhen student outfits (Guitar of Light, Razor Wings, Friendship Dress, Quinceañera). Presents at **EdTech Guangzhou**. 3D-printing partnership with **Dongwan Elementary**/Moralture. Featured in **TechNode**. Organises the **4th Nanshan School Maker Faire** (Nov). Classroom economy and blockchain teaching begin. |
| **2019** | 45 | **Peak year.** MakeFashion Edu's first show wraps (Jan). The program reaches **Tucson, AZ** (Feb, documentary by Michael Shaw) and the **second Shenzhen runway** (May, Design Society, fourth show overall). Residencies: Michelle (indoor farm), Felix Klee, Paul and Qiu. **HTTA: Hackers Tour Through Asia** (Mar to May). Teen Tech Week in California. Nanshan School Maker Faire again. AR Sandbox for a K-12 school. Xi'an report. |
| **2020** | 26 | **Pandemic pivot.** Remote tech-integration support. MFEdu Tucson 2020 runway (Feb, Dunbar Pavilion). **Maker Camp Live** with Make Media. **MakerEd Maker Convening** talk ("Advocacy Through Tech"). Teacher video and OBS resources. Large JamesEd essay series on IB, PBL, classroom management and educational philosophy. **Nano classroom economy** (SteamBeans). Christy Wang's mask-making. |
| **2021** | 18 | **Design Immersion Curriculum** published. **Virtual Maker Exhibition**. **Deeper Learning** conference session. **US Dept. of Education–supported Digital Learning Accelerator** (Nov). Quadratic voting in class. New steamhead.space and MFEdu websites (Oct/Nov). Team profiles (Carrie, Twila). |
| **2022** | 3 | Courses move onto steamhead.space ("The Shelf"). Quadratic-voting field trip. Brilliant.org review. *Quiet year.* |
| **2023** | 12 | Donations and online-events retrospectives (AI-assisted, disclosed). **Desert Solar Journey**. LiDAR scan at Fuse33. IB interdisciplinary units. Disability-inclusion pieces (seating, dyscalculia). Early ChatGPT experiments in teacher learning. MFEdu metacognition essay (July). *Blog then goes silent.* |
| **2024** | 0 | *No posts.* (A gap to explain or fill in other documents.) |
| **2025** | 0 | *No published posts.* (The WordPress export has a Jan 2025 "MG Space Cardboard Engineering Semester Course" post that was not migrated. See `blog-post-inventory.md`.) |
| **2026** | 3 | **Site rebuilt** on Astro (Great Things Blog relaunched, May). *Learning Happens Everywhere* (FabLab Bangkok). **Snow Drop!** Grade 2 robotics with MicroBlocks/OctoStudio. theMake.club and Wix archives restored into the blog. **"Advocacy by Design"** MFEdu course rewrite at `/courses/mfedu-2026/`. |

### Program milestones (short form, for other documents)

- **2014**: theMake.club founded (Shenzhen / San Francisco)
- **2016**: renamed SteamHead
- **2017**: Shekou makerspace, Maker Badges, Mojave Blue House Hub
- **2018**: MakeFashion Edu launched in Shenzhen
- **2019**: MakeFashion Edu reaches the US (Tucson); HTTA tour; busiest year (45 posts)
- **2020**: remote pivot; Make Media Maker Camp Live; MakerEd Convening
- **2021**: Design Immersion Curriculum; US Dept. of Ed–supported Digital Learning Accelerator; Deeper Learning
- **2023**: SteamBeans solar and economy work; inclusion writing
- **2024–25**: quiet period
- **2026**: new site, MFEdu 2026 course, return to classroom stories

### Gaps worth noting for future documents

- **2022 and 2024–25 are thin or empty.** If other documents (grants, annual
  reports) cover those years, the blog doesn't support them. Consider writing
  posts for them (MG Space cardboard course in 2025, Neighborhood Earth / Launches
  from Earth, System Upgrade).
- **Neighborhood Earth** and **System Upgrade** have almost no blog presence:
  one post is tagged `neighborhood-earth` and none `system-upgrade`, despite
  both having program pages.
- Program tagging is uneven: 44 posts are `makefashion-edu`, almost everything
  else is `general`, and `welcome-to-great-things` has no program at all.
  Re-tagging the SteamBeans and makerspace posts would make the future program
  filters useful.
