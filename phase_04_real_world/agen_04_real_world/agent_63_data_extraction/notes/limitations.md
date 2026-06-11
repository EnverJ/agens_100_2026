# Limitations: Data Extraction Agent

This agent does NOT:

- Perform OCR — input must be plain text, not image scans or PDFs with embedded images
- Infer the extraction schema automatically — the caller must define target fields
- Handle text longer than approximately 6000 tokens without truncation
- Guarantee zero hallucinations — uses anti-hallucination prompting but cannot be 100% certain for ambiguous text
- Validate extracted values against external systems (e.g., check if an extracted order_id actually exists in the database)
- Perform multi-document cross-referencing — one text block per invocation
- Normalize extracted values into specific formats automatically (dates may be returned in source format unless schema specifies a format)
- Store extraction results — returns data, does not persist it
- Handle real-time streaming text input — full text must be provided upfront
- Extract data from structured formats (JSON, CSV) — use standard parsers for those; this agent is for truly unstructured text
