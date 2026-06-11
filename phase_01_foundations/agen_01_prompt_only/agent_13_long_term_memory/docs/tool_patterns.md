Tool Patterns — Agent 13

Agent 13 does not use tool-calling (function calling via the LLM API). Instead it follows the Direct Storage Pattern: the agent code itself calls ChromaDB's Python client directly, bypassing any LLM tool dispatch layer.

This is intentional. ChromaDB reads and writes are deterministic and fast — there is no need for an LLM to decide when to call them. The agent's own logic determines whether to store or query based on the incoming mode flag.

Pattern in use:
  Direct SDK call → ChromaDB Python client → disk-backed collection

This contrasts with Agents 04 and 05, which used LLM tool-calling to decide which external function to invoke. Agent 13 shows that not every tool interaction requires an LLM in the decision loop. When the operation is deterministic, call the tool directly from application code.
