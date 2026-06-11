Agent 19 — Test Output Validator Architecture

┌───────────────────────────────────────────────────────┐
│                       Inputs                          │
│  actual: dict | str   (what the system produced)     │
│  expected: dict | str (value) or schema dict          │
│  mode: "value" | "schema"                            │
└───────────────────────┬───────────────────────────────┘
                        │
              ┌─────────▼──────────────────┐
              │      Mode Dispatcher       │
              │   "value"  │  "schema"     │
              └────┬───────┴────┬──────────┘
                   │            │
        ┌──────────▼──┐    ┌────▼──────────────────┐
        │   Exact     │    │   Schema Check         │
        │  Comparison │    │  for each field in     │
        │  actual ==  │    │  schema:               │
        │  expected?  │    │   - field present?     │
        │             │    │   - correct type?      │
        └──────┬──────┘    └────┬──────────────────┘
               │               │
        ┌──────▼──────┐    ┌────▼──────────────────┐
        │  Diff Builder│   │  Missing / Type Errors │
        │  note every  │   │  accumulated as list   │
        │  mismatch    │   └────┬──────────────────┘
        └──────┬──────┘         │
               └───────┬────────┘
                        │
              ┌─────────▼──────────────────────────────┐
              │          Validation Result              │
              │  {                                     │
              │    status: "PASS" | "FAIL",            │
              │    reason: "field status_code: ...",   │
              │    diff: { expected: X, actual: Y }    │
              │  }                                     │
              └────────────────────────────────────────┘

No LLM call. No state. No side effects. Pure comparison logic.
