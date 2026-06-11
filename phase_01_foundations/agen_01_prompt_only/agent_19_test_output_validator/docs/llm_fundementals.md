LLM Fundamentals — Agent 19

• Agent 19 makes no LLM call. Assertion logic is deterministic — exact comparison and type checking do not benefit from language model reasoning. Adding an LLM here would introduce nondeterminism into the assertion layer, which must be the most reliable component in any test pipeline.

• The contrast with LLM-based assertion is worth understanding. An LLM asserter might receive the actual and expected outputs and return "these are semantically equivalent" — which is useful for natural language outputs where exact match is too strict. Agent 19 handles structured outputs. LLM-based semantic assertion is appropriate for free-text fields only.

• Structured output from Agent 18 (the test case list) is what makes Agent 19's schema validation useful. Because Agent 18 enforces a fixed JSON schema on its output, Agent 19 can validate any test run result against that schema with confidence. This chain — structured generation → structured validation — is a core LLM pipeline pattern.

• When Agent 19 returns FAIL, the diff field should be injected into the next LLM prompt if an LLM is used to analyze the failure. A prompt like "the following assertion failed with this diff: {diff}. What is the most likely cause?" is far more effective than passing the raw actual and expected blobs.

• Token efficiency: Agent 19 never sends data to an LLM, so there is no token cost. This makes it safe to call it frequently — once per test case, once per API call, once per pipeline step — without concern for latency or cost.
