---
title: "Snow Drop with MicroBlocks!"
date: 2026-03-01
description: "Using MicroBlocks + OctoStudio for a Grade 2 Winter Performance -- /\\ Minimal styling so it looks clean anywhere (Divi/WP-friendly) \\/ -- .post-wrap { max-width: 820px; margin: 0…"
author: "James"
program: general
categories:
  - "Uncategorized"
draft: true
---

Using MicroBlocks + OctoStudio for a Grade 2 Winter Performance <!-- <br> --> /\* Minimal styling so it looks clean anywhere (Divi/WP-friendly) \*/<!-- <br> --> .post-wrap { max-width: 820px; margin: 0 auto; padding: 0 16px; }<!-- <br> --> .lede { font-size: 1.1rem; line-height: 1.55; }<!-- <br> --> hr { border: 0; border-top: 1px solid rgba(0,0,0,0.12); margin: 2rem 0; }<!-- <br> --> figure { margin: 1.25rem 0; }<!-- <br> --> img, video { max-width: 100%; height: auto; display: block; }<!-- <br> --> figcaption { font-size: 0.95rem; opacity: 0.8; margin-top: 0.5rem; }<!-- <br> --> ul { margin-top: 0.5rem; }<!-- <br> --> h1 { line-height: 1.2; margin: 0 0 0.75rem; }<!-- <br> --> h2 { margin: 0 0 0.75rem; }<!-- <br> --> h3 { margin: 1.25rem 0 0.5rem; }<!-- <br> --> .callout { padding: 0.9rem 1rem; border-left: 3px solid rgba(0,0,0,0.25); margin: 1.25rem 0; }<!-- <br> --> .two-col { display: grid; grid-template-columns: 1fr; gap: 18px; }<!-- <br> --> @media (min-width: 760px) { .two-col { grid-template-columns: 1fr 1fr; } }<!-- <br> --> .small { font-size: 0.95rem; opacity: 0.9; }<!-- <br> --> a { word-break: break-word; }<!-- <br> -->

## Using MicroBlocks + OctoStudio for a Grade 2 Winter Performance

At our elementary school winter festival, something unexpected happened.

**Paper snow fell from the ceiling.**

**And the Grade 2 students were controlling it.**

This project brought together collaboration, authentic audience, cross-grade mentorship, creative coding, and physical computing — and it shows a powerful pathway for educators exploring MicroBlocks.

* * *

## Video

  Your browser does not support the video tag.

_Students triggering paper snow during our winter performance._

* * *

## The Big Idea

**Grade 2 students:**

-   Built cardboard “snow release” boxes
-   Created paper snow
-   Programmed an iPad app in OctoStudio
-   Triggered a live robotics effect during a school performance

**Behind the scenes:**

-   Fifth graders wired servo motors to micro:bits
-   I wrote the MicroBlocks program that ran on the micro:bits
-   The Grade 2 classroom teacher orchestrated rehearsal, context, and performance flow

**The result?**  
A gymnasium full of students cheering as snow dropped on cue — triggered by second graders.

* * *

## Hardware + Software Overview

-   **Student-facing tool:** OctoStudio (iPad app)
-   **Microcontroller:** micro:bit
-   **Firmware:** MicroBlocks
-   **Actuation:** Servo motors connected to trap doors
-   **Trigger method:** OctoStudio “beam” signal received by MicroBlocks

The servo motors were mounted to bottom-facing doors on cardboard boxes suspended in the auditorium. When activated, the doors opened and released paper snow.

![OctoStudio code screenshot showing beam trigger](https://i0.wp.com/steamhead.space/images/2026/03/IMG_9878.png)

OctoStudio beam trigger code (single sprite shown; replicated across others).

* * *

## MicroBlocks Receiver Code

The micro:bit ran a MicroBlocks program that:

-   Listened for a specific beam ID
-   Rotated the servo to open the trap door
-   Returned the servo to closed position

![MicroBlocks code screenshot showing micro:bit receiving beam and actuating servo](https://i0.wp.com/steamhead.space/images/2026/03/microblocks_octo.png)

MicroBlocks receiver code running on micro:bit.

Uploading directly via MicroBlocks made iteration fast — especially useful during rehearsal testing.

* * *

## Fifth Grade Contribution

Fifth graders handled:

-   Servo wiring
-   Power connections
-   Mechanical mounting adjustments

This cross-grade collaboration gave older students meaningful technical responsibility and gave younger students a visible “tech mentor” layer.

* * *

## The Physical Build

The snow boxes were simple but effective:

-   Cardboard structure
-   Bottom flap door
-   Servo arm connected to the door
-   Suspended in the auditorium

![Cardboard snow dropper box suspended, view 1](https://i0.wp.com/steamhead.space/images/2026/03/snow1.png)

Snow dropper box (view 1).

![Cardboard snow dropper box suspended, view 2](https://i0.wp.com/steamhead.space/images/2026/03/snow2.png)

Snow dropper box (view 2).

The engineering constraint was real: if the servo didn’t move correctly, nothing happened.

* * *

## Why This Pathway Is Interesting

Many educators use OctoStudio.  
Many educators use micro:bit.  
Fewer combine them in this way.

**MicroBlocks becomes the bridge.**

OctoStudio → Beam → MicroBlocks → micro:bit → Servo → Physical Action

This implementation builds on work shared by Wenjie, extending OctoStudio beam support for micro:bit:

-   [https://wiki.microblocks.fun/en/octostudio/maqueen\_lite](https://wiki.microblocks.fun/en/octostudio/maqueen_lite)
-   [https://wwj718-github-io.translate.goog/post/编程/extend-octostudio/](https://wwj718-github-io.translate.goog/post/编程/extend-octostudio/)

I first learned about MicroBlocks from Kathy Giori at the Bay Area Maker Faire (Mare Island, 2024), and this project became the perfect live test of its flexibility.

* * *

## Authentic Assessment: Did It Work?

This project shifted assessment away from a rubric.

**Success was measured in real time:** Was the audience entertained?

When the snow dropped, the cheering was immediate and loud. Students saw directly that code + cardboard + motors = real-world impact.

It wasn’t a simulation.  
It wasn’t just a classroom demo.  
It was part of a public performance.

* * *

## Why This Matters Pedagogically

### 1\. Robotics Through Familiar Tools

OctoStudio is accessible and playful. MicroBlocks extends that environment into physical computing without abandoning block-based thinking.

### 2\. Real Audience > Teacher Assessment

When projects leave the classroom, reliability matters. Iteration becomes meaningful. Debugging becomes urgent.

### 3\. Cross-Grade Systems Thinking

Grade 2: design + coding  
Grade 5: wiring + electronics  
Teacher: system integration

Students experienced how complex systems require multiple roles — coding, hardware, mechanical design, and rehearsal timing.

* * *

## If You Want to Try Something Similar

Start small:

-   One micro:bit
-   One servo
-   One beam trigger
-   One cardboard mechanism

Then scale.

**The magic isn’t the snow.**

It’s the moment students realize they can control the physical world outside the classroom with code.
