# Tool Patterns — Agent 41: Manager-Worker

## Manager-Worker Pattern

One coordinator agent (the manager) controls N executor agents (the workers). The manager holds the full context of the goal, decides how to break it down, dispatches tasks to individual workers, and collects their outputs. Workers know only their own subtask — they have no awareness of the broader goal or of each other.

This pattern separates concerns cleanly: the manager handles strategy and decomposition; workers handle execution. Adding more workers does not change the manager's logic.

```
              [Manager]
             /    |    \
        [W1]   [W2]   [W3]
         |       |       |
       res1    res2    res3
             \    |    /
           [Aggregation]
```

## Task Decomposition Pattern

The manager makes a dedicated LLM call whose only job is to split one compound task into N structured subtasks. This call does not perform any work — it only produces a plan.

The output of decomposition is a structured list (typically JSON) where each subtask has a clear scope, defined inputs, and an expected output format. This structure is what gets dispatched to workers.

Keeping decomposition as a separate LLM call (rather than combining it with execution) makes the decomposition auditable and correctable before any worker is called.

```
Input: "Analyze the Q3 sales data for trends, anomalies, and forecasts"

Decomposition call output:
[
  { "id": 1, "task": "Identify top trends in Q3 data", "type": "trend_analysis" },
  { "id": 2, "task": "Flag statistical anomalies in Q3 data", "type": "anomaly_detection" },
  { "id": 3, "task": "Generate a 30-day forecast based on Q3 data", "type": "forecasting" }
]
```

## Aggregation Pattern

After all workers have returned results, a second LLM call synthesizes N individual outputs into one coherent response. This call receives all worker results simultaneously and produces a unified summary.

Aggregation is not simple concatenation — the aggregator LLM is asked to reconcile, integrate, and present the results as a single coherent whole, resolving any contradictions or redundancies.

```
Worker results (input to aggregation):
  - result_1: "Top trends: mobile revenue up 34%, desktop down 12%"
  - result_2: "Anomaly detected: Week 11 spike, likely data entry error"
  - result_3: "Forecast: +8% growth over next 30 days"

Aggregation output:
  "Q3 analysis summary: Mobile revenue grew 34% while desktop declined 12%.
   A Week 11 spike was flagged as a probable data entry error and excluded
   from the forecast model. Outlook: +8% growth projected for the next 30 days."
```

## Sequential Dispatch Pattern

Workers are called one at a time in a loop. The manager does not move to the next worker until the current worker's result has been received. All results are collected into a list before aggregation begins.

This pattern trades throughput for simplicity. There is no concurrency management, no race conditions, and no partial failure handling needed. It is the correct starting point before introducing parallel dispatch (covered in Agent 52).

```
for subtask in subtasks:
    result = call_worker(subtask)
    results.append(result)

final_output = call_aggregator(results)
```

The sequential constraint makes debugging straightforward: if a worker returns a bad result, you know exactly which subtask caused it and can inspect the input that was sent.
