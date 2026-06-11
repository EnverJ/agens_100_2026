# Agent Fundamentals: Agent 22 — Long-Term Memory

## IS / IS NOT

### This agent IS:
- A persistent, cross-session memory store backed by ChromaDB on disk
- A semantic retrieval engine using embedding-based k-nearest-neighbor search
- A structured storage system that pairs vectors with metadata
- The foundation for all RAG-based agents in Phase 2
- A two-operation interface: STORE and QUERY

### This agent IS NOT:
- Not a keyword search engine — retrieval is by embedding similarity, not exact match
- Not an LLM reasoning agent — it stores and retrieves, it does not generate or infer
- Not a session memory store — Agent 21 handles in-session context
- Not a multi-user system — single collection, no per-user isolation
- Not a summarization agent — old entries are never compressed or merged
- Not a relational database — no SQL, no joins, no schema enforcement

## Input Definition

### STORE operation
```python
{
  "operation": "store",
  "text": str,           # The text content to embed and store
  "metadata": dict,      # Optional: {timestamp, tags, source, session_id, ...}
  "id": str              # Optional: stable ID for upsert (auto-generated if omitted)
}
```

### QUERY operation
```python
{
  "operation": "query",
  "text": str,           # The query string to embed and search with
  "k": int,              # Number of top results to return (default: 5)
  "where": dict          # Optional: ChromaDB metadata filter, e.g. {"tags": "auth"}
}
```

## Output Definition

### STORE response
```python
{
  "status": "stored",
  "id": str,             # The ID under which the entry was stored
  "collection": str      # Name of the ChromaDB collection used
}
```

### QUERY response
```python
{
  "status": "ok",
  "query": str,          # Echo of the query text
  "results": [
    {
      "text": str,        # Original stored text
      "metadata": dict,   # Metadata attached at store time
      "distance": float   # Cosine distance (lower = more similar)
    }
  ],
  "result_count": int
}
```
