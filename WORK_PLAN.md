# Work Plan: 100 Agents in 2026 — 1 Hour/Day Starting July

## Context

Naveen K is a Senior SDET (Zomato, 8 years experience) building a disciplined 100-agent project
that blends general AI agent education with SDET-specific agent capabilities. Agents 01–12 are
complete. Agents 13–100 (88 agents) need to be built, starting July 2026, with ~1 hour/day.

The project constitution (hardCore.txt) mandates:
- One agent at a time, no skipping
- Reflection after each agent (mandatory documentation)
- Agent is complete ONLY when explicitly declared
- No copy-paste; understanding is mandatory

This constraint makes the 1-hour session the fundamental unit of work.

---

## Time Estimation Methodology

From full analysis of all 12 existing agents (actual line counts measured):

| Agent | Lines | Actual effort | Notes |
|---|---|---|---|
| 01 | 43 | ~30 min | Simple OpenAI wrapper |
| 02 | 32+97-line README | ~90 min | Different LLM library, docs heavy |
| 03 | 74 | ~45 min | Memory list introduced |
| 04 | 78 + tools.py | ~60 min | First tool integration |
| 05 | 106 + 12-line tools + 124-line README | ~120 min | Multi-tool, heaviest so far |
| 06 | 39 + 11-line tools | ~45 min | Simplified after 05 |
| 07 | 21 | ~30 min | System prompt only |
| 08 | 12 + 80-line README | ~45 min | Tiny code, detailed spec |
| 09–11 | 19–28 each | ~20 min each | Pure decision/assembly logic |
| 12 | 44 | ~30 min | Session memory management |

**Average across all 12: ~45 min coding, ~8 min docs. Total per agent: ~53 min.**

Important observation: `progress/daily_logs.md`, `progress/reflections.md`, and
`progress/roadmap.md` are **empty across all 12 agents**. The per-session rhythm below
makes these mandatory — they're the insurance against context loss over 6 months.

| Complexity Category | Typical Agent | Code Volume | Sessions Needed |
|---|---|---|---|
| Light | 13–17, 21, 25 | 20–45 lines | 1 session |
| Medium | 18–20, 23–24, 27 | 50–100 lines | 1–2 sessions |
| Heavy | 43, 49, 56, 61–78 | 100–200 lines + external APIs | 2–3 sessions |
| Very Heavy | 79–99 | 200+ lines, architecture decisions | 3–5 sessions |
| Capstone | 100 | Full system integration | 7 sessions |

Key overhead driver: every SDET agent that touches a real external tool (Playwright, JMeter,
JIRA API, Allure, Jenkins) adds at least 1 extra session for setup, learning the Python SDK,
and debugging integration.

---

## Schedule: July 2026 → December 2026

### JULY — Phase 1 Completion + Phase 2 Foundation
**Target: Agents 13–28 (16 agents) | 31 days**

| Week | Agents | Focus | Notes |
|---|---|---|---|
| Jul 1–7 | 13–17 | Phase 1 general tail | long_term_memory, reflection, self_critic, error_correcting, input_router — familiar patterns, 1/day |
| Jul 8–14 | 18–20 | **First SDET agents** | requirement_to_testcase, test_output_validator, allure_report_reader — budget 2 days each; first real LLM→SDET bridge |
| Jul 15–21 | 21–24 | Phase 2 memory start | short_term_memory (easy), long_term_memory (**vector DB spike: 3 days** — learn ChromaDB), test_run_history_analyzer, test_history_memory |
| Jul 22–31 | 25–28 | Reasoning foundations | working_memory, retrieval, test_knowledge_base, chain_of_thought |

**July checkpoint:** Agent 28 complete. First Allure-reading agent done. Vector DB understood.

---

### AUGUST — Memory Completion + Multi-Agent Start
**Target: Agents 29–48 (20 agents) | 31 days**

| Week | Agents | Focus | Notes |
|---|---|---|---|
| Aug 1–7 | 29–33 | Reasoning agents | deductive, inductive, root_cause_analyzer (**SDET spike: 2 days**), planning, goal_decomposition |
| Aug 8–14 | 34–37 | Bug reasoning + SDET | bug_hypothesis_generator (2 days), evidence_evaluator, decision_tree, flaky_test_detector (**SDET spike: 2 days** — statistical pattern matching) |
| Aug 15–21 | 38–42 | Reasoning tail + Multi-agent start | causal_reasoner, similar_failure_finder, meta_reasoner, manager_worker, orchestrator |
| Aug 22–31 | 43–48 | Multi-agent core | test_suite_orchestrator (**architecture spike: 3 days** — first time coordinating multiple agents), consensus, debate, test_review_agent, specialist, generalist |

**August checkpoint:** Agent 48 complete. First multi-agent test system running. Flaky test reasoning implemented.

---

### SEPTEMBER — Multi-Agent SDET + Real-World Start
**Target: Agents 49–65 (17 agents) | 30 days**

| Week | Agents | Focus | Notes |
|---|---|---|---|
| Sep 1–7 | 49–52 | Critical SDET integrations | jira_integration_agent (**spike: 2 days** — JIRA REST API, Python client), aggregator, test_pipeline_agent, parallel_executor |
| Sep 8–14 | 53–57 | Parallel + mobile | parallel_test_runner (**spike: 2 days**), broadcaster, filter, mobile_test_agent (**spike: 3 days** — Appium + AI), test_result_merger |
| Sep 15–21 | 58–62 | Real-world phase entry | arbitrator, supervisor, reporter, rest_api_intelligence_agent (**spike: 2 days**), playwright_ai_agent (**spike: 3 days** — Playwright Python + LLM) |
| Sep 22–30 | 63–65 | Data + test tools | data_extraction, test_data_generator (**spike: 2 days**), bug_reporter |

**September checkpoint:** Agent 65 complete. JIRA integration live. Playwright AI agent working. Mobile test agent running.

---

### OCTOBER — Heavy SDET Real-World
**Target: Agents 66–82 (17 agents) | 31 days**

| Week | Agents | Focus | Notes |
|---|---|---|---|
| Oct 1–7 | 66–68 | CI/CD + Coverage | jenkins_pipeline_agent (**spike: 3 days** — Jenkins API + quality gates), code_generator, code_coverage_agent (**spike: 2 days**) |
| Oct 8–14 | 69–72 | Environment + Allure | database_query, test_environment_manager (**spike: 2 days**), document_processor, allure_intelligence_agent (**spike: 3 days** — deep Allure JSON parsing, trend analysis, Slack formatting) |
| Oct 15–21 | 73–77 | Traffic + Defects | scheduler, high_traffic_test_selector (**spike: 2 days** — Zomato/Flipkart peak-event logic), summarizer, classifier, defect_classifier (**spike: 2 days**) |
| Oct 22–31 | 78–82 | JMeter + AI product | jmeter_intelligence_agent (**spike: 3 days** — JMeter XML parsing + anomaly detection), ai_product_tester (**spike: 3 days** — hallucination testing, prompt injection), report_generator, test_suite_evaluator, test_benchmarker |

**October checkpoint:** Agent 82 complete. JMeter intelligence running. First AI product tester built. Allure intelligence with Slack alerts.

---

### NOVEMBER — Meta Agents
**Target: Agents 83–93 (11 agents) | 30 days**

| Week | Agents | Focus | Notes |
|---|---|---|---|
| Nov 1–10 | 83–85 | Optimization + Healing | optimizer, self_healing_test_agent (**major spike: 5 days** — locator healing, Playwright selector regeneration, assertion auto-fix), curriculum_designer |
| Nov 11–20 | 86–89 | Strategy + Config | meta_learner, test_strategy_agent (**spike: 3 days** — reads project context, generates test strategy doc), config_manager, debugger |
| Nov 21–30 | 90–93 | Testing intelligence | ai_test_runner (**spike: 3 days** — risk-based prioritization), deployer, versioner, test_documentation_agent (**spike: 2 days**) |

**November checkpoint:** Agent 93 complete. Self-healing test agent is the flagship milestone — this alone is a major portfolio piece.

---

### DECEMBER — Advanced SDET + Capstone
**Target: Agents 94–100 (7 agents) | 31 days**

| Week | Agents | Focus | Notes |
|---|---|---|---|
| Dec 1–7 | 94–95 | Security + Performance | security_test_agent (**spike: 3 days** — SQL injection, XSS, auth testing probes), performance_profiler |
| Dec 8–14 | 96–98 | Chaos + Debt | chaos_test_agent (**spike: 3 days** — chaos engineering, resilience testing), reliability_checker, test_debt_analyzer (**spike: 2 days**) |
| Dec 15–18 | 99 | Simulation | simulator |
| Dec 19–31 | **100** | **CAPSTONE** | agentic_qa_platform — **7 days minimum**. Integrates: JIRA agent + Allure agent + parallel runner + self-healing + test strategy. Given a PR diff, orchestrates full QA cycle. Interview-ready portfolio piece. |

**December checkpoint:** 100/100 agents complete.

---

## Summary Timeline

| Month | Agents | Cumulative | Key Milestone |
|---|---|---|---|
| July | 13–28 | 28/100 | First SDET agents live, Vector DB learned |
| August | 29–48 | 48/100 | Multi-agent test orchestration |
| September | 49–65 | 65/100 | JIRA + Playwright + Mobile AI agents |
| October | 66–82 | 82/100 | JMeter intelligence + AI product testing |
| November | 83–93 | 93/100 | Self-healing test agent (flagship) |
| December | 94–100 | 100/100 | Full agentic QA platform capstone |

**Total duration: 6 months (Jul–Dec 2026)**
**Total sessions: ~184 (1/day)**
**Average pace: 1 agent per 2.1 days**

---

## Complexity Spikes — Pre-plan These

These agents require multi-day setup that doesn't produce working code on day 1.
Budget extra time (don't try to rush them):

| Agent | Spike Reason | Budget |
|---|---|---|
| 22 long_term_memory | First vector DB — learn ChromaDB from scratch | 3 days |
| 43 test_suite_orchestrator | First multi-agent architecture decision | 3 days |
| 56 mobile_test_agent | Appium Python client + AI integration | 3 days |
| 62 playwright_ai_agent | Playwright Python + LLM tool calling | 3 days |
| 66 jenkins_pipeline_agent | Jenkins REST API + quality gates | 3 days |
| 72 allure_intelligence_agent | Deep Allure JSON + trend analysis | 3 days |
| 78 jmeter_intelligence_agent | JMeter XML parsing + anomaly logic | 3 days |
| 84 self_healing_test_agent | Selector regeneration + assertion auto-fix | 5 days |
| 100 agentic_qa_platform | Full system integration capstone | 7 days |

---

## Per-Session Rhythm (1 hour)

| Time | Activity |
|---|---|
| 0–5 min | Re-read previous session's notes/next_step.md |
| 5–45 min | Code |
| 45–55 min | Update notes/ and progress/ files |
| 55–60 min | Write next_step.md for tomorrow |

This enforces the hardCore.txt discipline of reflection after each session and prevents context loss between days.

---

## Critical Files to Keep Updated

- `progress.md` (root) — update agent status after each completion
- Each agent's `progress/daily_logs.md` — daily 2-3 line log
- Each agent's `notes/next_step.md` — written at end of each session
- Each agent's `progress/reflections.md` — written when declaring agent complete

---

## What Changes Nothing

- Missing a day: the project absorbs it. Don't compensate by rushing the next day.
- An agent taking longer than expected: normal for spikes. The plan has buffer.
- Feeling behind in October: you're not — Phase 4 is intentionally heavier.
