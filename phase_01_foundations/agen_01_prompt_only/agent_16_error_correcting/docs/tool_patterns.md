Tool Patterns — Agent 16

Agent 16 uses no tools and makes no external calls. It follows the Template Lookup Pattern: map structured error codes to pre-written fix templates and return the assembled result.

This pattern is common in rule engines, linter auto-fix systems, and IDE quick-fix suggestions. The pattern has three components: an error taxonomy (a finite set of error codes), a template registry (a dict mapping codes to suggestion strings), and an assembly step (collect matching templates, sort by priority, return the list).

Pattern in use:
  Error codes + anomaly strings → Template registry lookup → Sorted suggestion list

The template registry should live in a separate configuration file (dict or YAML), not hardcoded inside the agent function. This allows the builder to add new fix templates without modifying the agent logic — the same separation-of-concerns principle used throughout the project.
