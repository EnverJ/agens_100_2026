LLM Fundamentals — Agent 13

• Embeddings are dense numerical vectors produced by a model trained to place semantically similar texts close together in vector space. The embedding model does not generate text — it encodes meaning into numbers.

• The quality of retrieval is entirely determined by the embedding model. A weak embedding model will cluster unrelated concepts together and separate related ones. Model choice matters more than the database choice for this agent.

• ChromaDB handles approximate nearest-neighbor search internally. "Nearest" means lowest cosine distance between query vector and stored vectors — not exact string match, not keyword overlap.

• This agent does not use a chat-completion LLM call. The LLM role here is limited to the embedding step. Understanding that LLMs serve multiple roles (text generation, embedding, classification) is a core concept introduced at this stage.

• Token limits do not apply in the traditional sense here — but there is a maximum input length for the embedding model. Texts longer than ~512 tokens typically need chunking before embedding, otherwise the model truncates them silently.
