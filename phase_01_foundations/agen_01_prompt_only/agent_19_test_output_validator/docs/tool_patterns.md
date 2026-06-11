Tool Patterns — Agent 19

Agent 19 uses no tools and makes no external calls. It follows the Assertion Module Pattern: a stateless, reusable function that takes actual and expected inputs and returns a structured verdict.

This pattern is the backbone of every testing framework: pytest's assert statements, JUnit's assertEquals, Selenium's assertTitle. Agent 19 is that same concept expressed as a callable agent component — one that any other agent in the pipeline can invoke.

Pattern in use:
  (actual, expected, mode) → comparison logic → { status, reason, diff }

Key properties:
  • Stateless: no memory, no side effects, safe to call in parallel
  • Reusable: any agent that needs to assert something calls Agent 19
  • Composable: the result dict can be passed directly to Agent 16 (error correcting) or Agent 20 (report reader)

SDET context: Build this once. Call it from Agent 18 outputs, from API test runners, from UI test frameworks. The pattern is universal.
