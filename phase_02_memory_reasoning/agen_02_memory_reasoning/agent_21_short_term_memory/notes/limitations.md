# Limitations: Agent 21 — Short-Term Memory (Phase 2)

This agent does NOT:

- Persist memory across process restarts — all session data is lost when the Python process exits
- Store memory to disk, a database, or any external system
- Perform semantic search or similarity-based retrieval over stored entries
- Summarize or compress old entries to make room — it simply drops the oldest
- Share memory across different session IDs or users
- Reason about the stored content — it stores and returns, nothing more
- Handle concurrent write safety — this implementation is not thread-safe without external locking
- Support memory expiry by time — entries only expire when pushed out by the sliding window
- Retrieve entries by tag, role, or keyword — the snapshot is always returned in full, not filtered
