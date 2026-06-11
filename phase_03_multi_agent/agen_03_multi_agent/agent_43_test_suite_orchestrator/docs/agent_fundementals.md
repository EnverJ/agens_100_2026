# Agent Fundamentals — Agent 43: Test Suite Orchestrator

## What This Agent IS

- A test suite coordinator that manages the full sequence of a test run as agent calls
- A pipeline stage manager that determines which test execution agent to call for each test group and in what order
- An abort-on-failure decider that evaluates critical test group results and decides whether to continue or halt the suite
- A result collector that accumulates pass/fail/skip counts from all test execution agents before handing off to reporting
- A handoff coordinator that passes all collected results to the report generation agent as a single structured payload

## What This Agent IS NOT

- Not a test case executor — it does not run test cases directly; it delegates execution to specialized test execution agents
- Not a test case generator — it consumes a pre-written test plan; it does not generate test cases from requirements or specifications
- Not a JIRA reporter — bug filing, issue creation, and defect tracking are out of scope; see Agent 49 for JIRA integration
- Not a parallel test runner — all test groups run sequentially; see Agent 53 for parallel test execution
- Not a test framework wrapper — it does not call Selenium, Appium, pytest, or any test framework directly

## Input

```python
test_plan: dict = {
    "suite_name": str,
    "abort_on_critical_failure": bool,
    "groups": [
        {
            "id": str,
            "name": str,
            "type": str,          # "smoke" | "unit" | "integration" | "e2e"
            "is_critical": bool,
            "test_cases": list[dict]
        }
    ]
}
```

## Output

```python
suite_result: dict = {
    "suite_name": str,
    "total": int,
    "passed": int,
    "failed": int,
    "skipped": int,
    "aborted": bool,
    "abort_reason": str | None,
    "report_url": str
}
```
