# Limitations: Agent 22 — Long-Term Memory

This agent does NOT:

- Summarize or compress old entries — the collection grows unboundedly; no pruning, merging, or distillation of stale memories occurs
- Support multi-user isolation — all entries share a single ChromaDB collection; there is no per-user namespace or access control
- Perform keyword or exact-match search — retrieval is embedding-based only; you cannot query for an exact string or ID by content
- Reason about retrieved results — it returns the top-K entries and distances; any interpretation or synthesis is the caller's responsibility
- Detect duplicate semantic content — two entries with near-identical meaning but different IDs will both be stored; deduplication is not automatic
- Support time-range queries natively — ChromaDB metadata filters require exact or comparison operators; date-range filtering requires the caller to encode dates as filterable metadata fields
- Guarantee retrieval order stability — approximate nearest-neighbor indexes (HNSW) can return slightly different result sets across index rebuilds
- Handle embedding model version changes — if the embedding model is swapped, existing vectors become incompatible with new query vectors; the collection must be rebuilt
- Provide read-your-writes consistency under concurrent writes — ChromaDB's embedded mode is not designed for high-concurrency multi-process writes
- Expire or evict old entries automatically — there is no TTL or age-based eviction; old memories persist indefinitely unless explicitly deleted
