# Architecture: Agent 23 — Test Run History Analyzer

```
STORE PATH
──────────

  Test Run Result (structured)
  { suite_name, run_date, pass_count,
    fail_count, duration_seconds,
    failures: ["err_1", "err_2"] }
        │
        ▼
┌──────────────────────────────┐
│        Serializer            │
│  Converts struct → text doc  │
│  "Suite checkout_regression  │
│   ran 2026-06-10. 47 passed, │
│   3 failed (94%). Failures:  │
│   cart_total_mismatch."      │
└──────────────┬───────────────┘
               │  text document
               ▼
┌──────────────────────────────┐
│      Embedding Model         │
│   text → float[]             │
└──────────────┬───────────────┘
               │  vector + metadata
               ▼
┌──────────────────────────────┐
│   ChromaDB Upsert            │
│   collection: "test_runs"    │
│   metadata: {                │
│     suite_name,              │
│     run_date,                │
│     pass_rate,               │
│     duration_seconds,        │
│     fail_count }             │
└──────────────┬───────────────┘
               │  writes to disk
               ▼
    [chroma_db/test_runs/ on disk]


QUERY PATH
──────────

  Natural Language Question
  "Has login been failing lately?"
        │
        ▼
┌──────────────────────────────┐
│      Embedding Model         │
│   query → float[]            │
└──────────────┬───────────────┘
               │  query vector
               ▼
┌──────────────────────────────┐
│   ChromaDB k-NN Search       │
│   optional: metadata filter  │
│   (e.g. suite_name="login")  │
└──────────────┬───────────────┘
               │  top-K raw results
               ▼
┌──────────────────────────────┐
│        Retriever             │
│   Formats results into       │
│   ranked history list with   │
│   pass rates, durations,     │
│   top failure messages       │
└──────────────┬───────────────┘
               │
               ▼
  {results: [{suite_name, run_date,
   pass_rate, duration, top_failures,
   similarity_score}]}
```

Key properties:
- The serializer step is critical: structured data must become natural language to embed well
- Metadata is stored separately from the text document and is queryable without embedding
- Collection name "test_runs" is fixed; one collection covers all suites
- suite_name in metadata enables pre-filtering before k-NN search
