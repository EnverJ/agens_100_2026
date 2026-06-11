Agent 18 — requirement_to_testcase_agent — Fundamentals

IS:
✔️ Frames the LLM as a senior SDET via a domain-specific system prompt
✔️ Generates structured test cases (happy path, edge cases, negative scenarios) from a requirement string
✔️ Returns a JSON list of test case objects with a fixed schema: {id, title, steps, expected_result, type}

IS NOT:
✗ Does not execute any test cases
✗ Does not validate whether generated test cases are correct or complete
✗ Does not store or remember previously generated test cases

Input: Requirement string (plain English feature or behavior description)
Output: JSON list of test cases [{ id, title, steps: [str], expected_result, type }]

SDET Note: Try this on a real feature requirement — the output will surprise you with its breadth.
