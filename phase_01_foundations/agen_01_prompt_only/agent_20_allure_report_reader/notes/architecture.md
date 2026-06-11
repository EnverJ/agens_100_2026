Agent 20 — Allure Report Reader Architecture

┌──────────────────────────────────────────────────────────┐
│                        Input                             │
│   report_path: str  (path to allure-results/*.json)     │
│   OR                                                     │
│   json_string: str  (raw JSON content)                   │
└──────────────────────────┬───────────────────────────────┘
                           │
               ┌───────────▼────────────────┐
               │       JSON Loader          │
               │  json.load(file) or        │
               │  json.loads(string)        │
               └───────────┬────────────────┘
                           │
               ┌───────────▼────────────────────────────┐
               │         Result Iterator                │
               │  for test in results["testResults"]    │
               │    accumulate by status                │
               │    if status in (failed, broken):      │
               │      extract name + statusDetails.msg  │
               └───────────┬────────────────────────────┘
                           │
               ┌───────────▼────────────────┐
               │     Counter Aggregator     │
               │  total = len(results)      │
               │  passed = count(passed)    │
               │  failed = count(failed)    │
               │  broken = count(broken)    │
               │  skipped = count(skipped)  │
               └───────────┬────────────────┘
                           │
               ┌───────────▼──────────────────────────────────┐
               │              Summary Dict                    │
               │  {                                          │
               │    total: 142,                              │
               │    passed: 118,                             │
               │    failed: 17,                              │
               │    broken: 4,                               │
               │    skipped: 3,                              │
               │    failures: [                              │
               │      { name: "test_login_empty_password",   │
               │        error: "AssertionError: expected 400 │
               │                got 200" },                  │
               │      ...                                    │
               │    ]                                        │
               │  }                                          │
               └──────────────────────────────────────────────┘

No LLM call. No writes. Read-only JSON parsing only.
