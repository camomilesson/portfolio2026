# Conjugadora — case study draft

Status: content draft for review, 2026-11-08. Not published.

## Overview

A Spanish conjugation practice app I built for myself and other learners.

Solo project · Three-week JavaScript and TypeScript course · AI-assisted development

Source: https://github.com/camomilesson/website-to-conjugate-verbs

## Why I built it

Conjugadora started as a project for my JavaScript and TypeScript course. The
assignment called for something basic, but I wanted to build a complete product.

I’m learning Spanish and nearly finished Duolingo’s English-to-Spanish course,
but I still needed more conjugation practice. The tools I found were either
frustrating to use or buried behind paywalls. So I built something I’d actually
want to use—and made it my course project.

## How I built it

This was a solo project for a three-week course. AI-assisted development was
allowed, and I used it to help turn the idea into a usable product within that
time, with working features beyond the basic practice screen.

## What I’m proud of

### Seeing where you struggle

The progress view helps you spot the verbs and tenses you’re getting wrong,
so you can see what needs more practice. It breaks down accuracy by verb and
tense and shows how many answers each result is based on.

### Making practice work for you

You can choose the verbs, tense categories, grammatical persons, and number of
questions you want to practise. You can type answers or use multiple choice,
and choose how strictly accents are checked. That flexibility lets you focus
on what you need and practise in a way that suits you.

## Technical foundation

React, TypeScript, and Vite power the interface. A separate verb catalogue
provides the practice data. Supabase handles sign-in and saved account data,
including preferences, progress, and practice history.

## Editorial notes — not website copy

- The motivation, solo ownership, course duration, AI use, and feature priorities
  come directly from Andrei. Feature and stack details come from the repository
  review; recheck them against the final version before publication.
- Three weeks describes the course duration, not a verified timeline for every
  feature in the current app. Confirm this distinction before adding a project
  duration label to the website.
- Describe customization as configurable practice. Do not imply automatic
  personalization, spaced repetition, or automatic targeting of weak verbs.
- Confirm the canonical live URL: the repository metadata and README previously
  linked different Vercel domains.
- Capture practice/customization and progress screenshots. Use real personal
  data with permission or clearly labelled demo data.
- Still to add: a concrete technical decision or challenge, and current outcome
  and limitations. Do not invent usage numbers or learning improvements.
