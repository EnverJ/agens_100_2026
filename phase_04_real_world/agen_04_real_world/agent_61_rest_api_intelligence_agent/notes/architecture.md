# Architecture: REST API Intelligence Agent

```
┌─────────────────────────────────────────────────────────────────┐
│                         CALLER / USER                           │
│  { url, method, headers, body, contract_description }           │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                    agent_61  (orchestrator)                      │
│                                                                 │
│  1. Validate inputs                                             │
│  2. Build request kwargs                                        │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                   requests.Session                              │
│                                                                 │
│   GET / POST / PUT / PATCH / DELETE  →  target API endpoint    │
│                                                                 │
│   Captures: status_code, headers, body (JSON), elapsed_ms      │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │  Response Context   │
                    │  Builder            │
                    │                     │
                    │  status: 200        │
                    │  elapsed: 142ms     │
                    │  body: {...}        │
                    │  contract: "..."    │
                    └──────────┬──────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                         LLM (Claude)                            │
│                                                                 │
│  System: "You are an API contract validator. Analyze..."        │
│  User:   <response context + contract>                         │
│                                                                 │
│  Output:                                                        │
│    verdict: PASS | WARN | FAIL                                  │
│    confidence: 0.0 - 1.0                                       │
│    findings: [ { field, issue, severity }, ... ]               │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Output Parser                                 │
│                                                                 │
│   Parse JSON from LLM → AnalysisResult dataclass               │
│   Fallback: WARN + raw text if JSON malformed                  │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
                    { verdict, confidence,
                      findings, raw_response }
```
