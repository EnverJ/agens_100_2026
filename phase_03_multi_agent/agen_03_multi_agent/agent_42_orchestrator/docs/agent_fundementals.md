# Agent Fundamentals — Agent 42: Orchestrator

## What This Agent IS

- A pipeline coordinator that calls agents in a fixed sequence
- The sole holder of pipeline knowledge — it knows which agents exist, in what order, and what data flows between them
- A handoff manager that translates the output of one stage into the input of the next
- A single entry point for multi-stage workflows — callers interact with the orchestrator, not with individual pipeline agents
- A composable unit itself — an orchestrator can be a stage inside a larger orchestrator

## What This Agent IS NOT

- Not a fan-out coordinator — it does not call multiple agents with the same input and collect results (that is the manager-worker pattern from Agent 41)
- Not a decision maker — it does not branch or route based on intermediate results; the pipeline is fixed
- Not a retry handler — if a stage fails, the orchestrator does not have fallback logic
- Not a parallel executor — stages run sequentially, one at a time
- Not aware of what the pipeline agents know about each other — it assumes they are stateless and isolated

## Input

```
{
  "goal": str   # The top-level task or input data for the first pipeline stage
}
```

## Output

```
{
  "result": str | dict   # The output of the final pipeline stage
}
```

## Data Flow Contract

Each stage must produce output in a format the next stage can consume. The orchestrator is responsible for ensuring this contract is met — either by designing compatible agent prompts or by transforming data between stages.
