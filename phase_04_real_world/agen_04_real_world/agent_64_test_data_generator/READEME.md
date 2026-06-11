# Agent 64 — Test Data Generator

## Purpose
Agent 64 generates realistic, diverse test data on demand. Given a data type specification (user profile, product record, transaction history, form input), it uses an LLM to produce datasets that include both representative happy-path values and systematic boundary/edge cases. It replaces the manual, error-prone work of creating test data by hand and ensures edge cases — max string lengths, negative numbers, special characters, null values — are always included.

## What This Agent Introduces
**LLM-Powered Test Data Synthesis** — generating realistic and adversarial test datasets from a data schema description, including automatic boundary value generation.

## How It Works
1. Accept a data schema description, the number of records to generate, and a generation mode (realistic, boundary, mixed).
2. Build a prompt that instructs the LLM to generate records matching the schema, including specific edge cases based on field types.
3. In boundary mode, explicitly request: empty strings, max-length strings, negative numbers, zero, null optionals, special characters, Unicode, and future/past date extremes.
4. Parse the LLM output as a JSON array of records.
5. Validate each record against the schema and report any malformed records.
6. Return the list of records with metadata (mode used, count generated, invalid records skipped).

## What It Is NOT
- No database seeding — returns data, does not write to any database
- No PII generation — does not generate real SSNs, credit card numbers, or actual real-person data
- No guaranteed uniqueness across multiple invocations — duplicates possible across calls

## Scope
- Up to 50 records per invocation (LLM token limits apply)
- Supports nested object schemas (address inside user profile)
- Returns JSON array, ready for direct use in test payloads
- Boundary mode always generates at least one record per boundary type

## Key Lesson
Test data quality determines test quality. Realistic data catches integration bugs; boundary data catches validation bugs. An LLM can generate both in one call, making thorough data coverage accessible without manual effort.

## Next Step
Once Agent 64 is complete, proceed to Agent 65.
