# Agent 22 — Long-Term Memory

## Purpose
Agent 22 introduces persistent, cross-session memory using ChromaDB, an embedded vector database. For the first time in this series, the system can remember information across restarts. Text is converted to an embedding vector and stored alongside metadata. Later queries retrieve semantically similar memories even when exact words differ. This is the foundation all retrieval-augmented agents in Phase 2 are built on.

## What This Agent Introduces
ChromaDB as a persistent vector store — embedding text, storing it with metadata, and retrieving by semantic similarity across sessions.

## How It Works
1. On a STORE call, the agent takes input text and optional metadata, generates an embedding via the embedding model, and upserts the vector + metadata into a ChromaDB collection.
2. On a QUERY call, the agent embeds the query string and performs a k-nearest-neighbor search over the stored vectors, returning the top-K most similar entries with their distances.
3. The ChromaDB collection persists to disk between runs, so memory survives process restarts.

## What It Is NOT
- No in-memory-only storage — this agent always writes to disk
- No keyword search — retrieval is by embedding similarity, not exact match
- No LLM reasoning — the agent stores and retrieves, it does not generate
- No automatic summarization of old entries
- No multi-user isolation (single collection, single user context)

## Scope
- Manage a named ChromaDB collection for long-term storage
- Accept STORE and QUERY operations as the two core actions
- Return top-K results with similarity scores and metadata
- Persist data between sessions using ChromaDB's on-disk backend

## Key Lesson
Vectors make memory semantic. Storing text as an embedding means you can find relevant memories using meaning, not just matching words — and those memories survive beyond the current session.

## Next Step
Once Agent 22 is complete, proceed to Agent 23.
