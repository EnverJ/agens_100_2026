# Architecture: Agent 22 — Long-Term Memory

```
STORE PATH
──────────

  Input Text + Metadata
        │
        ▼
┌───────────────────────┐
│   Embedding Model     │
│  text → float[]       │
│  (e.g. 384-dim vec)   │
└──────────┬────────────┘
           │  vector
           ▼
┌───────────────────────┐
│   ChromaDB Upsert     │
│  id:  uuid            │
│  doc: original text   │
│  emb: float[]         │
│  meta: {timestamp,    │
│          tags, src}   │
└──────────┬────────────┘
           │  writes to disk
           ▼
  [chroma_db/ on disk]
  ┌─────────────────┐
  │  collection:    │
  │  "long_term"    │
  │  entry_0        │
  │  entry_1        │
  │  ...            │
  └─────────────────┘

QUERY PATH
──────────

  Query String ("what did we learn about auth errors?")
        │
        ▼
┌───────────────────────┐
│   Embedding Model     │
│  query → float[]      │
└──────────┬────────────┘
           │  query vector
           ▼
┌───────────────────────┐
│   ChromaDB k-NN       │
│   Search              │
│   (cosine similarity) │
│   optional: metadata  │
│   pre-filter          │
└──────────┬────────────┘
           │  top-K results
           ▼
┌───────────────────────┐
│  Result List          │
│  [ { text,            │
│      metadata,        │
│      distance } ]     │
│  sorted by similarity │
└───────────────────────┘
           │
           ▼
  Caller / Downstream Agent
```

Key properties:
- ChromaDB collection persists to disk; survives process restarts
- Embedding model runs locally (no API call required for default model)
- Upsert by ID prevents duplicates on re-store of the same content
- Distance is cosine distance: 0.0 = identical, 2.0 = maximally dissimilar
- k-NN search is approximate (HNSW index) — fast but not exhaustive
