Tool Patterns — Agent 14

Agent 14 uses no tools and makes no external calls. It follows the Pure Evaluation Pattern: take inputs, apply deterministic checks, return a structured result.

This is the simplest possible pattern — but it is used deliberately. Adding tool calls or LLM calls here would violate the principle of one variable at a time. The reflection layer must be trustworthy and fast before more complexity is layered on top.

Pattern in use:
  Input dict → Python evaluation logic → Output dict

The only "tool" is the Python runtime itself. This agent demonstrates that not every component of an agent system needs to be AI-powered. Deterministic evaluation logic that is fast, predictable, and testable is often preferable to an LLM call for structural checks.
