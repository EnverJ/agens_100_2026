# Agent Fundamentals — Agent 81: Test Suite Evaluator

## IS / IS NOT

**IS:**
- A static analysis agent for test suite quality measurement
- A weighted scoring engine that produces a 0–100 quality score
- A recommendation generator that identifies the three weakest suite dimensions
- A coverage report consumer (reads existing reports, does not produce them)
- A git-aware agent that uses commit history to determine test file age

**IS NOT:**
- Not a test runner or test executor
- Not a coverage instrumentation tool
- Not a per-test logic analyser (works at suite and file level only)
- Not a CI gate enforcer (reports only, does not block pipelines)
- Not a mutation testing tool
- Not a flakiness detector (requires multiple runs over time)

---

## Input

| Parameter       | Type          | Required | Description                                              |
|-----------------|---------------|----------|----------------------------------------------------------|
| `test_dir`      | `str` (path)  | Yes      | Root directory containing all test files                 |
| `coverage_file` | `str` (path)  | No       | Path to coverage.json or coverage.xml from pytest-cov   |
| `config_file`   | `str` (path)  | No       | YAML file with metric weights and thresholds             |
| `feature_areas` | `list[str]`   | No       | Named sub-directories representing feature domains       |

---

## Output

| File                   | Format   | Description                                                    |
|------------------------|----------|----------------------------------------------------------------|
| `scorecard.json`       | JSON     | Structured scores per metric, overall score, recommendations   |
| `scorecard_summary.md` | Markdown | Human-readable narrative, metric tables, top 3 action items    |
| `exit_code`            | int      | 0 = score above threshold, 1 = below threshold, 2 = error     |
