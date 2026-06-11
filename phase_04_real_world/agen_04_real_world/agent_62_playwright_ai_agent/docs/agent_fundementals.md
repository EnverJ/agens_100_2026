# Agent Fundamentals: Playwright AI Agent

## IS
- A UI test automation agent powered by Playwright Python
- An LLM-assisted locator generator — no hard-coded selectors
- A test scenario interpreter — converts natural language scenarios to Playwright action plans
- A failure evidence collector — screenshots on failure
- Stateless per test run — each invocation is independent

## IS NOT
- Not a visual regression tool (no pixel comparison)
- Not a cross-browser parallel runner
- Not a test framework (no pytest integration)
- Not a UI scraper or data extractor
- Not a security scanner or accessibility auditor

## Input
```python
{
  "url": "https://staging.myapp.com/login",
  "test_scenario": "User logs in with valid credentials and sees the dashboard",
  "browser": "chromium",
  "headless": True,
  "credentials_hint": "email: test@example.com, password: Test1234!"
}
```

## Output
```python
{
  "verdict": "FAIL",
  "steps_log": [
    {"step": 1, "action": "fill email", "status": "PASS"},
    {"step": 2, "action": "fill password", "status": "PASS"},
    {"step": 3, "action": "click Login button", "status": "PASS"},
    {"step": 4, "action": "assert dashboard visible", "status": "FAIL",
     "error": "Locator 'get_by_text(Dashboard)' not found after 5s"}
  ],
  "screenshot_path": "/tmp/agent_62_failure_1234.png",
  "duration_ms": 3820
}
```
