# LLM Fundamentals — Agent 42: Orchestrator

- **Prompt chaining**: Each stage in the pipeline is a separate LLM call with its own system prompt and user message. Prompt chaining means the output of one LLM call becomes part of the input to the next. The quality of the final result depends on the cumulative quality of each chained call — errors introduced early amplify in later stages.

- **Context passing between stages**: When Agent A's output is passed to Agent B, only the output is forwarded — not Agent A's full conversation history. Each agent starts with a clean context window, receiving only what the orchestrator explicitly passes. This keeps context windows small and focused, but requires careful design of what information each stage needs to carry forward.

- **Pipeline state management**: The orchestrator maintains the state of the pipeline in memory — the original input, each stage's output, and the current stage number. This state is not stored externally; it exists only during execution. The orchestrator must not lose this state between stage calls, which means it runs as a single uninterrupted function call rather than multiple separate invocations.

- **Sequential vs parallel LLM calls**: Sequential calls (one at a time) are simpler to reason about and debug but are slower — total latency is the sum of all stage latencies. Parallel calls (multiple LLM calls simultaneously) reduce latency but require independent inputs. In a pipeline, each stage depends on the previous stage's output, which forces sequential calls. Parallelism is only possible when stages are independent of each other.

- **Output format contracts between agents**: For a pipeline to work, each stage must produce output in a format the next stage expects. This is typically enforced by the system prompt (instructing the LLM to return JSON in a specific schema) combined with output parsing in the orchestrator. If Agent A returns unstructured prose but Agent B expects a JSON object, the orchestrator must either parse Agent A's output or redesign Agent A's prompt to return structured output.
