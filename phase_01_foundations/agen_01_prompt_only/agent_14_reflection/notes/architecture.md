Agent 14 — Reflection Architecture

┌──────────────────────────────────────────────────────────┐
│                        Inputs                            │
│   context: { user_input, flags, session_id, ... }        │
│   agent_output: { any dict or string from prev agent }   │
└──────────────────┬───────────────────────────────────────┘
                   │
         ┌─────────▼──────────────┐
         │    Evaluation Checks   │
         │  ┌────────────────────┐│
         │  │ 1. Non-empty?      ││
         │  │ 2. Correct type?   ││
         │  │ 3. Required fields?││
         │  │ 4. Input/output    ││
         │  │    consistency?    ││
         │  └────────────────────┘│
         └─────────┬──────────────┘
                   │
         ┌─────────▼──────────────┐
         │   Anomaly Accumulator  │
         │  anomalies = []        │
         │  checks_passed = N     │
         └─────────┬──────────────┘
                   │
         ┌─────────▼──────────────────────────────────┐
         │              Reflection Report              │
         │  {                                         │
         │    has_errors: bool,                       │
         │    anomalies: ["missing field X", ...],    │
         │    health_score: float (0.0–1.0),          │
         │    checks_run: int,                        │
         │    checks_passed: int                      │
         │  }                                         │
         └────────────────────────────────────────────┘

NOTE: No writes, no routing, no LLM call. Pure evaluation logic.
