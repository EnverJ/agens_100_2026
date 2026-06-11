# Agent Fundamentals: Data Extraction Agent

## IS
- A schema-driven information extraction agent
- An LLM-powered replacement for brittle regex-based parsers
- A preprocessing building block used by other agents in the pipeline
- A completeness reporter — tells you what was found and what is missing
- Stateless — each invocation is independent

## IS NOT
- Not an OCR tool — text only, not images
- Not a schema inferrer — schema must be provided by the caller
- Not a data validator against external systems
- Not a storage layer — returns data, does not save it
- Not a structured data parser (use json.loads for JSON, not this agent)

## Input
```python
{
  "raw_text": "CRITICAL ERROR 2026-06-03 09:14:32 UTC — order-service DB_CONN_TIMEOUT after 30s. Retry #3 failed. Affected: checkout flow.",
  "schema": {
    "timestamp": "datetime string",
    "error_code": "string",
    "severity": "string",
    "service_name": "string",
    "retry_count": "integer",
    "affected_component": "string",
    "user_id": "string or null"
  }
}
```

## Output
```python
{
  "extracted": {
    "timestamp": "2026-06-03T09:14:32Z",
    "error_code": "DB_CONN_TIMEOUT",
    "severity": "CRITICAL",
    "service_name": "order-service",
    "retry_count": 3,
    "affected_component": "checkout flow",
    "user_id": null
  },
  "completeness": 0.857,
  "missing_fields": ["user_id"]
}
```
