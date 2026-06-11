# Architecture — Agent 42: Orchestrator

## Pipeline Flow

```
Input
  │
  ▼
[Orchestrator]
  │  (knows full pipeline: A → B → C)
  │
  ▼
[Agent A]          ← blind to B and C
  │
  │ output_A
  ▼
[Agent B]          ← blind to A and C
  │
  │ output_B
  ▼
[Agent C]          ← blind to A and B
  │
  │ output_C
  ▼
Final Output
```

## Expanded View with Data Flow

```
Input → [Orchestrator] → Agent A → output_A → Agent B → output_B → Agent C → Final Output
         (knows full                (blind to           (blind to
          pipeline)                  B and C)            A and C)
```

## Orchestrator Internal Logic

```
def run_pipeline(input_data):
    result_a = call_agent_a(input_data)       # Stage 1
    result_b = call_agent_b(result_a)         # Stage 2: A's output becomes B's input
    result_c = call_agent_c(result_b)         # Stage 3: B's output becomes C's input
    return result_c
```

## Key Structural Properties

- The orchestrator is the only node that references all three agents
- Each pipeline agent has exactly one upstream dependency (the orchestrator's call) and one downstream consumer (the orchestrator's next call)
- Removing or replacing any pipeline agent requires changing only the orchestrator — not the other agents
- The data contract between stages (what format output_A must be in for Agent B to accept it) is enforced at the orchestrator level
