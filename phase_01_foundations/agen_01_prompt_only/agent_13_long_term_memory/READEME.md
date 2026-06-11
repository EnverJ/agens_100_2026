# Agent 13 — long_term_memory

## Purpose
Agent 13 interfaces with a persistent vector database (ChromaDB) to store and retrieve information across sessions. Unlike session-scoped memory, everything written here survives process restarts. The agent converts text into numerical embeddings and stores them alongside metadata. Retrieval works by semantic similarity — not keyword matching — so queries like "what did the user ask about payments?" can surface relevant past entries even if the exact words differ.

## What This Agent Introduces
**Vector databases and semantic memory** — the first agent in the project that writes to persistent storage and retrieves by meaning rather than by exact string comparison.

## How It Works
1. Receive a context object and a text payload (either content to store or a query string).
2. Determine the operation mode: `store` or `query`.
3. For `store`: convert the text to a vector embedding and write it to ChromaDB with metadata (timestamp, session ID).
4. For `query`: convert the query string to a vector, run a similarity search in ChromaDB, return the top-k matched documents.
5. Return either a storage confirmation or a list of retrieved documents.

## What It Is NOT
- No reasoning over retrieved documents
- No session-scoped or in-memory-only storage
- No deletion or update of existing entries
- No ranking beyond cosine similarity score

## Scope
- Embedding text using a sentence-transformer or API-based embedding model
- Writing vectors plus metadata to a local ChromaDB collection
- Querying ChromaDB by semantic similarity
- Returning raw retrieved documents to the caller

## Key Lesson
Persistent memory is not about storing strings — it is about storing meaning. The vector representation allows the system to find relevant history even when the exact words do not match, which is fundamentally different from any database lookup the project has used before.

## Next Step
Once Agent 13 is complete, the project proceeds to Agent 14 — Reflection, which enables the system to evaluate its own outputs.
