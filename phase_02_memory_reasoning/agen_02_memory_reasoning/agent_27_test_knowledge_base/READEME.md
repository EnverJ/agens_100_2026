# Agent 27 — Test Knowledge Base

## Purpose
Agent 27 is a curated, queryable knowledge base for SDET teams. It stores known bugs, test patterns, test suite descriptions, and testing conventions in ChromaDB. Any team member (or agent) can ask "Do we have tests for the payment timeout scenario?" and get semantically matched answers — even if the stored document uses different terminology. This is institutional knowledge made searchable.

## What This Agent Introduces
A domain-specific vector knowledge base for test engineering — storing and retrieving SDET institutional knowledge using semantic search so that test coverage questions can be answered without exact keyword matches.

## How It Works
1. During setup, known bugs, test suite descriptions, and testing conventions are ingested into ChromaDB as text documents with type metadata (bug, pattern, suite, convention).
2. On a query, the agent embeds the question and retrieves the top-K most relevant knowledge entries.
3. Results are filtered by type if requested, and returned with their category, source reference, and similarity score.
4. New knowledge can be added incrementally as the team learns new patterns or discovers new bugs.

## What It Is NOT
- No test execution — this is a knowledge store, not a test runner
- No live bug tracker integration — knowledge is curated and stored, not synced from Jira
- No natural-language answer generation — retrieval only, the caller generates the answer
- No automatic knowledge extraction from test files

## Scope
- Store four knowledge types: bugs, test patterns, suite descriptions, conventions
- Query by natural language with optional type filter
- Return top-K results with category, similarity score, and source reference
- Support incremental ingestion of new knowledge entries

## Key Lesson
Institutional knowledge has no value if it cannot be found. Embedding test knowledge as vectors makes it retrievable by meaning, so an agent asking about "timeout handling" will find the "payment gateway latency tests" even without exact word overlap.

## Next Step
Once Agent 27 is complete, proceed to Agent 28.
