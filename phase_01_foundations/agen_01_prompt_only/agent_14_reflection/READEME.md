# Agent 14 — reflection

## Purpose
Agent 14 evaluates the outputs of other agents and the current system state to detect errors, anomalies, and inconsistencies. It produces a structured reflection report that describes what it found — without modifying anything. The agent acts as an internal observer: always watching, never intervening. This is the foundation on which self-improving systems are built.

## What This Agent Introduces
**Introspection** — the first agent in the project that looks at the system itself rather than processing user input. It introduces the concept of a system observing its own outputs.

## How It Works
1. Receive a context object and the output produced by a previous agent.
2. Apply a set of evaluation checks: is the output non-empty? does it match the expected type? are required fields present? are there obvious inconsistencies between input and output?
3. Assign an anomaly flag for each check that fails.
4. Compute an overall health score based on how many checks passed.
5. Return a structured reflection report dict containing: errors found, anomalies flagged, and health score.

## What It Is NOT
- No error correction or output modification
- No routing to other agents
- No memory storage
- No tool execution
- No reasoning about root cause

## Scope
- Structural validation of agent outputs (type, shape, required fields)
- Consistency checks between input context and output content
- Anomaly flagging with descriptive messages
- Producing a machine-readable reflection report

## Key Lesson
Before a system can improve itself, it must be able to observe itself. Reflection is a read-only operation by design: separating observation from intervention makes the system far easier to debug and reason about.

## Next Step
Once Agent 14 is complete, the project proceeds to Agent 15 — Self Critic, which applies quality scoring rules on top of the reflection report.
