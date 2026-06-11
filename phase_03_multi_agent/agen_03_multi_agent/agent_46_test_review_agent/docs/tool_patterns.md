# Tool Patterns — Agent 46: Test Review Agent

## LLM-as-Reviewer

**Pattern**: Use the LLM as a judge or evaluator rather than a generator. The model receives content and a rubric and returns scores and feedback.

**Why here**: Generated test cases need quality assessment that requires semantic understanding — determining whether an assertion is "specific enough" cannot be done with string matching or static analysis. The LLM can read a test case description and apply nuanced criteria that would take hundreds of rules to encode manually.

**Implementation**: Construct a prompt that includes the rubric criteria, the test case definition, and the scoring scale. Request structured JSON output. Parse the response into per-dimension scores.

---

## Rubric Scoring

**Pattern**: Define an explicit numeric scale with anchored examples at each level before asking the LLM to score.

**Why here**: Without anchoring, LLMs tend to cluster scores at the high end of a scale (leniency bias). Providing "score 1 = X, score 3 = Y, score 5 = Z" with concrete examples normalizes the distribution and makes scores comparable across test cases.

**Implementation**: Include the rubric scale in the system prompt. Use few-shot examples with their scores to calibrate the model before it evaluates real test cases.

---

## Knowledge Base Injection

**Pattern**: Load external criteria or domain knowledge at runtime and inject it into the prompt as context.

**Why here**: The quality criteria for test cases (critical path checklist, naming conventions, required edge case categories) live in Agent 27's knowledge base, not in this agent's code. Injecting them at runtime keeps the review agent decoupled from the criteria and allows criteria to evolve independently.

**Implementation**: Call Agent 27 at the start of each review session. Serialize the returned criteria dict into a structured text block. Prepend to the system prompt before processing any test cases.

---

## Structured Review Output

**Pattern**: Request JSON-formatted output from the LLM for all review results, specifying the schema explicitly in the prompt.

**Why here**: The review report must be machine-readable so downstream agents (Agent 49 for JIRA ticket creation, Agent 32 for regeneration) can consume it without brittle text parsing.

**Implementation**: Specify the output schema in the prompt: field names, types, and valid value ranges. Use response_format constraints where available. Validate the parsed JSON against the expected schema before returning.

---

## Quality Gate Pattern

**Pattern**: Insert a review/validation agent between a generator agent and an executor agent to catch low-quality output before it propagates downstream.

**Why here**: Low-quality test cases passed directly to a test executor waste execution time and produce misleading results (tests that pass because they assert nothing meaningful). The quality gate pattern mirrors the code review step in software development.

**Implementation**: In the orchestrator pipeline: Agent 32 generates → Agent 46 reviews → if overall_quality_score < threshold, route back to Agent 32 for regeneration → else route to test executor. The threshold (e.g., 3.5 / 5.0) is a configurable parameter, not hardcoded.
