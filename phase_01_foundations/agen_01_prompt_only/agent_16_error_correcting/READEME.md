# Agent 16 — error_correcting

## Purpose
Agent 16 reads the critique from Agent 15 and the reflection report from Agent 14, then produces a list of actionable fix suggestions for each identified problem. It does not apply the fixes itself — it recommends. This deliberate boundary keeps the pipeline transparent: suggestions are visible and reviewable before any correction is applied.

## What This Agent Introduces
**Fix suggestion generation** — the concept of translating error flags into specific, actionable recommendations. This separates the act of identifying a problem from the act of solving it.

## How It Works
1. Receive the critique object from Agent 15 and the reflection report from Agent 14.
2. For each rule violation in the critique, look up the corresponding fix suggestion template.
3. For each anomaly in the reflection report, generate a targeted suggestion based on the anomaly description.
4. Combine all suggestions into a ranked list (ordered by severity/point deduction).
5. Return a structured output: list of { error_code, description, suggested_fix } objects.

## What It Is NOT
- No automatic application of fixes
- No routing to other agents
- No memory storage
- No tool execution
- No intelligent reasoning about root cause

## Scope
- Reading violation codes from the critique object
- Reading anomaly strings from the reflection report
- Mapping error codes to fix suggestion templates
- Returning a prioritized list of actionable suggestions

## Key Lesson
The system suggesting a fix and the system applying a fix are two different responsibilities. Keeping them separate means a human or a downstream agent can review and approve suggestions before anything is changed — which is essential for building trustworthy automated systems.

## Next Step
Once Agent 16 is complete, the project proceeds to Agent 17 — Input Router, which uses context flags to decide which agent handles the next step.
