# Agent 43 — Test Suite Orchestrator

## Purpose

The Test Suite Orchestrator manages the full lifecycle of a test suite run as a sequence of agent calls. It receives a structured test plan, dispatches each test group to the appropriate test execution agent in order, collects pass/fail results from each group, applies abort-on-critical-failure logic, and hands off all collected results to a report generation agent. The orchestrator models what a CI/CD pipeline does — but in agent form: each stage is observable, replaceable, and auditable as an independent agent call.

## What This Agent Introduces

Agent-native CI/CD pipeline — each stage of a test run (parsing, execution per group, reporting) is an agent call orchestrated in sequence. This agent demonstrates that CI/CD pipeline logic — stage progression, abort conditions, result collection — can be expressed as an orchestration problem rather than a shell script or YAML configuration.

## How It Works

1. Receives a test plan (structured dict with test groups and metadata)
2. Parses the test plan to extract test groups and their execution order
3. Calls the appropriate test execution agent for each test group in sequence
4. Collects pass/fail/skip results from each agent call
5. After each critical test group (e.g., smoke tests), checks whether to abort or continue
6. If a critical group fails and abort-on-critical-failure is enabled, stops execution and skips remaining groups
7. Hands off all collected results to the report generation agent
8. Returns a summary with total pass/fail/skip counts and a reference to the generated report

## What It Is NOT

- No parallel test execution — all test groups run sequentially (see Agent 53 for parallel test running)
- No test case generation — uses pre-written test plans; does not generate test cases from requirements
- No direct test execution — delegates actual test execution to specialized test execution agents; does not call Selenium, Appium, or any test framework directly
- No JIRA integration — bug filing and issue tracking are delegated to Agent 49

## Scope

- Orchestrates 3-5 test groups in a single suite run
- Executes test groups sequentially in the order specified by the test plan
- Applies abort-on-critical-failure logic after designated critical groups
- Passes all collected results to a report generation agent as a single handoff

## Key Lesson

A CI/CD pipeline is an orchestration problem. When each pipeline stage is an agent, the pipeline becomes observable (you can inspect each agent's input and output), auditable (the full execution trace is preserved), and replaceable (swapping the unit test agent for a different one requires changing only the orchestrator's dispatch logic, not the pipeline structure). Agent-native pipelines are more flexible than YAML-configured pipelines because the orchestration logic is code, not configuration.

## Next Step

Once Agent 43 is complete, proceed to Agent 44.
