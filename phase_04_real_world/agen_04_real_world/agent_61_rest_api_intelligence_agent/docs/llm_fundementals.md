# LLM Fundamentals: REST API Intelligence Agent

- **Semantic reasoning over structured data**: The LLM reads a JSON payload and reasons about whether its values are logically consistent with the described contract — a capability far beyond regex or schema validators.

- **Structured output enforcement**: The system prompt instructs the LLM to respond only in a specific JSON format (verdict, confidence, findings). This is the "output schema" pattern — using prompt constraints to make LLM output machine-parseable.

- **Zero-shot domain knowledge**: The LLM brings pre-trained knowledge of REST API conventions, HTTP semantics, and common data patterns, allowing it to flag anomalies (e.g., negative prices, null required fields) even without being explicitly trained on the specific API.

- **Confidence calibration**: The agent asks the LLM to report a confidence score with its verdict, teaching the concept that LLM outputs should carry uncertainty estimates — not all answers are equally reliable.

- **Context window as the "memory"**: The entire API response and contract are injected into a single prompt context. There is no retrieval — everything the LLM needs to reason fits in one call. This is the simplest form of context-augmented reasoning.
