# Agent Fundamentals: Agent 23 — Test Run History Analyzer

## IS / IS NOT

### This agent IS:
- A persistent SDET memory agent for storing test run summaries in ChromaDB
- A natural-language query interface over structured historical test data
- A serializer that converts structured run results into embeddable text documents
- A trend-awareness tool: it supports "has this suite been failing?" style questions
- A direct specialization of Agent 22's general long-term memory pattern

### This agent IS NOT:
- Not a test executor — it stores results, it does not run tests
- Not a real-time monitor — history is queried on demand only
- Not a statistical analyzer — there is no regression model, no p-value, no significance test
- Not an alerting system — it returns information, it does not send notifications
- Not a log parser — it accepts pre-parsed run summaries, not raw log output
- Not a time-series database — ordering is by semantic similarity, not by timestamp

## Input Definition

### STORE operation
```python
{
  "operation": "store",
  "suite_name": str,          # e.g. "checkout_regression"
  "run_date": str,            # ISO 8601 date string, e.g. "2026-06-10"
  "pass_count": int,
  "fail_count": int,
  "duration_seconds": float,
  "failures": list[str]       # List of failure names or error messages
}
```

### QUERY operation
```python
{
  "operation": "query",
  "question": str,            # Natural language question about test history
  "k": int,                   # Number of historical runs to retrieve (default: 5)
  "suite_name": str           # Optional: filter to a specific suite by metadata
}
```

## Output Definition

### STORE response
```python
{
  "status": "stored",
  "id": str,                  # ChromaDB entry ID for this run
  "suite_name": str,
  "run_date": str
}
```

### QUERY response
```python
{
  "status": "ok",
  "question": str,
  "results": [
    {
      "suite_name": str,
      "run_date": str,
      "pass_rate": float,       # pass_count / (pass_count + fail_count)
      "duration_seconds": float,
      "top_failures": list[str],
      "similarity_score": float  # 1 - cosine_distance, higher = more relevant
    }
  ],
  "result_count": int
}
```
