# LLM Fundamentals: Playwright AI Agent

- **Code generation as structured output**: The LLM generates Playwright action steps as a JSON list of structured objects (locator string, action type, value). This is a controlled form of code generation — not free-form Python, but a structured intermediate representation that the agent can safely interpret and execute.

- **HTML comprehension**: LLMs trained on web data have implicit knowledge of HTML semantics — they understand that `<button aria-label="Submit order">` is a submit button and will generate `get_by_role("button", name="Submit order")` without being explicitly taught Playwright's API. This latent knowledge is what makes LLM-based locator generation effective.

- **Instruction following with domain constraints**: The system prompt constrains the LLM to only use Playwright-safe locator methods (get_by_role, get_by_label, get_by_text, get_by_placeholder) and to avoid fragile CSS selectors or XPaths. This demonstrates how prompt engineering can encode best practices.

- **Planning before execution**: The agent separates the planning phase (LLM generates the full action plan) from the execution phase (Playwright runs it). This reflects the ReAct-style pattern where reasoning precedes action — but here the full plan is generated upfront rather than step by step.

- **Graceful degradation**: If the LLM produces a malformed action plan, the agent falls back to a minimal "navigate and take screenshot" mode, ensuring some evidence is always collected.
