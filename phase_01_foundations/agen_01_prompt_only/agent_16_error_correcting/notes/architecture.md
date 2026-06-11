Agent 16 — Error Correcting Architecture

┌──────────────────────────────────────────────────────────┐
│                         Inputs                           │
│  critique: { score, passed, violations: [str], ... }    │
│  reflection_report: { anomalies: [str], ... }           │
└──────────────────────┬───────────────────────────────────┘
                       │
             ┌─────────▼──────────────┐
             │   Violation Iterator   │
             │  for v in violations   │
             │  for a in anomalies    │
             └─────────┬──────────────┘
                       │
             ┌─────────▼──────────────────────────────────┐
             │          Fix Template Lookup               │
             │                                            │
             │  "Rule 2: too short"   → "Expand prompt"  │
             │  "Rule 3: field miss"  → "Check schema"   │
             │  "anomaly: null field" → "Add fallback"   │
             │  "Rule 4: anomaly X"   → "Retry step N"   │
             └─────────┬──────────────────────────────────┘
                       │
             ┌─────────▼──────────────┐
             │   Priority Sorter      │
             │  sort by severity      │
             │  (point deduction)     │
             └─────────┬──────────────┘
                       │
             ┌─────────▼──────────────────────────────────────┐
             │             Suggestion List                     │
             │  [                                             │
             │    { error_code: "R2",                        │
             │      description: "Output too short",         │
             │      suggested_fix: "Expand prompt to ..." }, │
             │    { error_code: "A1",                        │
             │      description: "Missing field: result",    │
             │      suggested_fix: "Add fallback default" }  │
             │  ]                                             │
             └────────────────────────────────────────────────┘

No LLM call. No writes. No routing. Pure lookup + assembly.
