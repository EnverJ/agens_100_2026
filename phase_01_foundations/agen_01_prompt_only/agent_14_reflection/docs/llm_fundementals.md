LLM Fundamentals — Agent 14

• Agent 14 does not make an LLM call. All evaluation is deterministic Python logic. This is intentional — structural checks do not require language understanding, and using an LLM here would add latency and nondeterminism to a layer that should be fast and reliable.

• The distinction between structural errors (wrong type, missing field) and semantic errors (output contradicts context meaning) is important. Agent 14 catches structural errors only. Semantic error detection would require an LLM, but also a ground truth — neither of which is available at this stage.

• The health_score (0.0–1.0) is a heuristic signal, not ground truth. Downstream agents that consume it must treat it as an indicator, not a guarantee. An LLM consuming this score as context should be prompted to treat it accordingly.

• If an LLM were added to Agent 14 in a future version, the appropriate use would be as a semantic consistency checker: "given this input and output, does the response make sense?" This is a distinct LLM pattern — evaluation, not generation.

• Structured output discipline matters here: the reflection report must be a predictable dict schema. Any agent downstream that reads it must be able to rely on fixed field names. This is the same structured-output principle introduced in earlier agents, applied to meta-level pipeline data.
