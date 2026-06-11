Agent 18 — Requirement to Test Case Architecture

┌─────────────────────────────────────────────────────────┐
│                     Input                               │
│   requirement: str                                      │
│   e.g. "Users can filter restaurants by cuisine type.   │
│          Filters are multi-select. Results update       │
│          without page reload."                          │
└──────────────────────────┬──────────────────────────────┘
                           │
               ┌───────────▼───────────────┐
               │     Prompt Assembly       │
               │                           │
               │  system_prompt:           │
               │   "You are a senior SDET. │
               │    Generate test cases    │
               │    as JSON. Include       │
               │    happy path, edge       │
               │    cases, and negatives." │
               │                           │
               │  user_prompt:             │
               │   "Requirement: {req}"    │
               └───────────┬───────────────┘
                           │
               ┌───────────▼───────────────┐
               │       LLM Call            │
               │  (with JSON output mode)  │
               └───────────┬───────────────┘
                           │
               ┌───────────▼───────────────┐
               │     JSON Parser           │
               │  validate schema fields   │
               └───────────┬───────────────┘
                           │
               ┌───────────▼───────────────────────────────┐
               │           Test Case List                  │
               │  [                                        │
               │    { id: "TC-001",                        │
               │      title: "Valid cuisine filter",       │
               │      steps: ["Open app", "Tap filter",   │
               │              "Select Italian"],           │
               │      expected_result: "Only Italian       │
               │                        restaurants shown",│
               │      type: "happy_path" },                │
               │    { id: "TC-002", type: "edge_case",     │
               │      ... },                               │
               │    { id: "TC-003", type: "negative", ... }│
               │  ]                                        │
               └───────────────────────────────────────────┘
