---
title: "Editorial Team v2"
summary: "A conversational AI assistant for drafting, reviewing, and revising your writing."
category: "AI application"
technologies: ["Python", "LangGraph", "Telegram"]
featured: true
order: 3
source: "https://github.com/camomilesson/editorial-team-v2"
accent: "blue"
visual: "A second pair\nof eyes."
draft: true
---

## Writing as a conversation

Editorial Team v2 is a Telegram assistant that can start a writing task, review a draft, apply changes, and return to the latest task across later messages and application restarts.

## How the pieces work together

LangGraph owns the conversation and editorial workflow. A Coordinator routes the request, a Writer produces a draft, a Critic reviews it, and an Editor applies changes when revision is needed. SQLite checkpoints preserve conversation state and the working draft.

## Finding earlier work

Completed writing is stored as immutable artifacts. Conversation-scoped retrieval combines lexical and semantic search, with optional reranking, to find relevant earlier work.

## Evaluating the system

The repository includes retrieval and judged-generation evaluations. The reports cover failure cases as well as aggregate scores, including the difficulty of answering questions that need context from several chunks.
