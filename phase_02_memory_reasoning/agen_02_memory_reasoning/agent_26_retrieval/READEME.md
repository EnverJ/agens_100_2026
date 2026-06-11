# Agent 26 — Retrieval

## Purpose
Agent 26 is a pure retrieval engine. It takes a natural-language query, converts it to an embedding, and searches a ChromaDB collection for the most semantically similar stored documents. It returns ranked results with similarity scores. There is no LLM generation involved — this agent's entire job is finding relevant information, not creating new content. Understanding pure retrieval is essential before building retrieval-augmented generation (RAG) systems.

## What This Agent Introduces
Semantic retrieval via embedding similarity search — querying a vector store to find the most relevant stored documents using k-nearest neighbors, without any LLM generation step.

## How It Works
1. Receive a query string and optional filter parameters (collection name, k, metadata filters).
2. Embed the query string using the same embedding model used during storage.
3. Run a k-nearest-neighbor search against the target ChromaDB collection.
4. Return the top-K results sorted by cosine similarity distance, with document text, metadata, and relevance score.

## What It Is NOT
- No generation — the LLM is not called, no answer text is produced
- No reranking beyond the initial k-NN distance score
- No summarization of retrieved results
- No writing to the vector store (read-only operation)
- No fallback to keyword search when similarity is low

## Scope
- Accept a query string and return top-K semantically similar documents
- Support metadata pre-filtering before similarity ranking
- Return distance scores alongside document content and metadata
- Work against any named ChromaDB collection passed as input

## Key Lesson
Retrieval and generation are separate concerns. Mastering pure retrieval — knowing exactly what comes back, why, and how it is scored — is the prerequisite to building trustworthy RAG systems.

## Next Step
Once Agent 26 is complete, proceed to Agent 27.
