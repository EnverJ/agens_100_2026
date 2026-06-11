# Tool Patterns: Data Extraction Agent

## Pattern 1: Schema-Driven Extraction
Rather than asking the LLM to extract "everything important," the agent provides an explicit field list with types. This constrains the output space, improves reliability, and makes the output directly usable by downstream code without additional parsing.

## Pattern 2: Null-First Completeness Reporting
The agent tracks which schema fields were populated (non-null) and computes a completeness ratio. This metadata is returned alongside the extracted data, allowing callers to decide whether the extraction is "good enough" for their use case or whether human review is needed.

## Pattern 3: Type Coercion After Extraction
After the LLM returns extracted values as strings, the agent attempts type coercion based on the schema (e.g., `"3"` → `3` for integer fields). This post-processing step normalizes outputs and catches type mismatches early.

## Pattern 4: Composable Preprocessor
Agent 63 is designed to be called by other agents as a preprocessing step — not just by end users directly. Its simple input/output contract (text in, dict out) makes it trivially composable with any agent that receives unstructured text input.

## Pattern 5: Token Budget Awareness
Before building the LLM prompt, the agent estimates the token count of the input text. If the text exceeds the safe window, it truncates to the last N characters (preserving the most recent data, which is usually most relevant for log-style inputs) and adds a `[TRUNCATED]` notice.
