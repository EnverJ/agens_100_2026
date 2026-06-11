Agent 16 — error_correcting — Fundamentals

IS:
✔️ Maps rule violations from Agent 15's critique to specific fix suggestion templates
✔️ Maps anomalies from Agent 14's reflection report to targeted suggestions
✔️ Returns a prioritized list of actionable { error_code, description, suggested_fix } objects

IS NOT:
✗ Does not apply, execute, or automate any of the suggested fixes
✗ Does not route or branch the pipeline based on suggestions
✗ Does not use LLM reasoning — all suggestions come from pre-defined templates

Input: Critique dict (from Agent 15) + reflection report (from Agent 14)
Output: List of suggestion objects [{ error_code: str, description: str, suggested_fix: str }]
