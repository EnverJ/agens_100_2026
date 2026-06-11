# Architecture — Agent 81: Test Suite Evaluator

```
INPUT
  test_dir/          (path to test directory)
  coverage.json      (optional: from pytest-cov or Istanbul)
  git log            (for file age via git blame)
  config.yaml        (optional: metric weights, thresholds)
       |
       v
+------------------+
|  FILE WALKER     |  Recursively discovers test files
|  & PARSER        |  Parses markers, assertions, function names
+------------------+
       |
       v
+---------------------------+
|  METRIC CALCULATOR        |
|  1. coverage %            |  from coverage.json
|  2. tests per feature     |  from directory structure + naming
|  3. happy/negative ratio  |  from function name patterns + markers
|  4. age of oldest test    |  from git blame timestamps
|  5. skipped test count    |  from @pytest.mark.skip / xfail
|  6. assertions per test   |  from AST assertion node count
+---------------------------+
       |
       v
+------------------+
|  WEIGHTED SCORER |  Applies ScoringConfig weights → 0–100 score
|                  |  Identifies 3 weakest metric dimensions
+------------------+
       |
       v
+----------------------------+
|  LLM RECOMMENDATION ENGINE |  Receives score breakdown + weak dims
|                             |  Produces 3 specific, actionable items
|                             |  temperature=0, JSON output enforced
+----------------------------+
       |
       v
OUTPUT
  scorecard.json         (structured: scores, metrics, recommendations)
  scorecard_summary.md   (human-readable narrative + tables)
```
