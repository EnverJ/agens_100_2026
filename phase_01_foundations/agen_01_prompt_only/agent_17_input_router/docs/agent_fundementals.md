Agent 17 — input_router — Fundamentals

IS:
✔️ Reads memory_flag and tool_flag from the context object
✔️ Applies a deterministic if/elif decision tree to select the next agent
✔️ Returns the next agent ID as a string

IS NOT:
✗ Does not execute any agent — only names the next one
✗ Does not modify the context object
✗ Does not use LLM judgment, probability, or reasoning

Input: Context object (dict) with memory_flag (bool) and tool_flag (bool)
Output: Next agent ID string (e.g. "agent_13_long_term_memory")
