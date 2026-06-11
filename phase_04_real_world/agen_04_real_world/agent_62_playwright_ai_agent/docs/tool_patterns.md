# Tool Patterns: Playwright AI Agent

## Pattern 1: Browser as Headless Tool
Playwright is used as a headless browser tool — a controlled environment for interacting with web UIs programmatically. The browser is launched, used, and closed within a single agent invocation. This is the UI equivalent of making an HTTP request in Agent 61.

## Pattern 2: Page Snapshot → LLM Planning → Execution
The agent follows a three-phase pipeline: (1) take a snapshot of the page structure, (2) send it to LLM for action planning, (3) execute the plan. This is distinct from "LLM in the loop" patterns where the LLM decides each action after seeing the result of the previous one — here planning is done once upfront.

## Pattern 3: Safe eval Pattern for Action Execution
LLM-generated locator strings (e.g., `"get_by_role('button', name='Login')"`) are executed via controlled dispatch, not raw `eval()`. The agent maps action types to Playwright methods explicitly to prevent code injection.

## Pattern 4: Failure Evidence Collection
On any step failure, the agent immediately captures a screenshot before the browser state changes. This "evidence at the moment of failure" pattern is essential for debugging — screenshots taken after the fact often show a different page state.

## Pattern 5: Timeout-Bounded Execution
Each Playwright action is wrapped with a timeout guard. If a locator is not found within 5 seconds, the step fails gracefully rather than hanging. This makes the agent deterministic in its execution time.
