Agent 20 — Limitations

This agent does NOT:
• Compare results across multiple runs or identify regressions — it reads a single report per invocation
• Detect anomalies, classify failures, or reason about what caused a failure
• Handle Allure JSON schema variations across Allure versions — field paths are hardcoded to a specific format
• Write, update, or delete the Allure report file it reads
• Process report formats other than Allure JSON (no JUnit XML, no pytest JSON, no Cucumber support at this stage)

We change one variable at a time.
