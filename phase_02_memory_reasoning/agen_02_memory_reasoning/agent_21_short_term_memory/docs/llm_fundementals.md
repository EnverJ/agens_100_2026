# LLM Fundamentals: Agent 21 — Short-Term Memory (Phase 2)

- **Context window as working memory**: LLMs have no inherent memory between calls. Everything the model "knows" about the conversation must be injected into the prompt. Agent 21 manages the data structure that feeds this injection — the memory snapshot becomes part of the next prompt's context.

- **Structured vs. unstructured context**: Feeding a raw string history into a prompt is less effective than feeding structured role/content objects. Modern LLMs respond better when the context is clearly delineated by role (system, user, assistant), because this mirrors the format they were trained on.

- **Sliding window and token budget**: Every token in the memory snapshot costs tokens in the model's context window. A bounded sliding window is a practical solution to the token budget problem — it keeps recent history without exceeding the model's input limit.

- **Tagging for retrieval priming**: Including semantic tags in context entries allows later prompts to draw attention to specific past events ("you previously encountered an error tagged 'auth_failure'"). This is prompt-level retrieval before vector search is involved.

- **Memory as prompt engineering**: How you structure and inject memory into a prompt is itself a prompt engineering decision. The format, ordering, and selection of context entries directly affect the quality of the model's next response.
