# Limitations — Agent 81: Test Suite Evaluator

This agent does NOT:

- Run any tests. It reads and analyses test files statically; actual test execution
  is out of scope. Passing or failing tests are invisible to this agent.
- Instrument code for coverage. It consumes an existing coverage report (JSON or XML).
  If no coverage file is provided, the coverage metric is skipped or scored as zero.
- Perform per-test deep analysis. It works at suite level and file level, not at the
  level of individual test logic or assertion correctness.
- Detect flaky tests. Flakiness requires multiple executions over time; this agent
  operates on a single static snapshot.
- Support all test frameworks equally. Primary support is pytest. Jest and JUnit
  naming conventions are partially recognised but not guaranteed.
- Understand test semantics. It classifies tests as "negative" based on name patterns
  (`test_invalid_*`, `test_raises_*`) not on logical analysis of what the test asserts.
- Enforce quality gates. It reports scores and recommendations but does not fail a
  build or block a merge. Gate enforcement belongs to the calling CI pipeline.
- Perform mutation testing. It cannot inject code faults to verify that tests would
  catch regressions; that requires a separate mutation testing tool (e.g., mutmut).
- Track quality trends over time. It produces a point-in-time scorecard. Historical
  trend analysis is handled by Agent 86 (meta-learner).
- Analyse test data fixtures or factories. Test files are parsed; conftest.py files
  and fixture definitions are catalogued but not scored.
