## Core Concept – Agent 16

Agent 14 observed. Agent 15 scored. Agent 16 recommends. This three-step chain — observe, score, suggest — is the minimum viable self-improvement loop. Each step is independent, which means each can be tested, replaced, or upgraded without touching the others.

The key design principle of Agent 16 is that it maps error codes to fix templates. This is not intelligent reasoning — it is a lookup table. A violation of "Rule 2: output too short" maps to the suggestion "increase the prompt instruction to request longer responses." A reflection anomaly of "missing field: result" maps to "verify the upstream agent's output schema and add a fallback default." The templates are written by the builder; the agent selects and returns the right ones based on what Agent 15 flagged.

This template approach has an important property: it is auditable. Every suggestion can be traced back to a specific rule violation or anomaly flag. There is no black box. When a suggestion seems wrong, the builder can inspect the critique object and the template file to understand exactly why that suggestion was generated. This auditability is what makes the system safe enough to eventually automate.

The next evolution of this agent — not built here, but visible on the roadmap — would replace template lookups with an LLM call: "given this error and this context, what is the best fix?" That version would require a well-crafted prompt, few-shot examples, and careful evaluation. Agent 16 establishes the baseline: what does a correct suggestion look like for each error type? Those baseline answers become the few-shot examples for the future LLM-powered version.
