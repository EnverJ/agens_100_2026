# Tool Patterns — Agent 42: Orchestrator

## Pipeline Pattern

A fixed sequence of agent calls where each stage transforms data and passes its output to the next stage. The pipeline has a defined start (the first stage) and a defined end (the last stage). Adding a new stage means adding one more agent call in the orchestrator's sequence — no other agent needs to change.

```
Stage 1 → Stage 2 → Stage 3 → ... → Stage N → Output
```

The pipeline pattern is the most common multi-agent architecture for processing workflows. It maps naturally to assembly lines, ETL pipelines, and CI/CD pipelines.

## Sequential Chaining

The implementation mechanism of the Pipeline Pattern. Each agent call is made only after the previous call has returned its result. The result is stored in a local variable and passed directly as the next call's argument.

```python
result_a = agent_a.run(initial_input)
result_b = agent_b.run(result_a)
result_c = agent_c.run(result_b)
return result_c
```

Sequential chaining makes the data flow explicit and auditable. At any point in execution, you can inspect `result_a` or `result_b` to understand what each stage produced.

## Output-as-Input

The mechanism by which data moves through the pipeline. Rather than writing intermediate results to a shared store, the output of each agent call is directly passed as the input argument to the next call. This keeps the pipeline stateless from the perspective of the agents — no agent reads from a database or queue; it receives everything it needs from the orchestrator's function call.

Output-as-input also means the pipeline is easy to test: you can call any stage with a synthetic input and verify its output without running the full pipeline.

## Stage Contract Pattern

Each pipeline stage has a defined input schema and output schema. The contract specifies exactly what format a stage expects to receive and what format it will return. The orchestrator enforces these contracts at every handoff.

```
Stage A Contract:
  Input:  { "raw_text": str }
  Output: { "summary": str, "key_points": list[str] }

Stage B Contract:
  Input:  { "summary": str, "key_points": list[str] }
  Output: { "sentiment": str, "confidence": float }
```

When Stage A's output matches Stage B's input schema exactly, the handoff is seamless. When schemas differ, the orchestrator transforms the data between calls. Defining contracts before building stages prevents integration failures.
