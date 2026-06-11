# Agent 24 — Test History Memory

## Purpose
Agent 24 provides per-test-case memory. Where Agent 23 stores suite-level run summaries, this agent stores individual test outcomes — one memory entry per test execution. Given a test name, it can retrieve the full history of that test's outcomes: when it passed, when it failed, what error appeared, and how long it took. This enables agents to reason about individual test trends rather than suite-level aggregates.

## What This Agent Introduces
Per-test-case memory with keyed retrieval — storing individual test outcomes so that downstream agents can answer "what happened last time this specific test ran?"

## How It Works
1. On each test execution, the agent receives a single test result: test name, outcome (pass/fail/skip), error message (if any), duration, and run timestamp.
2. The result is embedded as text and stored in ChromaDB with test_name as a metadata key for filtering.
3. On a QUERY call, the agent filters ChromaDB by test_name and retrieves the N most recent outcomes, ordered by recency.
4. The response includes outcome history, failure rate, and the most recent error message if applicable.

## What It Is NOT
- No suite-level aggregation — this is per-test storage only
- No real-time test runner — it stores outcomes, it does not execute tests
- No diff analysis — it does not compare current results to past results automatically
- No flakiness scoring — scoring is left to Agent 37

## Scope
- Store individual test execution outcomes with test_name metadata
- Retrieve outcome history for a named test
- Support filtering by test_name using ChromaDB metadata filters
- Return ordered outcome history with recency context

## Key Lesson
Individual test history is the foundation of trend awareness. Knowing that test_checkout_flow has failed 3 of the last 5 runs requires per-test, not per-suite, memory storage.

## Next Step
Once Agent 24 is complete, proceed to Agent 25.
