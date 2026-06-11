LLM Fundamentals — Agent 20

• Agent 20 makes no LLM call. JSON parsing is deterministic and fast — there is no ambiguity that requires language model reasoning. Using an LLM here would add hundreds of milliseconds to what should be an instant extraction step.

• The output of Agent 20 is designed to be injected into LLM prompts in downstream agents. A prompt like "The following test run produced these failures: {failures}. Classify each failure as: environment issue, product bug, or test script error" is a high-value LLM task that depends entirely on Agent 20 having already extracted the failure list in structured form.

• Token efficiency matters for downstream LLM calls. If Agent 20 passed the raw Allure JSON (potentially megabytes) to an LLM, the token cost would be prohibitive and the model would struggle to find the relevant signal. Agent 20's summary is the pre-processing step that makes LLM analysis of test results economically viable.

• The failures list format — [{ name: str, error: str }] — is designed to be directly serializable into a prompt. Each failure can be formatted as a line: "FAILED: {name} — {error}" and injected into an analysis prompt without any additional transformation.

• Context window planning: a test suite with 500 tests might produce 50 failures. Each failure entry in the summary is roughly 100–200 tokens when serialized. This is well within the context window of any modern model, making the summary safe to pass in full to downstream analysis agents.
