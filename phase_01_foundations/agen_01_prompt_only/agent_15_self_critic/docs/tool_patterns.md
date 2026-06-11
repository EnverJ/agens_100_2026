Tool Patterns — Agent 15

Agent 15 uses no tools and makes no external calls. It follows the Rubric Evaluation Pattern: apply a fixed set of named, weighted rules to an input and return a numeric result.

This pattern is common in testing frameworks (pytest scoring, code quality linters, CI quality gates) and maps directly to SDET practices. A rubric is essentially an assertion suite — each rule is an assertion, and the score represents how many assertions passed.

Pattern in use:
  Input dicts → Rule set (loop) → Deduction accumulator → Score + violations list

The rubric itself should be stored as a separate configuration (dict or YAML) so that rules can be tuned without changing the evaluation logic. This separation of configuration from logic is the same principle that makes prompt templates in earlier agents maintainable.
