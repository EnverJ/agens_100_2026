# Agent 18 — requirement_to_testcase_agent

## Purpose
Agent 18 reads a plain-text software requirement and uses an LLM with a carefully crafted SDET system prompt to generate structured test cases. The output covers the happy path, edge cases, and negative scenarios — the same coverage a senior tester would produce manually, delivered in seconds. This is the first SDET-specific agent in the project.

## What This Agent Introduces
**LLM-as-test-engineer** — using prompt framing to transform the LLM from a general chatbot into a domain-specific test case generator. The key insight is that the intelligence is in the prompt, not in the code.

## How It Works
1. Receive a requirement string (plain English description of a feature or behavior).
2. Build a system prompt that frames the LLM as a senior SDET: "You are a senior software test engineer. Given a requirement, produce structured test cases..."
3. Inject the requirement into the user prompt.
4. Call the LLM and request structured JSON output.
5. Parse and return the response as a list of test case objects: [{id, title, steps, expected_result, type}].

## What It Is NOT
- No test execution
- No memory of previously generated test cases
- No validation that the generated cases are correct
- No tool calls to external systems

## Scope
- Parsing a plain-text requirement string
- Engineering an SDET-framed system prompt
- Calling the LLM with structured output instructions
- Parsing and returning the JSON test case list

## Key Lesson
The LLM is not just a chatbot — it is a domain expert when given the right framing. A well-crafted system prompt turns a general-purpose model into a specialist test engineer. What took a junior tester hours to write can be generated in seconds. The quality of the output depends almost entirely on the quality of the prompt.

## Next Step
Once Agent 18 is complete, the project proceeds to Agent 19 — Test Output Validator, which provides the assertion engine to validate test run results.
