LLM Fundamentals — Agent 18

• System prompt framing is the core technique here. The same model responds very differently when the system prompt says "You are a helpful assistant" versus "You are a senior SDET responsible for full test coverage of a production feature." Domain framing activates domain-relevant behavior in the model.

• Structured output (JSON mode) is critical for downstream compatibility. When the output schema is fixed and enforced — either via JSON mode or via a schema validator on the parsed output — the test case list becomes a reliable input to Agent 19 and future agents. Unstructured prose output would require a separate parsing step and introduce error surface.

• Hallucination risk is present and specific here: the LLM may generate test steps that reference UI elements, API endpoints, or workflows that do not exist in the actual product. This is not a failure of the model — it is a limitation of operating without product context. The fix is to provide more context in the requirement string or to add domain examples to the prompt.

• Few-shot prompting improves test case quality significantly. Including one or two example requirement-to-test-case pairs in the prompt teaches the model the exact level of detail expected in steps, the format of expected_result, and the distribution of test types. This is worth experimenting with.

• Token budget matters at this stage. A detailed requirement with many scenarios can produce a large JSON list. Monitor response length and consider requesting a specific number of test cases (e.g., "generate exactly 5 test cases") if latency or token cost is a concern.
