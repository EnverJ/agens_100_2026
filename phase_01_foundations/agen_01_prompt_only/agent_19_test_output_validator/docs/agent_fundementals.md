Agent 19 — test_output_validator — Fundamentals

IS:
✔️ Compares actual test output to an expected value (exact comparison mode)
✔️ Validates actual output against an expected schema (field presence + type checking mode)
✔️ Returns a structured result: { status: "PASS"|"FAIL", reason: str, diff: dict }

IS NOT:
✗ Does not execute tests or produce the actual output it validates
✗ Does not log bugs, create tickets, or route based on PASS/FAIL
✗ Does not handle partial matches or fuzzy comparison — comparison is exact

Input: actual (dict or str) + expected (value or schema dict) + mode ("value"|"schema")
Output: { status: str, reason: str, diff: dict }

SDET Note: This is the foundation of any AI-powered assertion library. Reuse it everywhere.
