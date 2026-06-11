# Architecture — Agent 82: Test Benchmarker

```
INPUT
  pytest_output.json      (from pytest-json-report plugin)
  previous_benchmark.json (optional: prior run baseline)
  parallel_config.yaml    (optional: xdist worker count, categories)
       |
       v
+----------------------+
|  TIMING COLLECTOR    |  Parses pytest-json-report output
|                      |  Extracts per-test duration + category label
|                      |  Groups tests by type: unit/integration/e2e/smoke
+----------------------+
       |
       v
+-------------------------------+
|  STATISTICAL AGGREGATOR       |
|  Per category computes:       |
|    p50 (median duration)      |
|    p95 (95th percentile)      |
|    p99 (99th percentile)      |
|    total duration             |
|    tests per minute           |
+-------------------------------+
       |
       v
+---------------------------+
|  BASELINE COMPARATOR      |  Loads previous_benchmark.json
|                           |  Computes delta % per category
|                           |  Flags categories with >10% regression
|                           |  Emits regression_alert: bool
+---------------------------+
       |
       v
+---------------------------+
|  BOTTLENECK IDENTIFIER    |  Ranks all tests by duration descending
|                           |  Selects top 10 slowest tests
|                           |  Computes % of total time consumed by top 10
+---------------------------+
       |
       v
+----------------------+
|  LLM REPORT WRITER   |  Receives: stats, deltas, bottleneck list
|                      |  Produces: natural language narrative
|                      |  Explains anomalies (why p95 >> p50)
|                      |  Generates 3 actionable speed recommendations
+----------------------+
       |
       v
OUTPUT
  benchmark.json        (structured: timings, deltas, bottlenecks, alert flag)
  benchmark_report.md   (human-readable: tables + narrative + recommendations)
```
