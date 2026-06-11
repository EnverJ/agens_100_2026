# Architecture — Agent 46: Test Review Agent

## Data Flow

```
Test Cases (from Agent 32)
         │
         ▼
[Test Review Agent]
         │
         ├── Load quality criteria from knowledge base
         │
         ├── Evaluate each test case:
         │     ├── Path coverage check
         │     ├── Edge case check
         │     ├── Assertion specificity check
         │     └── Naming convention check
         │
         └── Generate review report
                   │
                   ▼
         Review Report:
         { scores: [...], gaps: [...], recommendations: [...] }
```

## Component Breakdown

**Input Layer**
- Accepts a list of test case dicts from Agent 32 or any upstream generator
- Each test case dict contains: test_name, description, preconditions, steps, expected_result, assertions

**Knowledge Base Loader**
- Fetches quality criteria from Agent 27's knowledge base
- Criteria include: critical path checklist, assertion specificity standards, naming conventions, required edge case categories

**Evaluation Engine (LLM Call)**
- Constructs a review prompt with the quality criteria injected as context
- Sends each test case to the LLM with the rubric
- Parses the LLM response into structured scores per dimension

**Gap Detector**
- Compares the set of evaluated test cases against the critical path checklist
- Identifies which critical paths have no corresponding test case
- Flags missing edge case categories (e.g., no null input tests, no timeout tests)

**Report Generator**
- Assembles per-test scores, gap list, and recommendations into a structured dict
- Computes an overall_quality_score as the mean of all per-test scores
- Returns the review report to the caller

## Key Design Decisions

- Review is done per test case, not holistically, to produce actionable per-test scores
- Knowledge base criteria are injected into the prompt, not hardcoded, so the rubric can evolve without code changes
- The agent does not call Agent 32 to fix gaps — it reports gaps and leaves remediation to the orchestrator
