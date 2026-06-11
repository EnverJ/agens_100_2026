# Concept — Agent 46: Test Review Agent

## Why Test Quality Review Is Needed

Automatically generated test cases are not automatically good test cases. Agents like Agent 32 (test plan generator) can produce large volumes of test cases quickly, but speed and volume do not equal quality. Generated tests tend to cover the happy path and obvious inputs while missing edge cases, boundary conditions, and failure modes that matter most in production. Without a review step, a test suite may appear comprehensive — 50 tests for a checkout flow — while leaving critical scenarios like concurrent session conflicts or payment processor timeouts completely untested. Inserting a review agent between generation and execution forces a quality gate that mirrors the code review step in traditional development.

## How LLM-as-Reviewer Works

The LLM-as-reviewer pattern treats the language model as an evaluator rather than a generator. The agent is given a rubric — a set of quality criteria — and a list of test cases, and its job is to apply the rubric to each test case and report scores and gaps. The quality criteria come from the test knowledge base (Agent 27), which encodes domain-specific standards: what constitutes a specific-enough assertion, which user paths are considered critical, and what naming conventions apply to the project. The LLM reads each test case definition and compares it against these criteria, producing a score from 1 to 5 per dimension and a list of identified gaps. This is a different cognitive task from generation — it requires comparison and judgment, not creativity.

## Why This Is a Different Task Than Test Generation

Test generation and test review require different prompts, different context, and different output structures. A generation prompt is open-ended: "Given this feature, write test cases covering all important scenarios." A review prompt is closed-ended: "Given this test case and this rubric, score it on these four dimensions and identify what is missing." The generation prompt rewards breadth and creativity. The review prompt rewards precision and adherence to criteria. Mixing these tasks into one agent would degrade both. Separating them into Agent 32 (generate) and Agent 46 (review) follows the single-responsibility principle for agents: each agent does one thing well.

## Connection to Other Agents

Agent 46 is downstream of Agent 32 (test plan generator), which produces the test cases that Agent 46 reviews. It also draws from Agent 27 (knowledge base agent), which provides the quality criteria used in the rubric. The output of Agent 46 — a review report with gaps and scores — can be fed back to Agent 32 to trigger a regeneration pass, or forwarded to Agent 49 (JIRA integration agent) to create tickets for identified coverage gaps. This creates a feedback loop: generate, review, identify gaps, generate again — a quality improvement cycle that mirrors how human SDET teams work.
