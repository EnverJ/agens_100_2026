# Tool Patterns — Agent 43: Test Suite Orchestrator

## Pipeline Pattern

The test suite orchestrator is an instance of the Pipeline Pattern from Agent 42 applied to the CI/CD domain. Each stage in the pipeline corresponds to a phase of the test run: smoke tests → unit tests → integration tests → E2E tests → reporting. The orchestrator manages the sequence, and each stage agent is unaware of the others.

```
Smoke → Unit → Integration → E2E → Report Generator
  ↑
[Orchestrator controls the full sequence]
```

## Abort-on-Failure Pattern

A conditional gate inserted after critical pipeline stages. After a designated critical stage completes, the orchestrator checks the result before proceeding. If the critical stage has failed beyond a threshold, the pipeline is halted and all remaining stages are skipped.

```python
result = call_critical_stage_agent(input)
if result["critical_failure"]:
    return call_report_agent(partial_results, aborted=True)
# else: continue to next stage
```

This pattern prevents cascading failures — where a fundamental problem causes every subsequent stage to fail for the wrong reasons, producing misleading results and wasting execution time.

## Stage Handoff Pattern

Each stage agent receives exactly what it needs from the orchestrator — no more, no less. The orchestrator extracts the relevant portion of the test plan for each agent (e.g., only the unit test group is passed to the unit test agent). After the agent returns, its result is stored and the next relevant portion is extracted for the next agent. This keeps each agent's context minimal and focused.

```python
smoke_result = call_smoke_agent(test_plan["smoke_group"])
unit_result = call_unit_agent(test_plan["unit_group"])
# Each agent receives only its own group, not the full test plan
```

## Test Group Dispatch Pattern

The orchestrator maps test group types to their corresponding execution agents. This mapping is the orchestrator's core routing table. When the test plan contains a group of type "integration", the orchestrator calls the integration test agent. This dispatch logic is explicit and centralized — changing which agent handles integration tests means changing one line in the orchestrator, not modifying any of the agents themselves.

```python
AGENT_MAP = {
    "smoke": call_smoke_test_agent,
    "unit": call_unit_test_agent,
    "integration": call_integration_test_agent,
    "e2e": call_e2e_test_agent,
}

for group in test_plan["groups"]:
    agent_fn = AGENT_MAP[group["type"]]
    result = agent_fn(group)
    results.append(result)
```
