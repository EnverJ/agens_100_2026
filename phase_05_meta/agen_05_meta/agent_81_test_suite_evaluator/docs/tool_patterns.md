# Tool Patterns — Agent 81: Test Suite Evaluator

- **Static AST Analysis (`ast` module).** Python's built-in `ast` module parses each
  test file into a syntax tree. The agent walks the tree to count `assert` statements,
  identify function names beginning with `test_`, detect `pytest.raises` context
  managers, and flag functions decorated with `@pytest.mark.skip` or `@pytest.mark.xfail`.
  This is more reliable than regex because it handles multi-line expressions and nested
  function definitions correctly.

- **Coverage Report Ingestion (`coverage.json`).** The agent reads the JSON output of
  `pytest --cov --cov-report=json`. It extracts the `totals.percent_covered` field and,
  when `feature_areas` are specified, correlates source file paths to feature areas to
  produce per-area coverage breakdowns. No coverage instrumentation is performed; the
  agent is a consumer, not a producer.

- **Weighted Scoring Model (`ScoringConfig` dataclass).** A `ScoringConfig` dataclass
  holds six weight values (one per metric) that sum to 1.0. Each metric is normalised
  to 0–100 before weighting. The dataclass can be instantiated from a YAML config file
  or from defaults. This pattern separates policy (how much does coverage matter?) from
  mechanism (how is coverage measured?), making the scorer configurable without code
  changes.

- **LLM-as-Advisor (not executor).** The LLM is called once, after all metrics are
  computed, and acts purely as a recommendation writer. It receives structured data and
  returns structured recommendations. It does not execute tools, does not read files,
  and does not call external APIs. This keeps the LLM role narrow and the output
  deterministic and auditable.

- **Git Blame for Test Age.** The agent runs `git log --follow --format=%ai -- <file>`
  for each test file and parses the earliest commit timestamp. The age of the oldest
  test file in the suite is used as a proxy for "stale test" risk. Files that have not
  been touched in over 18 months while the source code has changed significantly are
  flagged as high-risk legacy tests.
