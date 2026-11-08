# Conjugadora — case study draft

Status: revised for a technical employer audience, 2026-11-08. Not published.

Personal context is condensed into one opening paragraph. Technical details were
checked against the application README, package scripts, CI workflow, and database
migrations. The website copy is maintained in `src/content/projects/conjugadora.md`.

## The idea

I built Conjugadora as a solo project for a three-week JavaScript and TypeScript course. I was learning Spanish and wanted better conjugation practice, so I turned the assignment into something I’d use myself. The course allowed AI-assisted development, which helped me take it beyond a basic prototype.

## Frontend and architecture

The app uses **React, TypeScript, Vite, and plain CSS**, with React Router handling navigation. Features keep their components, styles, tests, and documentation together behind public entry points.

Question generation and answer checking are separate from React and network code. That keeps the practice rules testable without rendering the interface or connecting to the backend.

## Practice data and answer checking

A separate **pnpm workspace package** contains the catalogue of 100 verbs and 16 practice categories. Conjugations come from versioned JSON files, with the catalogue loaded first and individual verb files loaded as needed.

Questions are shuffled without replacement. Typed answers support accepted alternatives and configurable accent handling; multiple-choice options match the verb and grammatical person. The app validates catalogue IDs and dataset versions before use.

## Accounts and persistence

**Supabase Auth** handles Google sign-in. **PostgreSQL** stores account preferences, progress, and completed practice history, with row-level security restricting access to each user’s data. Database functions group related updates into atomic operations.

Signed-in answers update progress as they are saved. Only completed practices appear in History. If a submission fails, the app offers a retry with the same answer identifier to avoid counting it twice.

Guests can practise without an account. Their settings stay in the browser, while their answers and results stay in memory. Account deletion runs through a **Supabase Edge Function**, keeping privileged credentials on the server.

## Progress and customization

These are the two features I’m most proud of. The progress matrix breaks accuracy down by verb and tense, with search, sorting, filters, and keyboard navigation. Overall accuracy uses total correct answers divided by total attempts, and each cell exposes its sample size.

Practice settings cover verbs, categories, grammatical persons, question count, answer mode, and accent handling. Saved preferences let people return to a setup that works for them.

## Testing and delivery

**Node’s test runner** covers practice logic, catalogue data, repositories, and the account-deletion handler. **GitHub Actions** runs TypeScript, ESLint, formatting checks, tests, ordered builds, and a production artifact audit for relevant code changes.

**Nx** ensures catalogue checks pass before the app builds. **Vercel** serves the frontend, with Supabase providing the backend services.

## Current limits

Desktop is the current focus. There’s no durable offline queue or resumable practice yet. Mobile polish and spaced repetition are possible next steps.

## Editorial notes — not website copy

- Andrei supplied the motivation, solo ownership, course duration, AI use, and
  feature priorities. Technical details were checked against the local app source.
- Three weeks describes the course duration, not a verified timeline for every
  feature in the current app. Avoid treating it as a full product delivery metric.
- Customization is configurable practice, not automatic personalization.
- Live URL confirmed by Andrei: https://conjugadora.vercel.app.
- User-supplied screenshots are integrated for practice home, progress, preferences,
  and history. The exported preferences screenshot excludes the account panel.
- Do not invent usage numbers, learning improvements, or test coverage percentages.
