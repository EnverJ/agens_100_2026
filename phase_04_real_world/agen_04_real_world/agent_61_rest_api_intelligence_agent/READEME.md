# Agent 61 — REST API Intelligence Agent

## Purpose
Agent 61 connects to a real REST API endpoint, retrieves the response, and uses an LLM to perform deep semantic analysis of that response. Rather than simple pass/fail status-code checks, this agent evaluates whether the response is meaningful, contract-compliant, and free of data anomalies. It is the foundation for intelligent API testing in the project.

## What This Agent Introduces
**Semantic API Response Validation** — using an LLM to understand what an API response *means*, not just what HTTP code it returns.

## How It Works
1. Accept an API endpoint URL, HTTP method, headers, body, and an optional API contract (schema or description).
2. Send the HTTP request using the `requests` library and capture status code, headers, body, and latency.
3. Serialize the full response into a structured context block.
4. Pass the response plus the API contract to the LLM with a structured analysis prompt asking it to evaluate contract compliance, semantic correctness, field anomalies, and data quality.
5. Parse the LLM output into a structured result: verdict (PASS / WARN / FAIL), confidence, and a findings list.
6. Return the analysis report to the caller.

## What It Is NOT
- No UI testing — this is purely API-layer intelligence
- No load testing — single-request analysis only, not concurrent load
- No authentication manager — auth headers must be provided by the caller
- No automatic contract generation — contract must be supplied or described by the caller
- No test suite runner — this agent analyzes one request/response pair per call

## Scope
- Supports GET, POST, PUT, PATCH, DELETE methods
- Handles JSON response bodies; binary or XML responses are flagged as unsupported
- LLM analysis is bounded by response body size (truncated at ~4000 tokens)
- Returns structured dict with verdict, confidence score, and list of findings

## Key Lesson
Status codes tell you *if* an API responded. LLM semantic analysis tells you *whether that response makes sense*. These are different questions, and the second one catches far more bugs — wrong data types, missing fields, logically impossible values, silent contract drift.

## Next Step
Once Agent 61 is complete, proceed to Agent 62.
