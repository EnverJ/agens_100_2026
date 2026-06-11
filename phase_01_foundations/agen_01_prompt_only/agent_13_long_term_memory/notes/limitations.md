Agent 13 — Limitations

This agent does NOT:
• Reason, summarize, or act on retrieved documents — it only returns them raw
• Support updating or deleting entries once written to ChromaDB
• Handle texts longer than the embedding model's token limit (typically ~512 tokens) — long inputs are silently truncated
• Maintain any awareness of the current session — all stored entries are treated as equally relevant regardless of when they were written
• Rank results by anything other than cosine similarity — no recency weighting, no importance scoring

We change one variable at a time.
