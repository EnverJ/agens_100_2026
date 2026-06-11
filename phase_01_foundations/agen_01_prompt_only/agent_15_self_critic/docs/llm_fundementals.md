LLM Fundamentals — Agent 15

• Agent 15 does not make an LLM call. This is a deliberate stage gate: establish a deterministic baseline scorer before introducing LLM-as-judge, which adds variance and requires prompt engineering of its own.

• LLM-as-judge is a real and powerful pattern — later agents in this project use it. But it requires calibration: you need to know what a good score looks like before you can trust an LLM to assign one. The rule-based scorer here provides that calibration baseline.

• Structured output discipline is critical at this layer. The critique dict must have a fixed schema so that Agent 16 (which reads it) and any other downstream consumer can rely on specific field names. Changing the schema breaks the pipeline.

• The score is a signal, not a ground truth. An LLM that later consumes the critique score as part of its context should be prompted with that caveat: "the following quality score was assigned by a rule-based rubric, not by semantic understanding."

• Threshold tuning is a form of prompt engineering applied to deterministic systems: lowering the pass threshold makes the system more permissive; raising it makes it stricter. The builder should experiment with different thresholds against real outputs to find the right operating point.
