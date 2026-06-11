LLM Fundamentals — Agent 16

• Agent 16 does not make an LLM call. Fix suggestions come from a template lookup table written by the builder. This is intentional at this stage — templates provide a controlled, verifiable baseline before LLM-generated suggestions are introduced.

• The future evolution of this agent — LLM-powered fix suggestion — would use an evaluation prompt: "given this error code, this context, and this output, what specific change would fix the problem?" That prompt requires few-shot examples. The templates written here become those examples.

• Prompt engineering for fix suggestion is different from prompt engineering for generation. The model must be constrained to produce concrete, specific suggestions — not vague advice. Techniques like structured output (JSON mode), constraint prompts ("respond with a single actionable step"), and few-shot examples are all applicable.

• When LLM-generated suggestions are eventually used, they must be validated just like any other LLM output. The suggestion should be structurally sound (correct fields, non-empty), relevant (addresses the flagged error), and safe (does not recommend destructive actions). Agent 19's validation pattern applies here.

• The separation between suggestion and application is a safety pattern: no LLM output should be executed without a human or deterministic validation step in between. This principle becomes critical when agents gain the ability to modify code or configuration automatically.
