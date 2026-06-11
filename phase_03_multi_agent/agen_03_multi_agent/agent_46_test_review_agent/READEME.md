# Agent 46 — Test Review Agent

## Purpose
Reviews a set of generated test cases for quality, completeness, and correctness. Checks whether critical user paths are covered, whether edge cases are included, whether assertions are specific enough to catch real bugs, and whether test naming follows conventions. Returns a structured review report with a list of gaps and improvement recommendations.

## What This Agent Introduces
LLM-as-reviewer in a testing context: the agent applies test quality criteria to evaluate another agent's output (test cases from Agent 32 or Agent 43).

## How It Works
1. Receives a list of generated test cases (from Agent 32 or similar)
2. Loads test quality criteria from the test knowledge base (Agent 27)
3. Evaluates each test case against criteria: path coverage, edge case inclusion, assertion specificity, naming convention
4. Identifies missing test scenarios by comparing against a critical path checklist
5. Scores each test case on a quality rubric (1-5)
6. Returns a review report: per-test scores, identified gaps, recommended additions

## What It Is NOT
- No test execution — it reviews test definitions, not test runs
- No test generation — it identifies gaps but does not fill them
- No static analysis — it uses LLM judgment, not AST parsing
- No JIRA integration — returns a report, does not create tickets

## Scope
- Accepts up to 50 test cases per review
- Checks 4 quality dimensions: coverage, edge cases, assertions, naming
- Returns structured report with gap list and scores

## Key Lesson
Quality gates between agents are as important as quality gates in traditional CI pipelines. Inserting a review agent between generation and execution catches low-quality tests before they waste execution time or produce misleading results.

## Next Step
Once Agent 46 is complete, proceed to Agent 47.
