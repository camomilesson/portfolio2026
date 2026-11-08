# Hic Sunt Dracones — case study

Status: first full draft integrated into the local portfolio, 2026-11-08.

## Evidence and assets

- Andrei confirmed solo ownership, the walking/exploration motivation, course
  context, storage/rendering challenge, and ongoing use by a few testers.
- Technical details checked against public repository commit
  `f3e70f67e12a950073737575f5fd03d570fe5ba3`: H3Manager, MapScreen, MapViewModel, Room entities/DAO,
  location tracking service, repositories, and Gradle dependencies.
- Four screenshots supplied by Andrei; project logo extracted from the repository
  launcher artwork. Only optimized image exports are stored in the portfolio.
- Status: functional, unpublished to app stores. No public demo/download link added.
- No quantified storage or rendering improvements have been claimed.

## Website copy

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
