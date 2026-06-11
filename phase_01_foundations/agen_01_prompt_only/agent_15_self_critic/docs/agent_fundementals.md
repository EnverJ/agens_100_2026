Agent 15 — self_critic — Fundamentals

IS:
✔️ Applies a named, weighted scoring rubric to evaluate output quality
✔️ Produces a numeric score (0–100) and a pass/fail determination
✔️ Returns a structured critique object with a list of rule violations

IS NOT:
✗ Does not modify, rewrite, or improve the output it critiques
✗ Does not make routing decisions — downstream agents act on the critique
✗ Does not use LLM judgment — all checks are deterministic rule evaluations

Input: Agent output (dict) + reflection report from Agent 14 (dict)
Output: Critique dict { score: int, passed: bool, violations: [str], threshold: int }
