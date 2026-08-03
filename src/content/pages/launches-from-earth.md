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
  external libraries — traced from real Natural Earth coastline geometry
  and drawn with the 2D Canvas API. It spins once every 200 seconds on its
  own; drag or swipe to spin it yourself, and it resumes on its own after a
  few seconds. Every spaceport gets a pin — green for scheduled, pulsing
  red for inside 24 hours, hollow for nothing booked — and tapping one
  opens a detail card with mission, vehicle, provider, destination orbit,
  liftoff converted to your own local time, and a confidence line stating
  plainly whether the date is a published target, a NET window, or an
  estimate. On load it tries a live spaceflight API (The Space Devs'
  Launch Library) and falls back to a bundled snapshot if that's
  unreachable, so the page is never blank.
classroom_body: >
  A teacher could build lessons around geography and time zones, orbital
  launch locations, engineering constraints, international cooperation and
  competition, launch frequency and patterns, data reliability, interface
  design, environmental effects, and the economics of spaceflight.
limitations_body: >
  The bundled fallback snapshot was hand-built from nextspaceflight.com and
  rocketlaunch.org on 3 August 2026, covering 30 spaceports and 29 missions
  through mid-September, plus labelled estimates for Starship, Neutron, and
  other quiet pads — it will drift out of date, which is exactly why the
  live feed matters and why the page always tries that first. Launch dates
  are often precise only to the month or quarter, and change frequently —
  the countdown and the card's confidence line reflect that uncertainty
  rather than hiding it. Mission details are only as complete as what
  launch providers choose to publish.
github_url: https://github.com/SteamHead/launches-from-earth
---

Launches from Earth is an interactive globe that lets people explore upcoming space launches around the world. Visitors can watch live countdowns, locate launch sites, and select individual spaceports to learn more about the missions beginning there.
