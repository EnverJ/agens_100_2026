# Agent 19 — test_output_validator

## Purpose
Agent 19 is the assertion engine. Given an actual output from a test run (an API response, a UI assertion result, or a generated test case) and an expected value or schema, it determines PASS or FAIL with a specific reason. This is the SDET equivalent of Agent 08 (Validator Gatekeeper) applied to test results rather than user input. It makes validation a reusable service that any agent in the pipeline can call.

## What This Agent Introduces
**Validation-as-a-service for test results** — a dedicated, reusable assertion module that any part of the pipeline can invoke to check whether an actual result meets an expectation.

## How It Works
1. Receive an actual output (dict or string) and an expected schema or value.
2. Determine validation mode: value comparison (exact match) or schema validation (field presence and type checking).
3. For value mode: compare actual to expected directly; note every field that differs.
4. For schema mode: check that every required field in the schema is present in actual and has the correct type.
5. Return a validation result: {status: "PASS"|"FAIL", reason: str, diff: dict}.

## What It Is NOT
- No test execution
- No bug logging or ticket creation
- No memory of previous validation runs
- No routing based on PASS/FAIL result
- No tolerance for partial matches

## Scope
- Exact value comparison between actual and expected
- Schema validation (field presence + type checking)
- Structured PASS/FAIL result with diff detail
- Reusable by any agent that needs to assert an output

## Key Lesson
Every test is ultimately an assertion. By making the assertion engine a standalone agent, the project demonstrates that validation logic should be centralized, not duplicated across every test. One assertion module, used everywhere.

## Next Step
Once Agent 19 is complete, the project proceeds to Agent 20 — Allure Report Reader, which parses test run reports to extract structured summaries.
