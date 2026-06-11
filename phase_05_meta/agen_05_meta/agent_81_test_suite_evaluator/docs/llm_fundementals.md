# LLM Fundamentals — Agent 81: Test Suite Evaluator

- **Structured data summarisation.** The LLM receives a pre-computed metric breakdown
  (six numeric scores with context) and synthesises it into coherent prose. The model
  is not doing arithmetic — the Python layer does all calculations — but it translates
  numbers into contextual meaning (e.g., "a 25:1 happy-path ratio in a payments module
  is particularly dangerous").

- **Few-shot recommendation prompting.** The system prompt includes two worked examples
  of scorecard-to-recommendation mappings, teaching the model the expected specificity
  level. Without examples, the model tends to produce generic advice ("add more negative
  tests"). With examples, it produces targeted suggestions ("add tests for the
  `process_refund` error path in `test_payments.py`").

- **Contextual grounding with concrete numbers.** The prompt always includes the actual
  metric values alongside the feature area names. This grounds the LLM's output in
  specifics rather than abstractions and dramatically reduces hallucinated recommendations
  that reference non-existent test files.

- **Output format enforcement (JSON array).** The recommendations block in the system
  prompt specifies that output must be a JSON array of objects with `dimension`,
  `finding`, and `action` keys. The model is not given the option to respond in prose
  for this section. This allows the output to be parsed programmatically downstream.

- **Temperature=0 for consistency.** Quality scorecards are compared run-to-run. Using
  temperature=0 ensures that identical inputs produce identical recommendations, making
  the agent's output deterministic and suitable for automated diff-tracking in CI.
