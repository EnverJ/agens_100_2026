Agent 19 — Limitations

This agent does NOT:
• Execute or trigger test runs — it only evaluates results that are handed to it
• Support fuzzy or partial matching — comparison is exact; "200 OK" does not match "200"
• Handle dynamic schemas where field names or types change at runtime
• Log, store, or aggregate PASS/FAIL results across multiple invocations
• Infer the expected output from context — expected must always be explicitly provided

We change one variable at a time.
