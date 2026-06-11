# Architecture: Manager Worker

```
          ┌─────────────────────────────────┐
          │         MANAGER AGENT           │
          │                                 │
  Task ──►│  1. Decompose task into N       │
          │     subtasks via LLM call       │
          │                                 │
          │  2. Dispatch each subtask       │
          └────────┬────────┬────────┬──────┘
                   │        │        │
                   ▼        ▼        ▼
            ┌──────────┐ ┌──────────┐ ┌──────────┐
            │ WORKER 1 │ │ WORKER 2 │ │ WORKER N │
            │          │ │          │ │          │
            │ subtask1 │ │ subtask2 │ │ subtaskN │
            │    ↓     │ │    ↓     │ │    ↓     │
            │ LLM call │ │ LLM call │ │ LLM call │
            │    ↓     │ │    ↓     │ │    ↓     │
            │ result1  │ │ result2  │ │ resultN  │
            └────┬─────┘ └────┬─────┘ └────┬─────┘
                 │             │             │
                 └─────────────┴─────────────┘
                               │
                               ▼
          ┌─────────────────────────────────┐
          │         MANAGER AGENT           │
          │                                 │
          │  3. Aggregate all results       │
          │     via LLM synthesis call      │
          │                                 │
          └──────────────┬──────────────────┘
                         │
                         ▼
                   Final Result

Data flow:
- Manager → Worker: (subtask_id, subtask_description)
- Worker → Manager: (subtask_id, result_text, status)
- Manager → Caller:  unified_summary_string
```
