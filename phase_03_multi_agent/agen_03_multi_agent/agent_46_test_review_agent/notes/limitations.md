# Limitations — Agent 46: Test Review Agent

## What This Agent Does NOT Do

**Does not execute tests**
Agent 46 reviews test case definitions — names, descriptions, steps, assertions as text. It does not run any test framework, connect to a test runner, or produce pass/fail results. Execution is a separate concern handled by dedicated execution agents.

**Does not generate missing tests**
When Agent 46 identifies a gap — for example, "no test for the null input case" — it reports the gap in the review report. It does not generate the missing test case. Gap remediation is the responsibility of Agent 32 (test plan generator), which should be re-invoked with the gap list as input.

**Does not parse actual test code**
Agent 46 reviews test case descriptions (structured dicts with text fields). It does not parse Python, Java, or JavaScript test code. It cannot analyze an actual test file to determine what assertions are present. If the input is raw code rather than a structured test case description, a preprocessing step is required.

**Does not guarantee all gaps are found**
LLM-based review is probabilistic. The agent may miss gaps, particularly for domain-specific edge cases that are not well-represented in the quality criteria or that require deep business domain knowledge. The review is a best-effort quality signal, not a formal verification.

**Does not integrate with CI/CD directly**
Agent 46 returns a review report dict. It does not post results to GitHub Actions, block pull requests, send Slack notifications, or write to any external system. Downstream integration is handled by the orchestrator or by Agent 49 (JIRA integration).

**Does not update the knowledge base**
If Agent 46 encounters a new category of gap not covered in the existing quality criteria, it does not update Agent 27's knowledge base. Criteria evolution requires a separate, human-supervised process.

**Does not handle more than 50 test cases per call**
The prompt context limits the number of test cases that can be reviewed in a single invocation. For larger test suites, the orchestrator must batch the input and aggregate the review reports.
