Agent 14 — reflection — Fundamentals

IS:
✔️ Evaluates structural correctness of agent outputs (type, shape, required fields)
✔️ Checks consistency between input context and produced output
✔️ Returns a machine-readable reflection report with anomaly list and health score

IS NOT:
✗ Does not modify, correct, or retry the output it evaluates
✗ Does not route to another agent or take any action
✗ Does not store its findings in memory

Input: Context object (dict) + agent output (dict or string from a previous agent)
Output: Reflection report { has_errors: bool, anomalies: [str], health_score: float, checks_run: int, checks_passed: int }
