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
how_body: >
  The globe is a single self-contained web page — no build step, no
  external libraries. Launch data is pulled live from a public spaceflight
  API (The Space Devs' Launch Library), matched to launch-site coordinates,
  and drawn onto a hand-built 2D projection of Earth. If the live feed is
  unreachable, the page falls back to a bundled snapshot so it's never
  blank. Selecting a site opens a detail card with the mission, vehicle,
  and provider.
classroom_body: >
  A teacher could build lessons around geography and time zones, orbital
  launch locations, engineering constraints, international cooperation and
  competition, launch frequency and patterns, data reliability, interface
  design, environmental effects, and the economics of spaceflight.
limitations_body: >
  Launch dates are often precise only to the month or quarter, and change
  frequently — the countdown reflects that uncertainty rather than hiding
  it. The live feed depends on a third-party API with its own rate limits
  and occasional downtime, which is why a static snapshot ships as a
  backstop (and why that snapshot will drift out of date over time).
  Mission details are only as complete as what launch providers choose to
  publish.
github_url: https://github.com/SteamHead/launches-from-earth
---

Launches from Earth is an interactive globe that lets people explore upcoming space launches around the world. Visitors can watch live countdowns, locate launch sites, and select individual spaceports to learn more about the missions beginning there.
