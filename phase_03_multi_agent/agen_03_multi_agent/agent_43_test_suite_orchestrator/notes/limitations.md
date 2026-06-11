# Limitations — Agent 43: Test Suite Orchestrator

This agent does NOT:

- Run test groups in parallel — all test groups execute sequentially; the unit test agent is not called until the smoke test agent has returned its result. For parallel test execution across groups, see Agent 53.
- Generate test cases — the agent consumes a test plan that must be provided as input. It does not generate test cases from requirements, user stories, or code. For test case generation, see Agent 32.
- Connect to real CI systems — there is no integration with GitHub Actions, Jenkins, CircleCI, or any CI/CD platform. The orchestration is self-contained; it does not trigger external pipelines or receive webhooks.
- Handle flaky test retry — if a test execution agent returns intermittent failures (tests that fail on first run but would pass on retry), the orchestrator has no retry logic. Each test group is called exactly once. Retry logic would need to be implemented either in the test execution agents or in a wrapper layer.
- Interact with Selenium, Appium, or any test framework directly — all actual test execution is delegated to test execution agents. The orchestrator only manages sequencing, abort logic, and result collection.
- Produce the final report itself — report generation is delegated to the report generator agent. The orchestrator passes collected results to the report agent and returns whatever the report agent produces; it does not format or generate the report content.
