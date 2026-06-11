# Concept — Agent 26: Retrieval

## Semantic Retrieval vs Keyword Search

Keyword search finds documents that contain the exact words in a query. It fails when a stored document uses different vocabulary to express the same idea — "latency spike" will not match "slow response time" even though they describe the same phenomenon. Semantic retrieval solves this by converting both the query and the stored documents into dense vector embeddings, where meaning is encoded as position in a high-dimensional space. Documents that mean similar things are geometrically close, regardless of surface-level word overlap.

## Cosine Similarity in Embedding Space

When a query is embedded, it becomes a vector of floating-point numbers representing its semantic position. The similarity between that query vector and each stored document vector is measured using cosine similarity — the cosine of the angle between the two vectors. A cosine similarity of 1.0 means the vectors point in the exact same direction (identical meaning); 0.0 means orthogonal (completely unrelated). ChromaDB typically exposes the complement as a distance score (lower distance = higher similarity), so results are sorted ascending by distance, not descending by similarity. Understanding this scoring mechanism is essential for interpreting and filtering retrieval results correctly.

## Why Pure Retrieval Matters as a Standalone Step

It is tempting to skip straight to RAG — retrieve then generate. But doing so hides the quality of retrieval behind the fluency of generation. An LLM can produce a confident-sounding answer even when the retrieved documents are irrelevant. By building Agent 26 as a pure retrieval engine with no generation, developers can inspect exactly what is coming back from the vector store, measure retrieval precision and recall independently, and tune the embedding model, chunking strategy, and k before ever involving an LLM. Retrieval quality is the foundation of RAG quality.

## Connection to Agent 22 and Future RAG Agents

Agent 22 (long-term memory) built the mechanism for storing documents as embeddings in ChromaDB. Agent 26 is the corresponding read path — the query engine that searches what Agent 22 stored. Together they form the backbone of any RAG system: write (embed + store) and read (embed + query). Future agents in the series will combine Agent 26-style retrieval with LLM generation to produce grounded answers, but those agents depend entirely on the retrieval layer working correctly. Getting retrieval right here means every downstream agent benefits.
