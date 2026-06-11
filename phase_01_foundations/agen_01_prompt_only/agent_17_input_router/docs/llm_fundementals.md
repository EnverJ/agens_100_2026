LLM Fundamentals — Agent 17

• Agent 17 makes no LLM call. Routing is deterministic and based entirely on flag values. This is by design — routing logic that involves an LLM introduces latency and nondeterminism into the control plane, which should be the most reliable part of the system.

• The contrast with LLM-based routing is instructive. An LLM router would take the user input as text and decide which agent to call based on the content — "this looks like a question that needs memory, route to Agent 13." That approach handles ambiguous inputs better but is harder to test and can route incorrectly. Deterministic routing handles unambiguous structured flags perfectly and never makes mistakes on the cases it covers.

• Understanding when to use deterministic vs. LLM-based routing is a key architectural judgment. Use deterministic routing when the routing signal is a structured flag that upstream agents set reliably. Use LLM routing when the signal must be inferred from unstructured text and ambiguity is acceptable.

• The flags that drive Agent 17's decisions (memory_flag, tool_flag) were set by upstream agents — specifically Agent 11 (context builder) and Agent 06 (input parsing). This dependency means the quality of routing is upstream of the router itself. If Agent 06 sets flags incorrectly, Agent 17 routes to the wrong agent — and does so correctly according to its own logic. Debugging routing errors often means debugging the flag-setting agents, not the router.

• In later agents, routing will be expressed as a graph with weighted edges rather than a flat if/elif tree. The flat tree introduced here is the simplest case of that more general concept.
