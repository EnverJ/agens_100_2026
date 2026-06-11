# LLM Fundamentals — Agent 46: Test Review Agent

## LLM-as-Evaluator Pattern

The core pattern here is LLM-as-evaluator: using the language model not to generate content but to judge it. The LLM is given a rubric, a piece of content (a test case), and asked to score the content against the rubric. This is a well-established pattern in LLM systems — often called "LLM-as-judge" — and it produces reliable results when the rubric is explicit and the scoring criteria are unambiguous. For test review, the rubric must define what a score of 3 means vs a score of 5 to avoid subjective drift across evaluations.

## Rubric-Based Scoring Prompts

Prompts for rubric-based scoring should be structured, not open-ended. Instead of "Is this a good test?", the prompt should say: "Score this test case on assertion specificity from 1 to 5, where 1 = no assertions, 3 = generic assertion (assert status == 200), 5 = precise assertion (assert response.body.error_code == 'CARD_DECLINED'). Return only a JSON object." Anchoring the scale with concrete examples at each level dramatically reduces scoring variance and makes the output more consistent across different test cases.

## Knowledge Base Injection into Review Prompt

The quality criteria from Agent 27 are injected into the system prompt at runtime, not hardcoded. This means the rubric can evolve — new critical paths can be added to the knowledge base, naming conventions can change — without modifying the review agent's code. The injection pattern is: load criteria dict from Agent 27, serialize to a structured text block, prepend to the review prompt as context. The LLM then uses these criteria as the authoritative standard during evaluation.

## Structured Output for Review Reports

The review prompt must request structured output (JSON) to enable downstream consumption. Free-text review reports are human-readable but not machine-processable. The prompt should specify the exact schema: `{ "coverage_score": int, "edge_case_score": int, "assertion_score": int, "naming_score": int, "notes": str }`. Using a schema in the prompt, combined with response_format=json_object if the API supports it, eliminates parsing failures and ensures the report can be consumed by Agent 49 (JIRA integration) or any downstream agent.

## Few-Shot Examples of Good vs Bad Test Cases in Prompt

Including one or two annotated examples in the review prompt significantly improves scoring accuracy. A "bad test case" example — one with vague assertions and no edge case coverage — paired with its low scores helps the LLM calibrate what a 1 or 2 looks like. A "good test case" example with specific assertions and clear steps paired with high scores anchors the top of the scale. These few-shot examples function as implicit rubric calibration and reduce the tendency of LLMs to score everything at the high end of a numeric scale (a known bias in LLM-as-evaluator systems).
