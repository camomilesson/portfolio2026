# Andrei Romashkov — Portfolio

A static portfolio built with Astro, TypeScript, Markdown content collections,
and custom CSS. This first version is local and has not been deployed.

## Development

Use Node.js 24 and pnpm 12.

```sh
pnpm install
pnpm dev
```

Open the local URL printed by Astro (normally http://localhost:4321).

```sh
pnpm build    # Type/content checks and production build
pnpm preview  # Serve dist/ locally
```

## Add a project

Add a Markdown file to `src/content/projects/`. Its filename becomes the URL slug.
Copy an existing entry and update the title, summary, category, technologies,
source URL, accent, and visual heading. Set `featured: true` to include it on the
homepage, and use `order` to control placement. All entries appear on `/projects/`.
Write the case study below the frontmatter. `draft: true` shows a note that the
full case study is still to follow; it does not hide the page.

Optional `image` and `imageAlt` fields replace the typographic preview with project
artwork. Put images under `public/images/`; use optimized exports, not raw captures.
Set `imageKind: screenshot` to show a complete screenshot without artwork styling.
Optional `screenshots` entries (src, alt, title, caption, width, height) add a static
product gallery below the case study. Set `imageLayout: portrait` for a phone screenshot. Each gallery entry can also
set `layout: portrait` to display phone captures in a two-column gallery.

An optional `logo` object with `src` and `alt` displays a project logo beside its
title in listing cards and the project header. Omit it for projects without a logo.
Optional `role` and `context` fields add contribution and project context to the
case-study sidebar. An optional `live` field adds a website link. Omit unavailable links.

## Structure

- `src/content/projects/`: project metadata and case studies.
- `src/content.config.ts`: typed content schema.
- `src/components/`: project cards and previews.
- `src/layouts/Layout.astro`: shared document, navigation, and footer.
- `src/pages/`: homepage, project index, and generated project pages.
- `src/styles/global.css`: responsive visual system.
- `docs/dev/`: agreed plan, content drafts, and outstanding launch work.

Fonts are self-hosted; their licenses are in `public/fonts/`. The cat tile artwork
comes from Andrei's 2048 project. Other project previews are clearly marked
editorial placeholders, not screenshots.

## Hosting later

Import the GitHub repository into Vercel using its Astro preset. Build command:
`pnpm build`; output directory: `dist`. No environment variables or server adapter
are required for this version. Set the canonical site URL and social preview image
once the deployment address or domain is chosen.
