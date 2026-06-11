# Agent 15 — self_critic

## Purpose
Agent 15 scores and critiques outputs against a defined quality rubric. It reads the output of a previous agent alongside the reflection report from Agent 14, then assigns a numeric quality score and a set of quality flags. The score and flags tell downstream agents whether to proceed, retry, or escalate — without the self-critic modifying anything itself.

## What This Agent Introduces
**Quality scoring** — the concept of measuring output quality against explicit rules, producing a numeric score that drives decisions elsewhere in the pipeline.

## How It Works
1. Receive the agent output and the reflection report from Agent 14.
2. Apply a scoring rubric: check completeness (required fields present?), clarity (output is a non-empty, coherent structure?), scope (output matches the agent's expected type?), and error count (how many anomalies did Agent 14 flag?).
3. Assign point deductions per failed rule.
4. Compute a final score from 0–100.
5. Set a pass/fail flag based on a configurable threshold (default: 70).
6. Return a critique dict with: score, pass/fail flag, and a list of rule violations.

## What It Is NOT
- No modification of the output being critiqued
- No routing decisions
- No memory storage
- No tool execution
- No intelligent understanding of content semantics

## Scope
- Rule-based quality checks against a fixed rubric
- Numeric scoring from 0–100
- Pass/fail threshold comparison
- Returning a structured critique object for downstream agents

## Key Lesson
Quality gates require explicit criteria. By making the rubric visible and rule-based, the self-critic keeps quality decisions auditable: you can always trace why a score was assigned and which rule caused a failure.

## Next Step
Once Agent 15 is complete, the project proceeds to Agent 16 — Error Correcting, which reads the critique and generates actionable fix suggestions.
