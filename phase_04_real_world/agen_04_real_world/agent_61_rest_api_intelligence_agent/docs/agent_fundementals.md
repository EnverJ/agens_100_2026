# Agent Fundamentals: REST API Intelligence Agent

## IS
- An agent that makes a real HTTP request to a live API endpoint
- A semantic validator: it judges response meaning, not just HTTP status
- A contract checker: compares actual response against a provided contract description
- A structured output producer: returns verdict, confidence, and itemized findings
- Stateless: each invocation is independent

## IS NOT
- Not an API mock or stub — it calls real endpoints
- Not a load testing tool — single request per run
- Not an authentication handler — caller provides auth headers
- Not a schema generator — contract must be pre-defined
- Not a regression comparator — no baseline stored between runs

## Input
```python
{
  "url": "https://api.example.com/orders/123",
  "method": "GET",
  "headers": {"Authorization": "Bearer <token>"},
  "body": None,
  "contract_description": "Returns an order object with order_id (int), status (enum: PENDING/PROCESSING/SHIPPED/DELIVERED), items (non-empty array), total_price (float > 0)"
}
```

## Output
```python
{
  "verdict": "WARN",
  "confidence": 0.82,
  "findings": [
    {"field": "status", "issue": "Value 'CMPLTD' not in documented enum", "severity": "HIGH"},
    {"field": "items", "issue": "Array is empty for a DELIVERED order — unexpected", "severity": "MEDIUM"}
  ],
  "status_code": 200,
  "elapsed_ms": 142
}
```
