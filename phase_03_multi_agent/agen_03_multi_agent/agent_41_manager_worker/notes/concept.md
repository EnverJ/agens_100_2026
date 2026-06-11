# Concept: Manager Worker Pattern

The manager-worker pattern exists because complex tasks cannot fit inside a single LLM call without degrading quality. When a task is large enough that breaking it into parts produces better results than attempting it whole, you need an agent that only breaks things apart. This is the manager's entire job. It is not smarter than the workers — it is specialized in decomposition and delegation.

This agent teaches the single most important insight in multi-agent design: the entity that decides what to do and the entity that does the thing should be different agents. The manager holds the high-level goal and the decomposition strategy. The workers hold domain knowledge and execution capability. Neither needs to know what the other knows beyond the interface between them.

The pattern connects directly to Agent 40 (the last agent of phase 2), which showed that a single agent reaches limits. Agent 41 is the answer to those limits. When one agent cannot hold the full context of a problem, you split the problem — not the agent. The manager ensures that each worker receives only the slice of context it needs to do its job well.

In SDET contexts, this pattern maps directly to a test lead who writes a test plan and assigns test cases to engineers. The test lead does not run the tests. The engineers do not write the plan. Agent 41 encodes this real-world division of labor into software.
