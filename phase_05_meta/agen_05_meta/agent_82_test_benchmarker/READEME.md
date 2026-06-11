# Agent 82 — Test Benchmarker

## Purpose
Agent 82 measures the performance of the test system itself — not whether tests pass or
fail, but how long they take, where the bottlenecks are, and whether the suite is getting
slower over time. A test suite that takes 45 minutes blocks developer flow more than slow
production code, because it sits in the critical path of every commit. This agent treats
the test infrastructure as software that has its own performance budget, regression risk,
and optimization opportunities.

## What This Agent Introduces
**Test infrastructure benchmarking** — the idea that the test system itself needs
performance measurement, baseline comparison, and regression alerting, just like the
production code it tests. This is distinct from Agent 81's quality measurement: quality
asks "are these tests any good?" and benchmarking asks "are these tests any fast?"

## How It Works
1. Run the test suite with timing hooks enabled (pytest-json-report plugin) to collect
   per-test and per-category duration data.
2. Collect per-test durations grouped by test type (unit, integration, e2e, smoke).
3. Compute statistical distributions per category: p50 (median), p95, and p99 durations.
4. Load the previous benchmark baseline from a stored JSON file (if one exists).
5. Compute regression delta — percentage change in p95 per category versus baseline.
6. Identify the top 10 slowest individual tests as primary bottleneck candidates.
7. Emit a structured benchmark report with narrative and regression alerts.

## What It Is NOT
- Not a test quality evaluator — it measures speed, not correctness or coverage.
- Not a flakiness detector — timing variance alone does not indicate flakiness.
- Not a code profiler — it does not analyse production code execution paths.
- Not a real-time monitor — it operates on completed test run output, not live streams.
- Not a test runner — it consumes pytest output, it does not trigger test execution.

## Scope
- Reads: pytest-json-report output (JSON), previous benchmark baseline (JSON, optional),
  parallel worker configuration (YAML), test category definitions.
- Writes: `benchmark.json` (structured timing data + deltas), `benchmark_report.md`
  (human-readable narrative with tables and regression alerts).
- Understands: pytest timing conventions, xdist parallel runner configurations,
  p50/p95/p99 statistical distributions applied to test durations.
- Does NOT touch: test files, source code, CI pipeline configs, or coverage data.

## Key Lesson
Test suites are software — they have performance budgets. A suite that takes 45 minutes
to run blocks developer flow more than slow production code ever could, because it is in
the critical path of every single commit. The key insight of this agent is that you need
a baseline to detect regression: a single run telling you "tests take 12 minutes" is
meaningless. The same number compared against "tests took 8 minutes last week" surfaces
a 50% regression that someone needs to investigate immediately.

## Next Step
Once Agent 82 is complete, proceed to Agent 83.
