# Architecture: Agent 21 — Short-Term Memory (Phase 2)

```
Input Event
    │
    ▼
┌─────────────────────────────────┐
│         parse_input()           │
│  Extracts: role, content, tags  │
└─────────────────┬───────────────┘
                  │
                  ▼
┌─────────────────────────────────┐
│      build_context_entry()      │
│  { role, content, timestamp,    │
│    tags, turn_index }           │
└─────────────────┬───────────────┘
                  │
                  ▼
┌─────────────────────────────────┐
│    SESSION MEMORY (in-process)  │
│  [ entry_0, entry_1, ... ]      │
│  Max N entries (sliding window) │
│  Oldest dropped when full       │
└──────┬──────────────────────────┘
       │
       │ append + trim
       ▼
┌─────────────────────────────────┐
│      get_snapshot()             │
│  Returns last N entries as list │
└─────────────────┬───────────────┘
                  │
                  ▼
┌─────────────────────────────────┐
│         Response Object         │
│  { answer, memory_snapshot,     │
│    turn_count, session_id }     │
└─────────────────────────────────┘
       │
       ▼
  Downstream Reasoning Agent
  (reads memory_snapshot to build context)
```

Key properties:
- Memory lives in the Python process (dict/list in RAM)
- Session boundary = process lifetime
- No I/O calls during memory read/write
- Snapshot is a deep copy to prevent mutation by callers
