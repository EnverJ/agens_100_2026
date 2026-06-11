Agent 15 — Self Critic Architecture

┌──────────────────────────────────────────────────────┐
│                       Inputs                          │
│  agent_output: { dict from previous agent }          │
│  reflection_report: { from Agent 14 }                │
└───────────────────┬──────────────────────────────────┘
                    │
          ┌─────────▼───────────────┐
          │      Scoring Rubric     │
          │  score = 100            │
          │  ┌─────────────────────┐│
          │  │ Rule 1: Non-empty   ││  -25 pts if fail
          │  │ Rule 2: Min length  ││  -20 pts if fail
          │  │ Rule 3: Req fields  ││  -25 pts if fail
          │  │ Rule 4: No anomalies││  -15 pts per flag
          │  │ Rule 5: Correct type││  -15 pts if fail
          │  └─────────────────────┘│
          └─────────┬───────────────┘
                    │
          ┌─────────▼───────────────┐
          │   Threshold Check       │
          │   score >= 70 → PASS    │
          │   score <  70 → FAIL    │
          └─────────┬───────────────┘
                    │
          ┌─────────▼────────────────────────────────┐
          │              Critique Object             │
          │  {                                      │
          │    score: int (0–100),                  │
          │    passed: bool,                        │
          │    violations: ["Rule 2 failed: ...",   │
          │                 "Rule 4: anomaly X"],   │
          │    threshold: 70                        │
          │  }                                      │
          └─────────────────────────────────────────┘
