Tool Patterns — Agent 20

Agent 20 uses no tools and makes no external calls. It follows the Artifact Ingestion Pattern: read an external file produced by another system, parse it, and convert it into a structured object that the agent pipeline can consume.

This pattern is the bridge between the external testing ecosystem (Allure, pytest, JUnit) and the internal agent pipeline. Without this bridge, the pipeline is isolated from the results of actual test runs. With it, every test execution automatically feeds structured data into the agent system.

Pattern in use:
  File path → JSON parser → iteration + accumulation → summary dict

Key properties:
  • Read-only: never modifies the report file
  • Idempotent: reading the same file twice produces the same summary
  • Format-dependent: changes to the Allure JSON schema (e.g., version upgrades) may require updates to the field paths used during parsing

SDET context: This pattern generalizes to any test report format — JUnit XML, pytest JSON, Cucumber JSON, k6 output. The agent structure stays the same; only the parsing logic changes per format. Build the pattern once with Allure, then extend it to other formats as needed.
