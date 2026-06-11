# Agent Fundamentals: Manager Worker

## IS
- A coordinator agent that decomposes a task and delegates subtasks
- A pattern where the deciding agent and the executing agents are separate
- A sequential dispatcher that calls workers one at a time
- An aggregator that synthesizes worker results into a unified answer
- The entry point for multi-agent thinking in this project

## IS NOT
- Not an executor — the manager does not process domain content itself
- Not aware of worker internals — it only sees inputs and outputs
- Not parallel — workers run sequentially in this implementation
- Not a router — it dispatches to all workers, not conditionally to one
- Not fault-tolerant — no retry logic when a worker fails

## Input
```
task: str  — a natural language description of the high-level task
```

## Output
```
result: str  — a synthesized summary merging all worker outputs
```

## Interfaces
- Manager calls workers via direct function calls (same process)
- Workers receive: subtask_id (int), subtask_text (str)
- Workers return: result_text (str)
- Manager passes all results to a final LLM synthesis call
