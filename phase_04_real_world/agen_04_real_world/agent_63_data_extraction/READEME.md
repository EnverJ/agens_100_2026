# Agent 63 — Data Extraction Agent

## Purpose
Agent 63 extracts structured data from unstructured text inputs such as server logs, error reports, email notifications, and incident tickets. Given free-form text, it uses an LLM to identify and pull key fields — dates, error codes, user IDs, service names, severity levels — and returns a clean Python dictionary. It is the foundation for all agents in the project that need to parse free-text inputs before acting on them.

## What This Agent Introduces
**LLM-Powered Information Extraction** — converting unstructured natural language or semi-structured text into a typed, usable Python dict.

## How It Works
1. Accept raw text input (log line, email body, incident report, etc.) and a target schema describing what fields to extract.
2. Build a prompt that presents the text and the desired output schema.
3. Send to LLM, instructing it to return only a JSON object matching the schema — null for missing fields.
4. Parse the JSON response and validate field types against the schema.
5. Return the extracted dict with a completeness score (how many schema fields were successfully populated).

## What It Is NOT
- No persistent storage — extracted data is returned, not saved to a database
- No OCR — input must be text, not image-based documents
- No streaming extraction — full text must be available upfront
- No schema inference — the caller must specify what fields to extract

## Scope
- Handles text up to approximately 6000 tokens
- Supports nested field extraction (e.g., extract an "error" object with sub-fields)
- Returns null for fields not found — does not hallucinate values
- Language-agnostic input (English, Hindi, multilingual logs supported)

## Key Lesson
Most real-world data exists in free-text form. The ability to extract structured fields from unstructured text is one of the highest-leverage LLM capabilities for engineering workflows — it replaces brittle regex patterns with understanding.

## Next Step
Once Agent 63 is complete, proceed to Agent 64.
