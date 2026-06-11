# Agent 17 — input_router

## Purpose
Agent 17 examines the current context object — specifically the flags set by earlier agents — and returns the ID of the next agent the pipeline should execute. It makes routing decisions deterministically: no probability, no reasoning, no LLM call. The right path is determined entirely by the flag values present in the context.

## What This Agent Introduces
**Deterministic conditional routing** — the concept of a pipeline component that decides which agent runs next based on structured state, without any intelligence or ambiguity.

## How It Works
1. Receive the context object built by Agent 11.
2. Read the `memory_flag` and `tool_flag` values from the context.
3. Apply an if/elif decision tree:
   - memory_flag=True, tool_flag=False → route to Agent 13 (long-term memory)
   - memory_flag=False, tool_flag=True → route to Agent 04/05 (tool execution)
   - memory_flag=True, tool_flag=True → route to Agent 11 (rebuild context with both)
   - memory_flag=False, tool_flag=False → route to Agent 01 (direct prompt)
4. Return the next agent ID as a string.

## What It Is NOT
- No tool execution
- No memory reads or writes
- No modification of the context object
- No reasoning about ambiguous or missing flags
- No probabilistic routing

## Scope
- Reading flag values from the context object
- Applying a fixed if/elif routing decision tree
- Returning the next agent ID string
- Logging the routing decision (optional)

## Key Lesson
Routing does not require intelligence — it requires clarity. Deterministic routing based on explicit flags is fast, testable, and completely transparent. Every routing decision can be explained with a single if/elif branch.

## Next Step
Once Agent 17 is complete, the project proceeds to Agent 18 — Requirement to Test Case Agent, the first SDET-specific agent in the project.
