# Limitations — Agent 26: Retrieval

## What This Agent Does NOT Do

- **Does not generate answers.** Agent 26 returns document chunks, not synthesized answers. The caller must decide what to do with the results. Combining retrieval with generation is the job of a RAG agent built on top of this one.

- **Does not rerank results.** Results are ordered solely by the initial cosine distance from the k-NN search. There is no cross-encoder reranking, no diversity-based reranking, and no business-logic-based reranking. If the top-K results cluster around the same sub-topic, no mechanism spreads them.

- **Does not fall back to keyword search.** If vector similarity is low for all candidates (i.e., the query is out-of-distribution for the collection's contents), Agent 26 still returns the top-K results without signaling that confidence is low. A hybrid retrieval layer combining BM25 and vector search is outside this agent's scope.

- **Does not handle out-of-vocabulary queries specially.** If the query uses domain terms the embedding model has never seen, the resulting query vector may be poorly positioned in the embedding space. Agent 26 has no mechanism to detect or compensate for this.

- **Does not guarantee recall.** k-NN search with HNSW (as used by ChromaDB) is approximate. A relevant document may not appear in the top-K even if it exists in the collection, because the ANN index trades a small amount of recall for speed.

- **Does not validate embedding model consistency.** If a collection was built with a different embedding model than the one used at query time, distances are nonsensical. Agent 26 does not detect this mismatch — it is the operator's responsibility to track and enforce model consistency.

- **Does not aggregate across multiple collections.** Each invocation targets exactly one ChromaDB collection. Multi-collection federated search requires calling Agent 26 once per collection and merging results externally.

- **Does not persist or cache query results.** Each invocation performs a fresh k-NN search. Caching frequently repeated queries is an optimization that must be implemented by the caller.

- **Does not summarize or cluster results.** If the top-K documents are all very similar to each other, no deduplication or clustering is applied — all k are returned as-is.

- **Does not score business relevance.** Cosine distance is a mathematical similarity measure, not a measure of whether a document is useful for the caller's specific task. A document can be semantically close to the query and yet be irrelevant to the actual need.
