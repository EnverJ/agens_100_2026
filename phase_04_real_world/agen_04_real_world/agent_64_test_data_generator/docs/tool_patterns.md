# Tool Patterns: Test Data Generator

## Pattern 1: Mode-Based Prompt Switching
The agent uses three distinct prompt strategies based on the requested mode (realistic, boundary, mixed). Mode selection is resolved before the LLM call, and the appropriate prompt template is selected. This avoids a single monolithic prompt that tries to handle all cases poorly.

## Pattern 2: Boundary Type Enumeration
The boundary mode prompt includes an explicit list of boundary types: empty string, max-length string (255 chars), negative integer, zero, null for optional fields, special characters, Unicode, past date extreme, future date extreme. This enumeration ensures systematic coverage rather than hoping the LLM picks good edge cases on its own.

## Pattern 3: Schema as Prompt Context
The schema description is injected verbatim into the prompt. Rather than converting it to a formal JSON Schema object (which would add complexity), the agent accepts a natural language schema description — "name: full name, Indian names preferred" — which the LLM interprets correctly with zero additional parsing code.

## Pattern 4: Validation That Preserves Invalidity
When validating generated records against the schema, the agent does NOT discard boundary records that intentionally violate constraints. Discarding invalid records would defeat the purpose of boundary testing. Instead, invalid records are flagged in metadata but included in the output.

## Pattern 5: Composable Data Factory
The agent is explicitly designed to be called by other agents. Its return format (plain JSON array) requires no deserialization by callers — records can be passed directly to API calls, database inserts, or test payloads without transformation.
