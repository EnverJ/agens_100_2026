# Agent 42 — Orchestrator

## Purpose

An orchestrator is an agent that knows the full pipeline. It calls agents in sequence, passing each agent's output as the input to the next. The orchestrator is the only part of the system that has the full picture: it knows which agents exist, what order they run in, and what data flows between them. The agents inside the pipeline are deliberately kept blind — they receive an input, do their job, and return an output, with no knowledge of what came before or after them.

This design keeps pipeline agents simple, reusable, and testable in isolation. The orchestrator absorbs all the coordination complexity so that individual agents do not have to.

## What This Agent Introduces

Linear pipeline orchestration: sequential agent chaining where each agent's output feeds the next. This is the foundation of multi-step agent workflows.

## How It Works

1. Orchestrator receives a top-level goal from the caller
2. Calls Agent A with the initial input
3. Takes Agent A's output and passes it as input to Agent B
4. Takes Agent B's output and passes it as input to Agent C
5. Continues until all pipeline stages complete
6. Returns the final stage's output as the result

## What It Is NOT

- No branching — the pipeline is linear; there is no conditional routing based on intermediate results
- No parallelism — all stages run in sequence, one at a time
- No agent awareness — pipeline agents do not know they are part of a pipeline; they see only their own input
- No shared state — agents cannot read or write to a shared memory store; data flows only through explicit input/output passing

## Scope

- Defines a 3-stage pipeline (configurable to more stages)
- Each stage is a distinct agent call with its own structured input and output format
- The orchestrator automatically passes each stage's output as the next stage's input
- No manual data wiring is needed between stages after initial configuration

## Key Lesson

The orchestrator centralizes all knowledge of the pipeline. Individual agents stay simple — they solve one problem, return one result, and know nothing about the context in which they are being used. This separation makes it easy to swap one pipeline agent for another, add new stages, or test individual stages independently.

## Next Step

Once Agent 42 is complete, proceed to Agent 43.
