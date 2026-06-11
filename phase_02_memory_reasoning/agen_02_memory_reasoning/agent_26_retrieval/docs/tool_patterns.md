# Tool Patterns — Agent 26: Retrieval

## Pattern 1: Embed-Then-Query
The core retrieval pipeline: embed the query string first, then pass the resulting vector to ChromaDB's query interface. Never pass raw text to the query function — the collection stores vectors and cannot perform text matching. Always treat embedding and querying as two distinct, sequential steps, even when an abstraction layer combines them.

```
query_vector = embedding_model.encode(query_text)
results = collection.query(query_embeddings=[query_vector], n_results=k)
```

## Pattern 2: Metadata Pre-Filter
Apply known categorical constraints before the k-NN step to reduce the candidate pool and improve both precision and speed. Use ChromaDB's `where` parameter with equality or `$in` operators. Keep filter conditions simple — complex nested logic can produce unexpected empty results if ChromaDB's metadata index does not cover all fields.

```
results = collection.query(
    query_embeddings=[query_vector],
    n_results=k,
    where={"type": {"$in": ["bug", "convention"]}}
)
```

## Pattern 3: Result Threshold Filtering
After retrieval, drop any result whose distance exceeds a configured maximum. This prevents low-confidence matches from polluting the result set. The threshold should be calibrated per collection — start with 0.5 as a conservative default and adjust based on empirical precision/recall trade-offs.

```
MAX_DISTANCE = 0.5
filtered = [r for r in results if r["distance"] <= MAX_DISTANCE]
```

## Pattern 4: Collection Routing
When multiple ChromaDB collections exist (e.g., one per domain, one per team), the caller specifies which collection to target as an input parameter. The retrieval agent does not decide which collection is relevant — that routing decision belongs to the orchestrating agent. Agent 26 accepts any valid collection name and treats it as a black box target.

```
# Caller decides routing:
agent_26.query(query="timeout errors", collection="payment_service_bugs", k=5)
agent_26.query(query="timeout errors", collection="auth_service_bugs", k=5)
```

## Anti-Pattern: Embedding at Query Time vs Storage Time
Never change the embedding model between storage and query. If a new model is adopted, the entire collection must be re-embedded. Maintain a model registry that records which embedding model version was used to build each collection, and validate this at query time before running k-NN.
