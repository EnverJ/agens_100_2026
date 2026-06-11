# Limitations: Agent 24 — Test History Memory

This agent does NOT:

- Compute flakiness scores — it returns raw outcome history; computing a flakiness metric from that history is the responsibility of the caller or Agent 37
- Execute tests — it stores and retrieves outcomes only; it has no connection to any test framework or runner
- Aggregate across test names — all retrieval is scoped to a single test_name per query; cross-test aggregation requires multiple calls and caller-side synthesis
- Auto-detect related tests — it does not identify tests that exercise the same code path or fail together; that analysis requires Agent 39 (Similar Failure Finder)
- Sort natively by recency — ChromaDB returns results sorted by similarity distance, not by timestamp; recency ordering is implemented client-side after retrieval
- Handle test renames — if a test is renamed, old entries retain the old test_name in metadata; there is no migration or aliasing mechanism
- Detect root causes — it surfaces error messages from historical outcomes but performs no analysis on why the failures occurred
- Support time-windowed queries natively — filtering "outcomes from the last 7 days" requires storing timestamps as comparable metadata and using ChromaDB's `$gt` operator; this is not automatically enforced
- Store stack traces or log output — it stores only the error_message string; full stack traces must be truncated or stored separately
- Support concurrent writes safely — ChromaDB embedded mode does not guarantee safe concurrent multi-process writes to the same collection
