---
title: "Conjugadora"
summary: "A Spanish conjugation app built around the way you want to practise."
category: "Web application"
technologies: ["React", "TypeScript", "Supabase"]
featured: true
order: 1
source: "https://github.com/camomilesson/website-to-conjugate-verbs"
live: "https://conjugadora.vercel.app"
liveLabel: "Try Conjugadora"
accent: "green"
visual: "Practica.\nRepite. Aprende."
image: "/images/conjugadora/home.webp"
imageAlt: "Conjugadora practice home with multiple-choice and typing modes and a summary of the current setup."
imageKind: "screenshot"
screenshots:
  - src: "/images/conjugadora/progress.webp"
    alt: "Progress table showing accuracy by Spanish verb and tense, with search, mode filters, and column controls."
    title: "See what needs another look"
    caption: "Accuracy by verb and tense makes the gaps easier to spot. Search, sorting, and column choices help you focus on what matters to you."
    width: 1800
    height: 1144
  - src: "/images/conjugadora/settings.webp"
    alt: "Practice preferences for answer mode, verbs, tenses and moods, grammatical persons, and question count."
    title: "Set up practice your way"
    caption: "Choose what to practise and how to answer, then save those choices as your defaults."
    width: 1800
    height: 677
  - src: "/images/conjugadora/history.webp"
    alt: "Completed practice history with scores, selected settings, and examples of mistakes alongside accepted answers."
    title: "Look back at each session"
    caption: "History keeps completed practices together with their scores, settings, and an example mistake."
    width: 1800
    height: 1139
draft: false
---

## Why I built it

Conjugadora started as a project for my JavaScript and TypeScript course. The assignment called for something basic, but I wanted to build a complete product.

I’m learning Spanish and nearly finished Duolingo’s English-to-Spanish course, but I still needed more conjugation practice. The tools I found were either frustrating to use or buried behind paywalls. So I built something I’d actually want to use—and made it my course project.

## How I built it

This was a solo project for a three-week course. AI-assisted development was allowed, and I used it to help turn the idea into a usable product within that time, with working features beyond the basic practice screen.

## What I’m proud of

### Seeing where you struggle

The progress view helps you spot the verbs and tenses you’re getting wrong, so you can see what needs more practice. It breaks down accuracy by verb and tense and shows how many answers each result is based on.

### Making practice work for you

You can choose the verbs, tense categories, grammatical persons, and number of questions you want to practise. You can type answers or use multiple choice, and choose how strictly accents are checked. That flexibility lets you focus on what you need and practise in a way that suits you.

## Under the hood

React and TypeScript power the interface, with Vite handling the build. The verb catalogue lives in a separate workspace package, while answer checking and question generation stay independent of the interface and network clients.

Supabase handles Google sign-in and saved account data. Guests can practise without an account; signing in adds saved preferences, progress, and practice history.

## Where it stands

The app supports both practice modes, custom practice settings, progress tracking, and history. Desktop is the current focus. Mobile polish, resumable practice, and spaced repetition are possible next steps, rather than features it already has.
