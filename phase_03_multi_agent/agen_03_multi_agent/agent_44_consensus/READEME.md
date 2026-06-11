# Agent 44 — Consensus

## Purpose

Sends the same question or decision prompt to N independent agent instances and determines the final answer by majority vote. When a single agent answers a question, its error rate is whatever the model's accuracy is for that type of question. When three independent agents answer the same question, the probability that a majority of them give the wrong answer is dramatically lower — the errors must coincide. This agent reduces single-agent error rates by requiring agreement between multiple independent judgments before accepting an answer.

## What This Agent Introduces

Majority voting across independent agent calls as a reliability mechanism — the ensemble pattern applied to LLM agents. This is the same principle as ensemble models in machine learning: multiple independent predictors that each make errors, combined so that individual errors cancel out in the vote.

## How It Works

1. Receives a question or task requiring a discrete decision (yes/no, category, value, choice from set)
2. Calls N agent instances with the same prompt — each instance is independent with no shared context (N is configurable, default 3)
3. Collects all N responses
4. Parses each response to extract the structured answer (the discrete value being voted on)
5. Tallies votes for each distinct answer that appeared in the responses
6. Returns the answer with the most votes as the consensus result
7. Includes the full vote breakdown and a confidence score (winning votes / total votes) in the output

## What It Is NOT

- No debate — agents do not see each other's answers; each agent answers independently before any results are collected
- No weighted voting — every agent instance counts equally regardless of expressed confidence
- No explanation synthesis — the output is the winning answer, not a merged or synthesized explanation of why that answer is correct
- No guarantee of correctness — consensus reduces error rates but does not eliminate them; all agents can agree on a wrong answer

## Scope

- Calls 3 or 5 agent instances (odd number to prevent ties)
- Parses each response to extract a single discrete answer value
- Returns the majority answer with vote counts and confidence score
- Handles ties by falling back to the first-in-order answer if N is even (not recommended)

## Key Lesson

Independent repetition combined with voting is one of the simplest and most effective reliability improvements available in multi-agent systems. When a single agent is wrong 20% of the time on a given question type, three independent agents are all wrong simultaneously only 0.8% of the time (0.2 × 0.2 × 0.2). The reliability gain is large and the cost is exactly N times the single-agent cost — a straightforward engineering trade-off.

## Next Step

Once Agent 44 is complete, proceed to Agent 45.
