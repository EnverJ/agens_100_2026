# Agent Fundamentals: Agent 24 — Test History Memory

## IS / IS NOT

### This agent IS:
- A per-test-case persistent memory store using ChromaDB
- A keyed retrieval system: test_name is the lookup key
- A source of individual test outcome history for downstream reasoning agents
- A metadata-filtered retrieval agent (test_name filter, recency sort)
- The per-test complement to Agent 23's suite-level memory

### This agent IS NOT:
- Not a suite-level store — one entry per individual test execution, not per suite run
- Not a flakiness scorer — it stores and retrieves outcomes, it does not compute flakiness metrics (see Agent 37)
- Not a test runner — it stores outcomes, it does not execute tests
- Not a diff engine — it does not compare current results to historical baselines automatically
- Not a root cause analyzer — it surfaces error messages but does not reason about why failures occur
- Not a real-time stream — it is a query-on-demand system, not a live event feed

## Input Definition

### STORE operation
```python
{
  "operation": "store",
  "test_name": str,         # e.g. "test_login_oauth_redirect"
  "outcome": str,           # "pass" | "fail" | "skip" | "error"
  "error_message": str,     # Empty string if outcome is "pass"
  "duration_ms": int,       # Execution time in milliseconds
  "run_id": str,            # Identifier of the enclosing test run
  "timestamp": str          # ISO 8601 datetime of this test execution
}
```

### QUERY operation
```python
{
  "operation": "query",
  "test_name": str,         # Exact test name to look up
  "last_n": int             # Number of most recent outcomes to return (default: 10)
}
```

## Output Definition

### STORE response
```python
{
  "status": "stored",
  "id": str,                # ChromaDB entry ID for this outcome
  "test_name": str,
  "outcome": str,
  "timestamp": str
}
```

### QUERY response
```python
{
  "status": "ok",
  "test_name": str,
  "outcomes": [
    {
      "outcome": str,          # "pass" | "fail" | "skip" | "error"
      "error_message": str,    # Empty if outcome is "pass"
      "duration_ms": int,
      "run_id": str,
      "timestamp": str         # ISO 8601, sorted most-recent first
    }
  ],
  "failure_rate": float,       # Proportion of non-pass outcomes in returned window
  "last_seen_error": str       # Most recent error_message; null if all passed
}
```
