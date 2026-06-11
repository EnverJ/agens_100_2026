# Limitations: Agent 23 — Test Run History Analyzer

This agent does NOT:

- Execute tests — it stores and queries results only; it has no connection to a test runner or CI system
- Parse raw log files — it accepts pre-structured run summaries; log parsing is the caller's responsibility
- Detect statistical significance — trend detection is based on retrieval similarity, not statistical tests; "has this been failing" is answered by recalling similar runs, not by computing failure rate confidence intervals
- Send alerts or notifications — it is a passive recall system; it does not push results to any channel
- Support native time-range queries — to filter by date, the caller must set run_date as a metadata field and use ChromaDB's comparison operators; there is no built-in date window query
- Aggregate across suites automatically — cross-suite analysis requires multiple queries and caller-side aggregation
- Detect root causes — it surfaces failure messages from historical runs but does not reason about why failures occurred
- Track individual test cases — it stores suite-level summaries, not per-test outcomes (see Agent 24 for per-test memory)
- Handle large failure lists efficiently — storing hundreds of failure messages in a single text document degrades embedding quality; callers should truncate to the top N failures before storing
- Support concurrent writes safely — ChromaDB embedded mode is not designed for simultaneous multi-process writes to the same collection
