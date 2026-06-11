# Agent Fundamentals: Agent 21 — Short-Term Memory (Phase 2)

## IS / IS NOT

### This agent IS:
- A session-scoped, structured context store
- An in-process memory manager (RAM only)
- A sliding-window buffer capped at a fixed entry count
- A context provider for downstream Phase 2 reasoning agents
- A Phase 2 evolution of Agent 12's basic string-list memory

### This agent IS NOT:
- Not a database (no disk writes)
- Not a vector store (no embeddings)
- Not a retrieval engine (no similarity search)
- Not a reasoning agent (no inference or decision-making)
- Not persistent (memory is lost on process restart)

## Input Definition

```python
{
  "session_id": str,          # Identifies the current session
  "role": str,                # "user" | "assistant" | "system"
  "content": str,             # The message or observation text
  "tags": list[str],          # Optional semantic tags, e.g. ["error", "test_name"]
  "metadata": dict            # Optional extra key-value pairs
}
```

## Output Definition

```python
{
  "status": "ok",
  "turn_index": int,          # Position of this entry in the session
  "memory_snapshot": [        # Last N context entries
    {
      "role": str,
      "content": str,
      "timestamp": str,       # ISO 8601
      "tags": list[str],
      "turn_index": int
    }
  ],
  "session_entry_count": int  # Total entries stored this session
}
```
