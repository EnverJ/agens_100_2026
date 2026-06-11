# Architecture: Agent 24 — Test History Memory

```
STORE PATH
──────────

  Single Test Result
  { test_name: "test_login_oauth_redirect",
    outcome: "fail",
    error_message: "TimeoutError: redirect took 8.2s",
    duration_ms: 8200,
    run_id: "run_20260610_142",
    timestamp: "2026-06-10T14:23:11Z" }
        │
        ▼
┌──────────────────────────────────────┐
│           Serializer                 │
│  "Test test_login_oauth_redirect     │
│   failed on 2026-06-10T14:23:11Z.   │
│   Error: TimeoutError: redirect      │
│   took 8.2s. Duration: 8200ms.      │
│   Run: run_20260610_142."            │
└──────────────────┬───────────────────┘
                   │  text
                   ▼
┌──────────────────────────────────────┐
│         Embedding Model              │
│      text → float[]                  │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│         ChromaDB Upsert              │
│   collection: "test_outcomes"        │
│   metadata: {                        │
│     test_name,   ← primary key       │
│     outcome,                         │
│     timestamp,                       │
│     run_id,                          │
│     duration_ms }                    │
└──────────────────┬───────────────────┘
                   │  writes to disk
                   ▼
    [chroma_db/test_outcomes/ on disk]
    (one entry per individual test run)


QUERY PATH
──────────

  Query: { test_name: "test_login_oauth_redirect",
            last_n: 10 }
        │
        ▼
┌──────────────────────────────────────┐
│   ChromaDB Metadata Filter           │
│   where: { test_name:                │
│     "test_login_oauth_redirect" }    │
│   (pre-filter, no k-NN needed yet)   │
└──────────────────┬───────────────────┘
                   │  candidate set
                   ▼
┌──────────────────────────────────────┐
│   Sort by timestamp (recency)        │
│   Take last_n entries                │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│   Response Builder                   │
│   Computes: failure_rate             │
│   Extracts: last_seen_error          │
│   Returns: ordered outcome list      │
└──────────────────┬───────────────────┘
                   │
                   ▼
  { test_name, outcomes: [...],
    failure_rate, last_seen_error }
```

Key properties:
- test_name metadata field is the lookup key; all entries for a test share this field
- Retrieval is primarily metadata-filtered, not semantic — we know the exact test name
- Results sorted by timestamp descending (most recent first)
- failure_rate is computed client-side from the returned outcomes
