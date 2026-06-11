# Limitations: REST API Intelligence Agent

This agent does NOT:

- Perform load or stress testing — it sends exactly one request per invocation
- Manage authentication tokens, OAuth flows, or session cookies automatically
- Generate an API contract from scratch — the caller must describe or provide one
- Handle binary response bodies (images, PDFs, protobuf) — only JSON is analyzed
- Retry on transient network failures — a single attempt is made
- Validate against formal OpenAPI/Swagger schema files — it uses natural language contract descriptions
- Test sequences of API calls — each invocation is stateless and single-request
- Detect rate limiting or throttling conditions automatically
- Compare responses across multiple runs to detect regressions over time
- Access internal service logs or trace IDs to correlate server-side errors
