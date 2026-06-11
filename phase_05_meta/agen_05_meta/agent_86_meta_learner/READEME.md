# Agent 86 — Meta-Learner

## Purpose
Agent 86 closes the improvement loop on the entire agent system. It reads historical
performance data — scores, output quality ratings, prompt versions, tool success rates
— and uses that data to identify which patterns led to the best results. It then generates
concrete improvement suggestions: use this prompt variant, increase this timeout, skip this
tool call. The goal is continuous, data-driven improvement of the agent system itself.

## What This Agent Introduces
Feedback loops in AI systems — the idea that an agent system should monitor its own
performance and generate improvements, not just execute tasks. This is the foundation
of self-improving systems.

## How It Works
1. Load historical run data from the performance log store (JSON/ChromaDB).
2. Group runs by agent, prompt version, and tool configuration.
3. Compute performance statistics per group: mean quality score, success rate, latency.
4. Identify top-performing configurations and failing patterns.
5. Use LLM to reason about why certain configurations outperform others.
6. Generate ranked list of improvement suggestions with supporting evidence.
7. Optionally auto-apply safe improvements (e.g., prompt wording tweaks).
8. Write improvement report and updated configuration recommendations.

## What It Is NOT
- No real-time monitoring — works on historical batch data, not live streams.
- No automatic retraining — does not fine-tune models.
- No A/B testing framework — identifies patterns from existing data, does not run experiments.
- No production deployment — suggests changes, does not push them.

## Scope
- Reads: run_history.json or ChromaDB collection of agent runs.
- Writes: improvement_report.md, recommended_config.yaml.

## Key Lesson
Every agent system produces data as a side effect of running. The difference between a
good system and a great system is whether that data is used to improve the next run.
Feedback loops are what separate naive automation from adaptive intelligence.

## Next Step
Once Agent 86 is complete, proceed to Agent 87.
