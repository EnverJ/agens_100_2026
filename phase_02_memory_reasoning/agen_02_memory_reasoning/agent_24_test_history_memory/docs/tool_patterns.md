# Tool Patterns: Agent 24 — Test History Memory

## Pattern: Metadata-Keyed Retrieval

Use ChromaDB's `where` clause to look up all entries for a specific test by exact test_name match. This is keyed retrieval: the test_name is the lookup key, and the metadata index provides constant-time scoping before any vector math runs.

```python
results = collection.get(
    where={"test_name": {"$eq": test_name}},
    include=["documents", "metadatas"]
)
```

Use `collection.get()` (not `collection.query()`) when you want all matching entries by metadata, without a similarity ranking. Use `collection.query()` when you also want a semantic similarity ranking over the filtered set.

## Pattern: Recency-Ordered Results

ChromaDB does not sort by timestamp. After fetching entries, sort client-side by the timestamp metadata field and take the last_n most recent entries.

```python
import operator

entries = list(zip(results["metadatas"], results["documents"]))
entries.sort(key=lambda x: x[0]["timestamp"], reverse=True)  # newest first
recent = entries[:last_n]
```

## Pattern: Hybrid Filter + Semantic (Optional Mode)

When the caller wants to find tests with similar error messages (cross-test discovery), combine metadata filtering with semantic search.

```python
results = collection.query(
    query_embeddings=[embed(error_message_query)],
    n_results=k,
    where={"outcome": {"$eq": "fail"}},  # only failures
    include=["documents", "metadatas", "distances"]
)
```

## Pattern: Per-Entity Memory Pattern

This is the general pattern for storing one-entry-per-event for a named entity, with keyed retrieval by entity identifier:

1. Add entity ID as a metadata field on every stored entry.
2. Use `where={"entity_id": {"$eq": id}}` to scope all retrieval to that entity.
3. Sort and slice client-side for recency-ordered history.
4. Compute aggregate stats (failure_rate, last_seen_error) from the retrieved window.

This pattern applies to any domain: test_name → test history, user_id → user event history, bug_id → bug state history.
