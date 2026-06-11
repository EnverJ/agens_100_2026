# Agent Fundamentals: Test Data Generator

## IS
- An on-demand test data factory driven by schema description and LLM
- A boundary value generator — systematically produces edge cases
- A mode-aware generator: realistic, boundary, or mixed output
- A composable tool — other agents can call it to generate their own test inputs
- Stateless — generates fresh data each invocation

## IS NOT
- Not a database seeder — does not write to any storage
- Not a PII generator — all data is fictional
- Not a uniqueness guarantor across multiple calls
- Not a statistical distribution simulator
- Not a CSV or XML generator — JSON output only

## Input
```python
{
  "schema": {
    "user_id": "integer, auto-increment style",
    "name": "full name, Indian names preferred",
    "email": "valid email address",
    "phone": "Indian mobile number format",
    "age": "integer 18-90",
    "account_status": "enum: ACTIVE, INACTIVE, SUSPENDED",
    "signup_date": "ISO date string"
  },
  "count": 10,
  "mode": "mixed"
}
```

## Output
```python
{
  "records": [
    {"user_id": 1, "name": "Arjun Mehta", "email": "arjun.mehta@gmail.com",
     "phone": "+91-9876543210", "age": 34, "account_status": "ACTIVE",
     "signup_date": "2024-03-15"},
    {"user_id": 2, "name": "", "email": "not-an-email", "phone": "0",
     "age": -1, "account_status": "SUSPENDED", "signup_date": "1900-01-01"}
  ],
  "count": 10,
  "mode": "mixed",
  "boundary_types_covered": ["empty_string", "negative_number", "extreme_past_date", "invalid_email"]
}
```
