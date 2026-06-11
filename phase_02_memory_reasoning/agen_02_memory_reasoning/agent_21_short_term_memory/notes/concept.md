# Concept: Short-Term Memory in a Reasoning Pipeline

Agent 21 exists to elevate a primitive concept — in-session memory — to the standard required by Phase 2's reasoning pipeline. In Phase 1, Agent 12 introduced the idea of keeping a list of messages within a session. That was sufficient for simple agents that reply and forget. Phase 2 agents reason across multiple steps, and they need richer context objects to reason over, not bare strings.

The core insight is that the shape of memory determines what you can ask of it. A list of raw user strings tells a downstream reasoner only what words were typed. A list of context objects — each carrying role, timestamp, and semantic tags — tells it who said what, when, and why it matters. This structured representation is what lets later agents do planning, hypothesis generation, and causal reasoning without re-reading the full conversation.

Agent 21 also introduces the concept of a bounded sliding window. Unlimited session memory would eventually overflow a model's context window. By capping the list at N entries and dropping the oldest, the agent maintains a fixed-size representation of the recent conversational state. This is the same design used in production conversational AI systems: keep the most recent and most relevant, discard the oldest.

The connection to previous work is deliberate. Agents 21 through 25 form a memory stack: working memory (21 revisited), session memory (21), long-term memory (22), domain-specific history (23, 24), and ephemeral scratch space (25). Understanding how each layer differs — scope, structure, speed, and persistence — is the foundation for building agents that remember intelligently rather than remembering everything.
