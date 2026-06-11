# Concept: Test Data Generator

Agent 64 solves the test data problem that plagues every QA team: test data is either too uniform (everyone uses the same five hardcoded records) or too much effort to create properly (someone has to manually craft edge cases for every field in every schema). The result is that boundary conditions go untested — and those are precisely where bugs hide.

The LLM is an excellent tool for test data generation because it understands context. When you describe a "user profile with a phone number field," an LLM doesn't just generate random strings — it generates phone numbers in realistic formats for multiple countries, and in boundary mode it adds numbers that are too long, too short, contain letters, or are completely empty. It does this because it has internalized the concept of "phone number" from training data, not because it was given an explicit list of edge cases.

The "mixed mode" is the most powerful feature. It generates a dataset that includes approximately 70% realistic records (what production data looks like) and 30% boundary records (what breaks systems). This ratio is configurable, but the default reflects the practical observation that most bugs appear at the boundaries — you need both types to have a useful test dataset.

This agent connects to the broader project by enabling other agents to generate their own test inputs. Agent 62 (Playwright) needs realistic form data. Agent 69 (Database Query) needs realistic records to query against. Agent 79 (AI Product Tester) needs adversarial inputs. Rather than each agent hard-coding its test data, they can call Agent 64 to generate contextually appropriate data on demand, creating a more dynamic and thorough testing pipeline.
