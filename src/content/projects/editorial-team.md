---
title: "Editorial Team"
summary: "A conversational AI assistant for drafting, reviewing, and revising your writing."
category: "AI application"
technologies: ["Python", "LangChain", "LangGraph", "Gemini", "SQLite", "MLflow"]
featured: true
order: 3
source: "https://github.com/camomilesson/editorial-team-v2"
accent: "blue"
visual: "A second pair\nof eyes."
role: "Team lead · Team project"
context: "Agentic AI Systems · Harbour.Space"
image: "/images/editorial-team/architecture.svg"
imageAlt: "Editorial Team architecture: Telegram queue, LangGraph Coordinator, Writer–Critic–Editor workflow, hybrid retrieval tools, and SQLite persistence."
imageKind: "screenshot"
screenshots:
  - src: "/images/editorial-team/drafting.webp"
    alt: "A sample LinkedIn announcement drafted by the Writer, reviewed by the Critic, and returned as the working draft in Telegram."
    title: "From a request to a reviewed draft"
    caption: "A demonstration brief for Aurora passes through the Writer and Critic. The labels expose each stage of the editorial workflow."
    width: 1268
    height: 1092
  - src: "/images/editorial-team/revision.webp"
    alt: "An ordinary chat exchange followed by a request to make the earlier Aurora draft more formal, and the revised output."
    title: "Pick up where you left off"
    caption: "An ordinary chat turn doesn’t replace the active writing task. A later request can return to the draft and change its tone."
    width: 1260
    height: 842
  - src: "/images/editorial-team/retrieval.webp"
    alt: "A request retrieves the latest stored dragons tweet; a follow-up asks for a longer version and receives a new draft."
    title: "Find earlier work, then keep writing"
    caption: "A retrieved draft becomes the active task, so a follow-up like ‘make it longer’ applies to the writing just brought back."
    width: 1270
    height: 678
draft: false
---

## The project

Editorial Team is a Telegram assistant that writes, reviews, and revises drafts through conversation. I was the team lead on this project for the Agentic AI Systems course at Harbour.Space.

The most interesting challenge was moving from a custom orchestration harness to LangChain and LangGraph in 24 hours, while keeping the writing workflow working.

## Orchestration and state

**Python and LangGraph** run the conversation and editorial subgraph. A **LangChain tool-calling Coordinator** decides whether a message needs ordinary chat, a new writing task, a revision, or retrieval of earlier work. **Gemini** provides the model responses.

The Writer produces a draft, and the Critic returns a structured PASS or REVISE decision. A revision goes to the Editor; a pass completes the workflow. Each stage shares the same run context, with checks that reject stale or mismatched outputs.

**SQLite checkpoints** preserve conversation state and one active working draft across application restarts. Ordinary chat leaves that draft in place, so a later “make it more formal” can return to it.

## Retrieval that leads back into editing

Completed writing is saved as immutable artifacts in a separate SQLite store. The Coordinator has two scoped tools: `search_corpus` finds relevant excerpts, and `get_draft` loads a complete stored draft.

Search combines **Sentence Transformers embeddings**, exact NumPy cosine search, and **BM25**, then merges the rankings with Reciprocal Rank Fusion. A cross-encoder can optionally rerank the results. Conversation and date filters apply before ranking.

Loading an earlier draft makes it the active writing task. Retrieval alone displays the stored text without rewriting it; a later editing request starts a fresh editorial run.

## Reliability and evaluation

Telegram updates pass through a chat allowlist and a bounded queue with a single worker. Tools are scoped to the current conversation, and structured model responses pass through application validation.

**pytest** covers routing, persistence, restart recovery, isolation, and failure handling. Retrieval and generation evaluations sit alongside full-agent scenarios, where tool selection, parameter correctness, and goal completion are scored separately. **MLflow** records execution traces and evaluation feedback so failures can be inspected after a run.

## Learning to build with AI

AI-assisted development was required for the course. I was used to writing and understanding every line myself, so this pushed me to learn how to delegate to AI, check its work, and decide where closer review mattered.

## Current status

The application can be run locally with Telegram and model credentials. It isn’t currently running as a hosted service. The screenshots show demonstration conversations, not a public live demo.
