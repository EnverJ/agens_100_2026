Tool Patterns — Agent 17

Agent 17 uses no tools. It follows the Conditional Dispatch Pattern: read structured state, apply branching logic, return a target identifier.

This pattern is the foundation of workflow orchestration systems (Apache Airflow DAGs, AWS Step Functions, LangGraph conditional edges). The router is a pure function: same context flags always produce the same next agent ID.

Pattern in use:
  Context dict → if/elif tree → agent ID string

Key properties of this pattern:
  • Idempotent: calling the router twice with the same context always produces the same result
  • Testable: every branch can be tested with a single mock context object
  • Explicit: the full routing table is visible in one place — no hidden dispatch logic

The routing table (the if/elif branches and their mappings) should ideally be extracted to a configuration dict, making it easy to add new routes without modifying the core routing logic.
