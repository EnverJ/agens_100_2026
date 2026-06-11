# Architecture — Agent 43: Test Suite Orchestrator

## Full Pipeline View

```
Test Plan Input
      │
      ▼
[Test Suite Orchestrator]
      │
      ├──► [Smoke Test Agent] ──► pass? → continue
      │                           fail? → ABORT (skip remaining groups)
      │
      ├──► [Unit Test Agent] ──► results { passed, failed, skipped }
      │
      ├──► [Integration Test Agent] ──► results { passed, failed, skipped }
      │
      ├──► [E2E Test Agent] ──► results { passed, failed, skipped }
      │
      └──► [Report Generator Agent] ──► Final Report
                                        { total, passed, failed, skipped, report_url }
```

## Abort-on-Critical-Failure Logic

```
smoke_result = call_smoke_test_agent(test_plan.smoke_group)

if smoke_result.critical_failure:
    return call_report_agent(
        results=[smoke_result],
        aborted=True,
        abort_reason="Smoke tests failed — environment is not viable"
    )

# Continue with remaining groups only if smoke tests passed
unit_result = call_unit_test_agent(test_plan.unit_group)
integration_result = call_integration_test_agent(test_plan.integration_group)
e2e_result = call_e2e_test_agent(test_plan.e2e_group)

return call_report_agent(
    results=[smoke_result, unit_result, integration_result, e2e_result],
    aborted=False
)
```

## Data Flow

```
test_plan (input)
    │
    ├── smoke_group ──────────► Smoke Test Agent ──► smoke_result
    │
    ├── unit_group ───────────► Unit Test Agent ───► unit_result
    │
    ├── integration_group ────► Integration Agent ─► integration_result
    │
    └── e2e_group ────────────► E2E Test Agent ────► e2e_result

[smoke_result, unit_result, integration_result, e2e_result]
    │
    ▼
Report Generator Agent
    │
    ▼
suite_result { total, passed, failed, skipped, report_url }
```
