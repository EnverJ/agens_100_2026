Agent 14 — Limitations

This agent does NOT:
• Fix, modify, or retry the outputs it evaluates
• Detect semantic errors — only structural ones (type, shape, required fields)
• Remember past reflection results — each invocation is stateless
• Reason about why an anomaly occurred or what caused it
• Guarantee that a health_score of 1.0 means the output is correct — only that it passed all structural checks

We change one variable at a time.
