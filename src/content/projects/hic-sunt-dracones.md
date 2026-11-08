---
title: "Hic Sunt Dracones"
summary: "An Android app that turns everyday exploration into a map worth uncovering."
category: "Mobile application"
technologies: ["Kotlin", "Jetpack Compose", "Google Maps", "H3", "Room"]
featured: true
order: 2
source: "https://github.com/camomilesson/hic-sunt-dracones-map"
accent: "ochre"
visual: "Here be\ndragons."
image: "/images/dracones/map-parchment.webp"
imageAlt: "Hic Sunt Dracones map with explored streets revealed through parchment-colored fog."
imageKind: "screenshot"
imageLayout: "portrait"
heroLayout: "screenshot-strip"
logo:
  src: "/images/dracones/logo.webp"
  alt: "Hic Sunt Dracones dragon and compass logo"
screenshots:
  - src: "/images/dracones/map-night.webp"
    alt: "Explored streets and parks revealed through blue fog on the map."
    title: "Find a different way home"
    caption: "Explored cells reveal the map, making unfamiliar streets easier to spot."
    width: 576
    height: 1280
    layout: "portrait"
  - src: "/images/dracones/map-parchment.webp"
    alt: "Parchment-colored fog surrounds explored routes in the city."
    title: "Here be dragons"
    caption: "Map styling and fog colors can be combined to give exploration a different feel."
    width: 576
    height: 1280
    layout: "portrait"
  - src: "/images/dracones/statistics.webp"
    alt: "Discovery statistics with local exploration percentages, total uncovered cells, estimated area, and personal records."
    title: "See how far you’ve explored"
    caption: "Discovery statistics show nearby coverage, uncovered cells, estimated area, and recent activity."
    width: 576
    height: 1280
    layout: "portrait"
  - src: "/images/dracones/settings.webp"
    alt: "Settings for fog opacity, map styles, fog colors, and visibility of map features."
    title: "Make the map yours"
    caption: "Adjust the fog, choose a map style, and control which places and transport details appear."
    width: 576
    height: 1280
    layout: "portrait"
draft: false
---

## The idea

I often walk to university or the climbing gym and like trying new streets along the way. Remembering where I haven’t been is harder. So I built a fog-of-war exploration app for my Mobile Development course at Harbour.Space. It was a solo project: I built the whole app.

## Android architecture

The app uses **Kotlin, Jetpack Compose, and Material 3**, with **Google Maps Compose** displaying the map. ViewModels expose state through **StateFlow**, while repositories handle exploration data and map themes.

Location updates come from Google’s fused location provider. A foreground service keeps tracking active when the app is in the background, with a persistent notification and permission checks.

## Storing exploration with H3

Keeping every walked path would make storage grow with each trip, including repeated journeys down the same streets. **H3** gave me a way to represent explored areas as cells instead.

Each location maps to a resolution-11 cell. **Room** stores one record per visited cell, including its first and latest visit, visit count, and parent cells for broader areas. Revisiting a cell updates that record rather than adding another path.

The parent hierarchy also supports exploration summaries at block, neighborhood, and district scales. Progress shows coverage around the most recently visited cell, along with estimated uncovered area and activity records.

## Drawing the fog efficiently

Storage was only half the challenge. Drawing every discovered hexagon separately would create more work as the explored area grew.

The app merges neighboring cells into region outlines, then uses those outlines as holes in a fog polygon. Unexplored pockets inside an explored region are filled back in, so walking around a block doesn’t reveal its interior.

Geometry processing runs on a background dispatcher, and cell boundaries are cached. The map filters region outlines against a padded viewport and hides fog at low zoom levels. These choices keep the rendering focused on the current view.

## Themes and persistence

Users can adjust fog opacity and color, choose map themes, and toggle map details. **Retrofit** fetches theme definitions, with a Room cache and built-in fallbacks when theme downloads are unavailable. Exploration data stays on the device; map availability still depends on Google Maps.

## Current status

The app works but hasn’t been published to an app store. A few testers still use it for their own exploration.
