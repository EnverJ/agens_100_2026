Agent 15 — Limitations

This agent does NOT:
• Use LLM judgment — cannot evaluate semantic quality, coherence, or relevance to user intent
• Modify, rewrite, or improve the output it scores
• Learn from past critiques or adjust its rubric based on feedback
• Handle outputs that don't conform to the expected dict structure gracefully — malformed inputs may cause scoring errors
• Guarantee that a passing score (>= 70) means the output is actually correct — only that it satisfied the defined rules

We change one variable at a time.
