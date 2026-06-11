Agent 13 — long_term_memory — Fundamentals

IS:
✔️ Embeds text into numerical vectors using an embedding model
✔️ Stores vectors plus metadata persistently in ChromaDB
✔️ Retrieves documents by semantic similarity (cosine distance)

IS NOT:
✗ Does not reason, summarize, or interpret retrieved documents
✗ Does not support deletion or update of stored entries
✗ Does not maintain session-scoped or in-process-only memory

Input: Context object + { mode: "store"|"query", text: str }
Output: { stored: true } on store / [{ document: str, score: float }] on query
