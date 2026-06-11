# Tool Patterns: Agent 21 — Short-Term Memory (Phase 2)

## Pattern: Bounded Sliding Window Buffer

Maintain a fixed-size list. On each new entry, append and then slice to the last N items. This prevents unbounded memory growth and mirrors the "recent context" model that LLMs expect.

```python
MAX_ENTRIES = 20

def append_entry(session: list, entry: dict) -> list:
    session.append(entry)
    return session[-MAX_ENTRIES:]
```

## Pattern: Structured Context Object

Always store context as a typed dict — not a raw string. Include role, content, timestamp, and tags. This makes the memory useful not just for prompt injection but also for filtering and downstream reasoning.

```python
def build_entry(role: str, content: str, tags: list, turn_index: int) -> dict:
    return {
        "role": role,
        "content": content,
        "timestamp": datetime.utcnow().isoformat(),
        "tags": tags,
        "turn_index": turn_index
    }
```

## Pattern: Snapshot Isolation (Deep Copy)

When returning memory to downstream agents, return a copy — not a reference to the internal list. This prevents callers from accidentally mutating the stored state.

```python
import copy

def get_snapshot(session: list) -> list:
    return copy.deepcopy(session)
```

## Pattern: Session Key Routing

Use a session_id string to route memory to the correct session buffer. Multiple concurrent sessions each have their own list, keyed in a dict.

```python
sessions: dict[str, list] = {}

def get_or_create_session(session_id: str) -> list:
    if session_id not in sessions:
        sessions[session_id] = []
    return sessions[session_id]
```
