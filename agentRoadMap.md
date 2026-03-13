Agents #1–#20 Roadmap

⸻

Layer 1 — Foundations (Agents 01–10)

Agent 01 — Prompt-only Agent
	•	Purpose: Receive user input and format it for the system.
	•	Scope: Simple input capture and normalization.
	•	IS: Text normalization, basic tokenization.
	•	IS NOT: Memory handling, routing, tool calls.
	•	Input: Raw user text
	•	Output: Normalized text
	•	Reflection Questions:
	•	Did I ensure consistent text formatting?
	•	Was the input correctly tokenized?

⸻

Agent 02 — Simple Response Agent
	•	Purpose: Map normalized input → simple template response.
	•	Scope: Deterministic output based on input patterns.
	•	IS: Pattern matching, basic reply.
	•	IS NOT: Complex reasoning, memory retrieval, tool execution.
	•	Input: Normalized text
	•	Output: Template response
	•	Reflection Questions:
	•	Does every input produce a valid response?
	•	Are outputs predictable and consistent?

⸻

Agent 03 — Input Validator
	•	Purpose: Validate user input for correctness, completeness, and type.
	•	Scope: Detect missing or invalid information.
	•	IS: Validation checks (empty, format, type).
	•	IS NOT: Suggesting fixes, memory usage, routing.
	•	Input: User text
	•	Output: Validation status (valid/invalid)
	•	Reflection Questions:
	•	Are all invalid inputs caught?
	•	Are valid inputs accepted without false negatives?

⸻

Agent 04 — Routing Agent
	•	Purpose: Decide the next agent to handle the input.
	•	Scope: Basic conditional routing.
	•	IS: Mapping input categories → agent paths.
	•	IS NOT: Tool execution, memory retrieval, reasoning.
	•	Input: Validated input
	•	Output: Next agent ID
	•	Reflection Questions:
	•	Does routing match expected logic?
	•	Are all categories covered?

⸻

Agent 05 — Logger Agent
	•	Purpose: Log system events for later reflection.
	•	Scope: Record inputs, outputs, and agent paths.
	•	IS: Basic logging to memory or file.
	•	IS NOT: Analysis, routing, or decision-making.
	•	Input: Input text, output, agent ID
	•	Output: Log entry confirmation
	•	Reflection Questions:
	•	Is logging complete and accurate?
	•	Can logs be easily retrieved for analysis?

⸻

Agent 06 — Memory Placeholder Agent
	•	Purpose: Set up memory scaffolding for future agents.
	•	Scope: Initialize memory structure (empty, deterministic).
	•	IS: Create memory storage template.
	•	IS NOT: Retrieve or store real data yet.
	•	Input: None / system init
	•	Output: Memory object
	•	Reflection Questions:
	•	Is memory structure flexible for later agents?
	•	Is it deterministic and predictable?

⸻

Agent 07 — Response Builder Agent
	•	Purpose: Format outputs for the user.
	•	Scope: Combine system outputs into structured response.
	•	IS: Output formatting, deterministic text assembly.
	•	IS NOT: Decision-making, tool execution, memory retrieval.
	•	Input: Agent outputs
	•	Output: Formatted user response
	•	Reflection Questions:
	•	Are all outputs structured clearly?
	•	Does formatting remain consistent across agents?

⸻

Agent 08 — Validator Agent
	•	Purpose: Confirm correctness of outputs before user delivery.
	•	Scope: Check output completeness and adherence to rules.
	•	IS: Deterministic evaluation.
	•	IS NOT: Decision-making, memory retrieval, tool execution.
	•	Input: Formatted output
	•	Output: Validation status (pass/fail)
	•	Reflection Questions:
	•	Are outputs accurate and complete?
	•	Does validation cover edge cases?

⸻

Agent 09 — Memory Decision Agent
	•	Purpose: Decide if memory storage or retrieval is needed.
	•	Scope: Minimal branching logic based on input type.
	•	IS: Conditional check for memory use.
	•	IS NOT: Execute memory retrieval or store data.
	•	Input: Validated input / system state
	•	Output: Boolean memory flag
	•	Reflection Questions:
	•	Is decision logic correct?
	•	Are memory flags correctly set for future agents?

⸻

Agent 10 — Tool Decision Agent
	•	Purpose: Determine if a tool (calculator, API, etc.) is required.
	•	Scope: Detect keywords or patterns indicating tool usage.
	•	IS: Tool routing decision
	•	IS NOT: Execute the tool, retrieve results, or reason beyond detection.
	•	Input: Validated input, memory flag
	•	Output: Tool-required flag / agent routing
	•	Reflection Questions:
	•	Does detection match expected triggers?
	•	Are false positives minimized?

⸻

Layer 2 — Coordination & Routing (Agents 11–20)

Agent 11 — Context Builder Agent
	•	Purpose: Aggregate input, memory, and previous outputs into a structured context for downstream agents.
	•	Scope: Context assembly, deterministic.
	•	IS: Builds unified context object.
	•	IS NOT: Reasoning or output formatting.
	•	Input: User input, logs, memory flag
	•	Output: Context object
	•	Reflection Questions:
	•	Is context complete and consistent?
	•	Does it provide all needed data for next agents?

⸻

Agent 12 — Short-term Memory Agent
	•	Purpose: Store temporary memory for current session.
	•	Scope: Memory creation and retrieval in session scope.
	•	IS: Short-term state handling.
	•	IS NOT: Long-term storage, retrieval across sessions.
	•	Input: Context object
	•	Output: Updated context + short-term memory
	•	Reflection Questions:
	•	Is session memory persistent and accurate?
	•	Are retrievals correct?

⸻

Agent 13 — Long-term Memory Agent
	•	Purpose: Interface with long-term memory storage (vector DB).
	•	Scope: Store/retrieve historical information.
	•	IS: Long-term memory retrieval, storage.
	•	IS NOT: Tool execution, reasoning.
	•	Input: Context object, memory flags
	•	Output: Context updated with long-term memory
	•	Reflection Questions:
	•	Are retrievals accurate?
	•	Is data properly stored and accessible later?

⸻

Agent 14 — Reflection Agent
	•	Purpose: Analyze agent outputs and system state for self-improvement.
	•	Scope: Simple evaluation logic.
	•	IS: Detect errors, anomalies, inconsistencies.
	•	IS NOT: Corrective action or reasoning beyond reporting.
	•	Input: Context, outputs
	•	Output: Reflection report
	•	Reflection Questions:
	•	Are errors correctly identified?
	•	Are anomalies logged for learning?

⸻

Agent 15 — Self-critic Agent
	•	Purpose: Critique its own outputs for accuracy and clarity.
	•	Scope: Evaluation against validation rules.
	•	IS: Simple scoring system.
	•	IS NOT: Modifying outputs or routing.
	•	Input: Outputs, reflection report
	•	Output: Critique / score
	•	Reflection Questions:
	•	Are outputs consistently evaluated?
	•	Are critiques actionable?

⸻

Agent 16 — Error-correcting Agent
	•	Purpose: Flag and suggest fixes for detected errors.
	•	Scope: Suggestive corrective logic.
	•	IS: Flags issues for the builder or downstream agents.
	•	IS NOT: Automatic correction or reasoning beyond suggestion.
	•	Input: Critiques, reflection reports
	•	Output: Error flags / suggestions
	•	Reflection Questions:
	•	Are corrections properly flagged?
	•	Are false positives minimized?

⸻

Agent 17 — Input Router Agent
	•	Purpose: Route input to specific tool or agent based on updated context.
	•	Scope: Routing logic based on context & memory flags.
	•	IS: Conditional routing
	•	IS NOT: Execute tools or modify outputs
	•	Input: Context object, flags
	•	Output: Next agent ID
	•	Reflection Questions:
	•	Are routing decisions correct and deterministic?
	•	Are edge cases handled?

⸻

Agent 18 — Tool Executor Agent
	•	Purpose: Execute detected tools (API, calculator, etc.)
	•	Scope: Perform tool calls based on flags.
	•	IS: Executes and returns results
	•	IS NOT: Decision-making beyond execution
	•	Input: Context, tool-required flag
	•	Output: Tool results
	•	Reflection Questions:
	•	Are tool calls executed correctly?
	•	Are results accurate and returned timely?

⸻

Agent 19 — Output Validator Agent
	•	Purpose: Validate results from tools and memory retrieval.
	•	Scope: Pass/fail validation
	•	IS: Checks correctness, completeness
	•	IS NOT: Corrective action or formatting
	•	Input: Tool results, memory outputs
	•	Output: Validation status
	•	Reflection Questions:
	•	Are validations consistent and accurate?
	•	Do all errors get flagged?

⸻

Agent 20 — Context Updater Agent
	•	Purpose: Update system context with latest outputs and validations.
	•	Scope: Maintain updated context for downstream agents
	•	IS: Context object update
	•	IS NOT: Decision-making or output formatting
	•	Input: Validation results, context object, outputs
	•	Output: Updated context object
	•	Reflection Questions:
	•	Is context always consistent?
	•	Are updates reflected correctly for downstream agents?

⸻

✅ Next Step Recommendation
	•	Begin building Layer 1 agents (#01–#10) first.
	•	Complete reflection after each agent.
	•	Only after Layer 1 is fully complete, move to Layer 2 (#11–#20).

⸻

```sh

```