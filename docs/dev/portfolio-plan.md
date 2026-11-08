# Portfolio development plan

Status: agreed baseline, recorded 2026-11-08.

This document preserves the agreed scope and sequence. Update it explicitly when
decisions change; outstanding decisions below are not settled requirements.

## Purpose

Showcase selected projects through a personal portfolio with clear summaries,
substantive case studies, and useful media and demo links.

## Audience and introduction

Primary audience: potential employers.

- Public name: Andrei Romashkov.
- Role/title: Software Developer.
- Supporting introduction: “I build web applications, mobile experiences, and
  AI-powered tools.”

## Visual direction

The initial warm editorial design is preserved in commit `3fc4721`. The accepted
redesign from `design/swiss-cobalt` uses Swiss-inspired typography with a bolder contemporary
layout: white and cool gray, near-black text, cobalt accents, strong sans-serif
headings, numbered projects, and larger project imagery. Project visuals retain
their own colors. No italic serif headings. A restrained rotating project showcase is approved
for the homepage hero.

Andrei approved this direction for merging into `main` on 2026-11-08.

## Technical direction

- Astro + TypeScript.
- Markdown case studies in a typed Astro content collection.
- Custom CSS and reusable layouts/components.
- Static pages with standard navigation, media, and links. The approved homepage
  showcase uses a small browser script to crossfade between Conjugadora, Dracones,
  and Cats every six seconds, with manual selection and pause/play controls.
  Hover, keyboard focus, and background tabs suspend rotation; reduced-motion
  preferences start it paused. Without JavaScript the first preview stays usable.
  React islands, filters, interactive galleries, and playable app demos remain deferred.
- A dedicated GitHub repository and Vercel hosting.
- Static output initially; no backend or CMS required for the agreed scope.
- Host the 2048 Android beta download in a GitHub Release and link to it.

Source repository: https://github.com/camomilesson/portfolio2026

## Growing the portfolio

Each project has its own Markdown entry and media. Generate project pages and
listing cards from this collection, so routine additions do not require layout
changes. Include featured status and display order in project metadata. Keep the
homepage curated and make the full collection accessible on an All projects page.

## Featured projects

These five projects form the initial selection, in the agreed display order:

1. Conjugadora — web product development and Spanish conjugation practice.
2. Hic Sunt Dracones — Android exploration app with location tracking and fog of war.
3. Editorial Team — conversational editorial assistant with orchestration,
   persistence, retrieval, and evaluations.
4. 2048 Cats — Unity/C# Android puzzle game with power-ups and a cat-themed identity.
5. Steam Price Modeling — end-to-end data science and ML workflow with API serving.

University Curriculum Scheduler and Breakout50 are candidates for a smaller
additional-projects section. The earlier Editorial Team agent can provide context
within the Editorial Team story. Neither is committed launch scope yet.

## Delivery phases

### 1. Define the story

Audience, introduction, broad visual direction, and project order are agreed above.

### 2. Shape the content

Write a concise summary and case study for each featured project. Cover the
problem, personal contribution, key decisions, outcome, and relevant links.
Identify the screenshots, videos, and charts needed. Ground claims in verified
project evidence and distinguish implemented features from future work.

### 3. Choose the visual direction

Establish typography, colors, and layout. Design the homepage and one
representative project page before extending the system.

### 4. Build the foundation

Set up Astro, reusable layouts, and the typed project collection. Implement the
homepage, project pages, about/contact content, and responsive navigation.

### 5. Bring the projects to life

Integrate optimized media, gameplay clips, source/demo links, and the 2048 beta
download. Keep the first version focused on static presentation; a browser-playable
2048 Cats build or Android emulator is deferred.

### 6. Polish and launch

Check mobile layouts, keyboard access, performance, links, and social sharing
previews. Deploy to Vercel, optionally connect a custom domain, and document how
to add or update projects.

## First milestone

A local homepage and one complete case study, ready to review together before
building out the remaining project pages.

Conjugadora is the first case study. Its working content draft is in
`docs/dev/conjugadora-case-study.md`.

## Outstanding decisions and inputs

- Specific typography, colors, and layout details.
- Individual contributions to team/course projects.
- Screenshots, gameplay recordings, charts, and final demo/download URLs.
- Contact links and whether to include a downloadable CV.
- Domain and whether to include the optional supporting projects.

## Current state

The first local Astro build is implemented: homepage, all-projects index, and five
project pages. All five featured projects have developed case studies, with project media
or technical charts integrated. Optional project logos and portrait screenshot layouts
are supported. Shared layouts, typed Markdown content, responsive CSS, local
fonts, and project ordering are in place. No deployment has been made. Remaining
content and launch work is tracked in `docs/dev/launch-checklist.md`.
