# Agent 41 — Manager Worker

## Purpose
This agent implements the supervisor pattern in multi-agent systems. A single manager agent receives a high-level task, decomposes it into subtasks, delegates each subtask to a dedicated worker agent, and then aggregates all results into a final unified output. The manager never performs the actual work — its job is coordination, delegation, and synthesis.

## What This Agent Introduces
The supervisor pattern: one orchestrating agent delegates to many executing agents, separating coordination logic from execution logic.

## How It Works
1. Manager receives a high-level task (e.g., "analyze these 5 documents")
2. Manager decomposes the task into N subtasks (one per document)
3. Manager calls worker agents, passing each subtask with its specific inputs
4. Each worker agent processes its subtask independently and returns a result
5. Manager collects all worker results
6. Manager aggregates and synthesizes results into a single coherent output
7. Final aggregated result is returned to the caller

## What It Is NOT
- No parallel execution — workers are called sequentially in this agent (see Agent 52 for parallel)
- No worker self-selection — the manager assigns tasks, workers do not choose
- No shared state between workers — each worker operates independently
- No retry logic — failed workers surface errors upward (see Agent 59 for supervision)

## Scope
- Defines the manager role: task decomposition and result aggregation
- Defines the worker role: single-task execution with no knowledge of other workers
- Demonstrates clean separation between coordination and execution

## Key Lesson
In multi-agent systems, the entity that decides WHAT to do and WHO does it should be separate from the entities that actually DO it. The manager-worker split is the foundational pattern for all complex agent pipelines.

## Next Step
Once Agent 41 is complete, proceed to Agent 42.
