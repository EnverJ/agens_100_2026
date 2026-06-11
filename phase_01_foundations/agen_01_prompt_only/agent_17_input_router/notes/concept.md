## Core Concept – Agent 17

By Agent 17, the system has memory (Agents 12 and 13), tools (Agents 04 and 05), validation (Agent 08), reflection (Agent 14), and critique (Agent 15). The problem is that a single linear pipeline can no longer serve all use cases. Some inputs need memory access. Some need tool calls. Some need both. Some need neither. Agent 17 is the mechanism that decides which path the input should take.

The routing logic is deliberately deterministic. Every possible combination of flag values maps to exactly one next agent. There are no gray areas, no probability weights, no LLM judgment calls. This is a strength, not a weakness. Deterministic routing means the pipeline behavior is fully predictable from the context state. A builder can look at the context flags and know with certainty which agent will be called next — before running anything.

The context object produced by Agent 11 is what makes this routing possible. Because Agent 11 ensures that every interaction has a consistent, structured context with named flags, Agent 17 can rely on those fields always being present. This is why the context builder was introduced before the router: you cannot route on structure that does not exist yet.

Agent 17 also demonstrates a broader architectural principle: control flow in a multi-agent system should be explicit and inspectable. Routing based on hidden state, embedding similarity, or LLM decisions is powerful — but it is also opaque and hard to debug. Deterministic flag-based routing keeps the control layer simple while the intelligence lives in the individual agents. Later in the project, probabilistic and LLM-based routing will be introduced — but this explicit baseline makes those later patterns easier to evaluate and calibrate.
