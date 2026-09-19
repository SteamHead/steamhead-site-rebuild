---
hero_tagline: >
  Explore upcoming space launches through an interactive globe, live
  countdowns, and launch-site stories.
guiding_question: >
  What can worldwide space launches teach us about how Earth is connected?
why_body: >
  Space launches are often presented as isolated events: a rocket, a
  company, a nation, or a dramatic countdown. Viewed together on a globe,
  they tell a larger story. They reveal patterns of geography, engineering,
  infrastructure, international collaboration, economics, and access to
  space.


  Launches from Earth was created as part of Neighborhood Earth, a
  SteamHead initiative that helps learners investigate the technologies,
  systems, places, and people connecting our planet.
learn_intro: >
  Launches from Earth is both a public exploration tool and an open-source
  learning project. Students, educators, developers, and curious visitors
  can use it to investigate questions such as:
learn_questions:
  - Why are launch sites located where they are?
  - How do geography and Earth's rotation affect launches?
  - Which countries and organizations are launching into space?
  - How accurate are launch schedules and public datasets?
  - What can launch activity tell us about our changing relationship with space?
how_heading: >
  The globe is arithmetic, not 3D
how_body: >
  No 3D engine and no graphics library. Every frame, the page works out
  where each coastline point and every launch pad falls on a circle,
  throws away everything on the far side of the planet, and draws what is
  left. The globe you just turned is trigonometry and a drop shadow.


  It also rebuilds itself. Once a day a small program fetches the latest
  schedule, rewrites this page's data, checks the result still runs, and
  publishes it with nobody watching.
classroom_body: >
  A teacher could build lessons around geography and time zones, orbital
  launch locations, engineering constraints, international cooperation and
  competition, launch frequency and patterns, data reliability, interface
  design, environmental effects, and the economics of spaceflight.
limitations_body: >
  The bundled fallback snapshot is rebuilt every day by an automated job
  from The Space Devs' Launch Library, so it should never be more than
  about 24 hours behind — and the page tries the live feed first anyway,
  with a Refresh button for the gap between the two. Launch dates are
  often precise only to the month or quarter and change frequently; the
  countdown and the card's confidence line reflect that uncertainty rather
  than hiding it. Mission details are only as complete as what launch
  providers choose to publish, so some fields read "TBD" or "not
  disclosed".
github_url: https://github.com/SteamHead/earth-launches
---

Launches from Earth is an interactive globe that lets people explore upcoming space launches around the world. Visitors can watch live countdowns, locate launch sites, and select individual spaceports to learn more about the missions beginning there.
