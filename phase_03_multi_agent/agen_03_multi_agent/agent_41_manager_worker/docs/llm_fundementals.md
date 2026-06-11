# LLM Fundamentals: Manager Worker

- **Task decomposition via prompting**: The manager uses a structured prompt to instruct the LLM to break a task into N independent subtasks. The quality of decomposition depends entirely on prompt clarity — ambiguous decomposition prompts produce overlapping or incomplete subtasks.

- **Context isolation per worker**: Each worker receives only its subtask, not the full original task or the other subtasks. This deliberate context isolation prevents workers from being confused by irrelevant information and keeps each LLM call focused and cheap.

- **Synthesis as a second LLM call**: Aggregating N results into one coherent answer is itself an LLM task. The manager makes a second LLM call with all worker results concatenated. This two-call structure (decompose, then synthesize) is the skeleton of most multi-agent pipelines.

- **Token budget management**: The manager must be aware that each worker call consumes tokens. With N workers and a synthesis call, total token cost is roughly N × (subtask_tokens + result_tokens) + synthesis_tokens. Decomposing into too many subtasks multiplies cost without proportional benefit.

- **Role separation in system prompts**: The manager's system prompt says "you are a task planner." The worker's system prompt says "you are an executor." Different roles, different prompts, different behaviors from the same underlying model.
