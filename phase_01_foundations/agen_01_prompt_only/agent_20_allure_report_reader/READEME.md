# Agent 20 — allure_report_reader

## Purpose
Agent 20 reads an Allure test report in JSON format and extracts a clean, structured summary: total test count, counts by status (passed, failed, broken, skipped), and a list of failed test names with their error messages. It converts a complex, deeply nested JSON report into a flat, machine-readable summary that downstream agents — and humans — can act on immediately.

## What This Agent Introduces
**Report parsing as a pipeline component** — the concept of treating an external artifact (the test report) as structured data input to the agent system, not just a file for humans to read in a browser.

## How It Works
1. Accept a path to an Allure result JSON file or a JSON string directly.
2. Load and parse the JSON.
3. Walk through the test results array and accumulate counts by status.
4. For each failed or broken test, extract the test name and the top-level error message.
5. Return a summary dict: {total, passed, failed, broken, skipped, failures: [{name, error}]}.

## What It Is NOT
- No trend analysis across multiple runs
- No JIRA ticket creation or bug logging
- No anomaly detection or historical comparison
- No routing decisions

## Scope
- Loading and parsing Allure JSON report files
- Counting results by status category
- Extracting failure details (name + error message) for failed and broken tests
- Returning a flat, structured summary dict

## Key Lesson
The Allure HTML dashboard is for humans. The Allure JSON is for machines. Agent 20 reads the machine format and produces a summary that every downstream agent in the QA pipeline can consume — from JIRA integration to anomaly detection to executive dashboards.

## Next Step
Once Agent 20 is complete, the project proceeds to Agent 21, continuing to build toward the full AI-powered QA platform.
