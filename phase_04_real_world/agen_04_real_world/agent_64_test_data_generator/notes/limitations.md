# Limitations: Test Data Generator

This agent does NOT:

- Seed data directly into any database — returns records as Python objects only
- Generate real PII (Social Security Numbers, actual credit card numbers, real passport numbers) — uses realistic-looking fictional data only
- Guarantee uniqueness across multiple calls — the same email address may appear in two separate invocations
- Generate more than approximately 50 records per single LLM call due to token limits
- Validate generated data against external constraints (e.g., "does this postal code match this city?")
- Generate binary data (file attachments, images, PDFs)
- Produce statistically distributed data matching a real production distribution
- Handle circular or recursive schema definitions
- Generate data in XML or CSV format — only JSON array output
- Guarantee the LLM will cover every possible boundary type — boundary coverage is best-effort
