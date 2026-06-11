Agent 17 — Input Router Architecture

┌─────────────────────────────────────────────────────┐
│                   Context Object                    │
│  {                                                  │
│    user_input: str,                                 │
│    memory_flag: bool,                               │
│    tool_flag: bool,                                 │
│    session_id: str,                                 │
│    ...                                              │
│  }                                                  │
└───────────────────────┬─────────────────────────────┘
                        │
              ┌─────────▼──────────────────────────────┐
              │         Routing Decision Tree          │
              │                                        │
              │  if memory=T, tool=F:                  │
              │      → "agent_13_long_term_memory"     │
              │                                        │
              │  elif memory=F, tool=T:                │
              │      → "agent_05_multi_tool"           │
              │                                        │
              │  elif memory=T, tool=T:                │
              │      → "agent_11_context_builder"      │
              │        (rebuild with both active)      │
              │                                        │
              │  else (memory=F, tool=F):              │
              │      → "agent_01_prompt_only"          │
              └─────────┬──────────────────────────────┘
                        │
              ┌─────────▼──────────────────┐
              │   Next Agent ID (string)   │
              │   e.g. "agent_13"          │
              └────────────────────────────┘

No state changes. No LLM call. No side effects.
Context object is read-only — not modified by the router.
