# LLM Fundamentals: Data Extraction Agent

- **Information extraction as NLU task**: The LLM performs Named Entity Recognition (NER) and slot filling — classical NLP tasks — but using a general-purpose model rather than a domain-specific trained model. The advantage is zero additional training; the LLM generalizes from its pre-training to any domain.

- **Anti-hallucination prompting**: The system prompt explicitly instructs the LLM to return `null` for fields not found in the source text rather than generating a plausible value. This is a critical safety constraint — extraction agents that hallucinate missing values corrupt downstream data pipelines.

- **Schema injection**: The target schema is injected into the prompt as a typed field list. The LLM uses this schema as a "slot template" to fill from the source text. This is a form of structured prompting where the output format is defined before the LLM generates any tokens.

- **JSON-mode output**: The LLM is instructed to return only valid JSON. In practice, Claude reliably returns JSON when constrained this way, but the agent always wraps the parse in a try/except and returns a partial result rather than crashing.

- **Multilingual robustness**: LLMs trained on multilingual data can extract fields from mixed-language text (e.g., English error codes in a Hindi incident report) without explicit configuration. This is an emergent capability that regex-based extraction cannot match.
