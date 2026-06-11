# Agent 62 — Playwright AI Agent

## Purpose
Agent 62 is the first UI test agent in the project. It uses Playwright Python to automate browser interaction, but rather than relying on hard-coded selectors, it uses an LLM to interpret the page structure, suggest locators, and determine assertion strategies. Given a natural language test scenario, it navigates a real web application, performs actions, and returns a pass/fail verdict with a screenshot as evidence.

## What This Agent Introduces
**AI-Assisted UI Testing** — LLM-generated locators and assertion strategies applied to real browser automation with Playwright.

## How It Works
1. Accept a base URL, test scenario description, and optional page hints (title, key element descriptions).
2. Launch a Playwright browser instance (Chromium, headless).
3. Navigate to the URL and capture the page HTML structure (truncated to key landmarks).
4. Send the HTML snapshot plus the test scenario to the LLM, asking it to produce a Playwright action plan: locators, actions (click/fill/assert), and expected outcomes.
5. Execute the action plan step by step using Playwright's Python API.
6. On assertion failure or exception, capture a screenshot.
7. Return structured result: PASS/FAIL, step-by-step log, and screenshot path if applicable.

## What It Is NOT
- No visual regression testing — pixel comparison is not performed
- No cross-browser parallel execution — single browser instance per run
- No test framework integration (pytest fixtures, etc.) — standalone agent
- No dynamic page re-analysis mid-test — page is analyzed once at start

## Scope
- Single page flow per invocation (login, search, checkout step — not full multi-page journeys)
- Chromium only by default; browser is configurable
- Screenshot taken on failure, not at every step
- LLM produces the action plan; the agent executes it deterministically

## Key Lesson
Brittle selectors are the #1 cause of UI test maintenance cost. By letting an LLM interpret page structure and suggest resilient locators (role-based, text-based, aria), this agent demonstrates that AI can reduce the maintenance burden of UI test suites significantly.

## Next Step
Once Agent 62 is complete, proceed to Agent 63.
