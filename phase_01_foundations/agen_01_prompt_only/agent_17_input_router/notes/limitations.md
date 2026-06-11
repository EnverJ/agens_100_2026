Agent 17 — Limitations

This agent does NOT:
• Handle missing or None flag values gracefully — undefined flags cause a routing error or fall through to the default branch unexpectedly
• Support more than two flags (memory_flag, tool_flag) without adding new branches manually
• Log routing decisions to memory or a persistent store — routing is stateless and leaves no trace
• Route based on the content or meaning of user_input — only structured flags are considered
• Handle the case where the target agent does not exist or is unavailable

We change one variable at a time.
