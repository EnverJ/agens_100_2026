# Agent 81 — Test Suite Evaluator

## Purpose
Agent 81 evaluates the overall quality of a test suite, moving beyond simple pass/fail
results to answer a deeper question: are your tests actually any good? It scans a test
directory, collects structural and coverage metrics, and produces a scorecard that tells
you where your testing investment is healthy and where it is dangerously thin. The goal
is to surface institutional blind spots before production does.

## What This Agent Introduces
**Test suite quality metrics** — the discipline of measuring tests themselves, not just
the code they cover. Passing tests are necessary but not sufficient; a suite full of
trivial happy-path checks gives false confidence. This agent makes suite quality
objectively measurable for the first time in the project.

## How It Works
1. Accept a path to a test directory and an optional coverage report (JSON or XML).
2. Walk the directory tree, cataloguing every test file and counting test functions.
3. Parse pytest markers (`@pytest.mark.skip`, `xfail`, `parametrize`) and assertion counts.
4. Compute six metrics: coverage %, tests per feature area, happy-path to negative
   test ratio, age of the oldest test (git blame), count of skipped tests, and average
   assertions per test function.
5. Weight each metric against configurable thresholds to produce a 0–100 quality score.
6. Identify the three weakest dimensions and generate specific, actionable recommendations.
7. Emit a structured scorecard in JSON and a human-readable summary in Markdown.

## What It Is NOT
- No test execution — it reads and analyses, never runs tests.
- No code coverage instrumentation — it consumes existing coverage reports, does not
  produce them.
- No per-test deep analysis — it works at the suite level, not the individual test level.
- No CI gate — it reports quality; enforcing thresholds is left to the calling pipeline.
- No mutation testing — it does not inject faults to verify test sensitivity.

## Scope
- Reads: test directory file tree, pytest markers, coverage JSON/XML, test function
  signatures, git log for file age.
- Writes: `scorecard.json`, `scorecard_summary.md`.
- Understands: pytest, Jest, JUnit naming conventions for skips, parametrize, and
  assertions.
- Does NOT touch: production source code, CI configs, or test data files.

## Key Lesson
Coverage percentage tells you what fraction of code is touched by tests. Test suite
quality tells you whether those tests would actually catch a bug. Both numbers are
necessary; neither alone is sufficient. A 90% coverage score with all happy-path tests
is more dangerous than 60% coverage with rigorous negative and edge-case tests, because
it creates false confidence.

## Next Step
Once Agent 81 is complete, proceed to Agent 82.
