# Agent 21 — Short-Term Memory (Phase 2)

## Purpose
Agent 21 revisits short-term memory in the richer context of Phase 2. Where Agent 12 introduced a simple in-session string list, this agent integrates that concept into the full memory-and-reasoning pipeline. Memory no longer holds raw strings — it stores structured context objects with role, content, timestamp, and tags, giving downstream reasoning agents something they can query, filter, and build upon.

## What This Agent Introduces
Structured session-scoped memory feeding a reasoning pipeline — context objects instead of raw strings.

## How It Works
1. Receive an input message and the current session context object.
2. Parse the input into a structured context entry: `{role, content, timestamp, tags}`.
3. Append the entry to the bounded in-memory session list (capped at N entries, oldest dropped first).
4. Return the full updated context snapshot to the caller for use by downstream reasoning agents.

## What It Is NOT
- No persistence across restarts — this is session-scoped only (see Agent 22 for cross-session memory)
- No semantic search — retrieval is positional and chronological, not similarity-based
- No reasoning — storing context is the only job; no inference happens here

## Scope
- Maintain a bounded list of structured context objects for the current session
- Return a memory snapshot on each update
- Expose a `get_recent(n)` interface for downstream agents to pull the last N entries

## Key Lesson
Structured context objects — not raw strings — are the correct unit of memory for reasoning pipelines. The shape of what you store determines the quality of what you can reason about downstream.

## Next Step
Once Agent 21 is complete, proceed to Agent 22.
