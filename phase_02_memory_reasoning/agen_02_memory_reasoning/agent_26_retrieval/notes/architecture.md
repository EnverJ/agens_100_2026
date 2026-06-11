# Architecture — Agent 26: Retrieval

## Data Flow

```
┌─────────────────────┐
│   Input             │
│  query: str         │
│  collection: str    │
│  k: int             │
│  where: dict|null   │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Embedding Model    │  (same model used during storage)
│  embed(query)       │
└────────┬────────────┘
         │
         ▼  query_vector: [float]
┌─────────────────────────────────────────────────────┐
│  Optional Metadata Pre-Filter                       │
│  where: {"type": "bug", "severity": "critical"}     │
│  Applied BEFORE k-NN — reduces candidate set first  │
└────────┬────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────┐
│  ChromaDB k-NN      │
│  cosine distance    │
│  search over        │
│  filtered subset    │
└────────┬────────────┘
         │
         ▼  raw candidates (up to k results)
┌─────────────────────┐
│  Distance Sort      │
│  ascending order    │
│  (lower = closer)   │
└────────┬────────────┘
         │
         ▼
┌───────────────────────────────────────────────────────┐
│  Output                                               │
│  results: [                                           │
│    { id, text, metadata, distance },  ← most similar │
│    { id, text, metadata, distance },                  │
│    ...                                                │
│    { id, text, metadata, distance }   ← least similar│
│  ]                                                    │
│  query_embedding_dim: int                             │
│  collection: str                                      │
└───────────────────────────────────────────────────────┘
```

## Key Design Decisions

- The embedding model is never swapped at query time. The query must be embedded with the same model that was used to embed the stored documents, or distances are meaningless.
- Metadata pre-filtering narrows the candidate pool before k-NN runs, which improves both speed and precision when type or tag constraints are known.
- No LLM is instantiated in this agent. The agent is a pure vector lookup pipeline.
