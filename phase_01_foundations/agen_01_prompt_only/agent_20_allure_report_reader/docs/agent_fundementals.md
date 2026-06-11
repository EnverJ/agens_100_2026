Agent 20 — allure_report_reader — Fundamentals

IS:
✔️ Parses Allure JSON result files (or JSON strings) from disk
✔️ Counts test results by status: total, passed, failed, broken, skipped
✔️ Extracts failure details (test name + error message) for every failed or broken test

IS NOT:
✗ Does not analyze trends across multiple runs or compare to historical data
✗ Does not create JIRA tickets, send alerts, or take any action on failures
✗ Does not write, modify, or delete the report file

Input: File path to Allure JSON result file, or raw JSON string
Output: Summary dict { total: int, passed: int, failed: int, broken: int, skipped: int, failures: [{ name: str, error: str }] }

SDET Note: Run this on a real Allure report from your test suite. The summary it produces in milliseconds replaces manual dashboard reading.
