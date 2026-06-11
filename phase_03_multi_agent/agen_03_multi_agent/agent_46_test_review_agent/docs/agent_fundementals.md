# Agent Fundamentals — Agent 46: Test Review Agent

## What This Agent IS

- **Test quality reviewer**: applies a structured rubric to evaluate generated test cases
- **Gap detector**: identifies missing critical paths, absent edge cases, and weak assertions
- **Scoring agent**: produces a numeric quality score (1-5) per test case and per dimension
- **Structured reporter**: outputs a machine-readable review report with scores, gaps, and recommendations
- **Knowledge base consumer**: pulls quality criteria from Agent 27 at runtime, not hardcoded

## What This Agent IS NOT

- **Not a test executor**: does not run tests, does not connect to a test runner, does not produce pass/fail results
- **Not a test generator**: identifies gaps but does not fill them — gap remediation is handled by Agent 32
- **Not a static code analyzer**: does not parse AST, does not lint code, does not check syntax — reviews test descriptions using LLM judgment
- **Not a CI/CD integration**: does not push results to a pipeline, does not block deployments, does not post to GitHub Actions

## Inputs

```python
test_cases: list[dict]
# Each dict contains:
# {
#   test_name: str,
#   description: str,
#   preconditions: list[str],
#   steps: list[str],
#   expected_result: str,
#   assertions: list[str]
# }
# Max 50 test cases per invocation

quality_criteria: dict  # loaded from Agent 27 knowledge base
# Contains:
# {
#   critical_paths: list[str],
#   required_edge_case_categories: list[str],
#   assertion_specificity_standards: str,
#   naming_conventions: str
# }
```

## Outputs

```python
review_report: dict
# {
#   per_test_scores: [
#     {
#       test_name: str,
#       coverage_score: int,      # 1-5
#       edge_case_score: int,     # 1-5
#       assertion_score: int,     # 1-5
#       naming_score: int,        # 1-5
#       notes: str
#     }
#   ],
#   gaps: list[str],             # missing critical paths or edge cases
#   recommendations: list[str],  # suggested additional test cases
#   overall_quality_score: float # mean of all per-test dimension scores
# }
```

## Quality Dimensions

| Dimension | What Is Checked |
|---|---|
| Path Coverage | Does the test cover a documented critical user path? |
| Edge Cases | Does the test include boundary values, nulls, or failure inputs? |
| Assertion Specificity | Are assertions precise enough to catch real bugs (not just "assert response exists")? |
| Naming Convention | Does the test name follow the project's naming standard? |
