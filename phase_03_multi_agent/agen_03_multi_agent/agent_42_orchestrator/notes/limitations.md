# Limitations — Agent 42: Orchestrator

This agent does NOT:

- Branch based on intermediate results — the pipeline is linear and fixed; there is no conditional logic that routes to a different agent based on what a previous stage returned. For conditional routing, see later agents.
- Recover from stage failures — if any pipeline agent raises an exception or returns an unusable output, the orchestrator has no fallback path, no retry mechanism, and no way to skip to the next stage. The entire pipeline fails.
- Retry individual stages — a stage that returns a malformed response is not retried with a different prompt or a simplified input. The failure is immediate and final.
- Construct the pipeline dynamically — the sequence of agents is hardcoded in the orchestrator. It cannot decide at runtime to add, remove, or reorder stages based on the nature of the input.
- Detect cycles — if the pipeline were ever configured to call itself (Agent A → Agent B → Agent A), the orchestrator has no cycle detection and would loop indefinitely or until a call limit is hit.
- Run stages in parallel — even when two stages could theoretically run simultaneously (if they share the same input but do not depend on each other), this orchestrator always runs them sequentially.
