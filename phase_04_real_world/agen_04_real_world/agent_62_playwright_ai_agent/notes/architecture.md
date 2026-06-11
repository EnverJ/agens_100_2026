# Architecture: Playwright AI Agent

```
┌─────────────────────────────────────────────────────────────────┐
│                         CALLER / USER                           │
│  { url, test_scenario, browser="chromium", headless=True }      │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                 Playwright Browser Launcher                      │
│                                                                 │
│   playwright.chromium.launch(headless=True)                     │
│   page.goto(url)                                                │
│   page.wait_for_load_state("networkidle")                       │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│               Page Structure Extractor                          │
│                                                                 │
│   Grabs: page.title(), page.content() (truncated)              │
│   Extracts landmark roles, button labels, form fields           │
│   Produces: html_summary (compact representation)              │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                   LLM — Test Planner                            │
│                                                                 │
│  Input: html_summary + test_scenario                           │
│  Output: action_plan = [                                       │
│    { step: 1, action: "fill",                                  │
│      locator: "get_by_label('Email')",                         │
│      value: "test@example.com" },                              │
│    { step: 2, action: "click",                                 │
│      locator: "get_by_role('button', name='Login')" },        │
│    { step: 3, action: "assert_text",                          │
│      locator: "get_by_text('Welcome')",                       │
│      expected: "Welcome" }                                      │
│  ]                                                              │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                  Action Executor (Playwright)                   │
│                                                                 │
│   For each step in action_plan:                                │
│     eval(f"page.{locator}.{action}()")                         │
│     log step result                                             │
│     on failure → page.screenshot(path=screenshot_path)         │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
              { verdict: PASS/FAIL, steps_log,
                screenshot_path (if FAIL), duration_ms }
```
