# Limitations — Agent 41: Manager-Worker

This agent does NOT:

- Run workers in parallel — all subtask calls are sequential; worker 2 does not start until worker 1 has returned its result. For parallel execution, see Agent 52.
- Handle worker failures or retries — if a worker call raises an exception or returns an unusable result, the agent has no fallback logic. The failure propagates upward.
- Dynamically select which workers to call — the manager calls the same worker function for every subtask. There is no routing logic that selects a specialist worker based on subtask type.
- Allow workers to communicate with each other — each worker receives only its own subtask. Workers cannot share intermediate findings, coordinate, or reference each other's outputs.
- Persist results between runs — all results exist only in memory during a single execution. There is no database write, file write, or cache. Rerunning the agent starts from scratch.
- Support more than 5 subtasks without quality degradation — the decomposition prompt and aggregation prompt are not designed for large numbers of subtasks. Beyond 5, the LLM tends to produce overlapping subtasks during decomposition and loses coherence during aggregation.
