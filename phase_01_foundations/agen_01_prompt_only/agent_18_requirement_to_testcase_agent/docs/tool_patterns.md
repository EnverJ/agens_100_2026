Tool Patterns — Agent 18

Agent 18 does not use tool-calling (function calling). It uses the Prompt-to-Structured-Output Pattern: craft a system prompt that frames the LLM in a specific role, inject the user's input, and parse the JSON response.

This pattern is the workhorse of LLM-powered automation: no tools, no APIs, just a well-engineered prompt producing machine-readable output. It is simple, fast, and composable. The output of this pattern is a first-class data object — not a string for a human to read.

Pattern in use:
  system_prompt (SDET frame) + user_prompt (requirement) → LLM (JSON mode) → parsed list

SDET context: This same pattern applies to any requirement-to-artifact generation task: requirement → test plan, requirement → API contract, requirement → acceptance criteria. The agent structure stays the same; only the system prompt changes. Build the pattern once, reuse it everywhere.
