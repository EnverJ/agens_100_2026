# LLM Fundamentals: Test Data Generator

- **Domain knowledge as test oracle**: The LLM's training data includes millions of examples of realistic data formats — phone numbers, email patterns, name conventions by culture, date formats. This embedded knowledge is what makes the generated "realistic" records look like real data rather than random strings.

- **Boundary value analysis via instruction**: By explicitly naming boundary types in the system prompt (empty, max-length, negative, null, special characters), the agent teaches the LLM to apply systematic boundary value analysis — a classical testing technique — as part of generation. The LLM does not invent these boundaries; the prompt prescribes them.

- **Controlled creativity**: Generating test data requires a balance between creativity (variety, realism) and constraint (must match schema types). The prompt instructs the LLM to be creative within schema boundaries, demonstrating temperature-like behavior through prompt instruction rather than parameter tuning.

- **Batch generation**: The LLM can generate multiple records in one call by requesting a JSON array, which is far more token-efficient than calling once per record. This is the "batch output" pattern for LLM code generation and data tasks.

- **Intentional invalidity**: In boundary mode, the agent asks the LLM to generate records that intentionally violate field constraints (wrong types, format violations). This requires the LLM to reason about what "invalid" means for each field type — demonstrating understanding of constraints, not just pattern generation.
