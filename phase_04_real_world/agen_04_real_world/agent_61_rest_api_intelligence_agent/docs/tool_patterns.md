# Tool Patterns: REST API Intelligence Agent

## Pattern 1: HTTP Client as Tool
The `requests` library is used as the agent's external tool. The agent calls it to acquire evidence from the real world (the API response), then passes that evidence to the LLM for analysis. This separation of "data acquisition tool" from "reasoning engine" is the canonical pattern for all real-world agents.

## Pattern 2: Context Assembly Before LLM Call
Before calling the LLM, the agent assembles a structured context block — formatting status code, headers, body, elapsed time, and contract description into a single coherent prompt. Good context assembly is critical: poorly formatted context leads to poor LLM analysis.

## Pattern 3: Structured Output with Fallback
The LLM is prompted to return JSON. The agent includes a parser that attempts `json.loads()` on the LLM output, and falls back gracefully to `{"verdict": "WARN", "findings": [{"issue": raw_text}]}` if parsing fails. Robust agents never crash on LLM output format deviations.

## Pattern 4: Response Truncation Guard
If the API response body exceeds the token budget, the agent truncates it and adds a `[TRUNCATED]` marker before sending to the LLM. This prevents context overflow while signaling to the LLM that the full response was not analyzed.

## Pattern 5: Single Responsibility per Invocation
The agent does exactly one thing per call: analyze one request/response pair. It does not loop, retry, or accumulate state. This makes it composable — a test suite runner can call it in a loop while the agent stays simple.
