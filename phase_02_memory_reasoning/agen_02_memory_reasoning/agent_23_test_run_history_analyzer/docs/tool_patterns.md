# Tool Patterns: Agent 23 — Test Run History Analyzer

## Pattern: Structured-to-Text Serialization for Embedding

Convert the structured test run result into a natural-language sentence before embedding. This ensures the embedding captures the semantic meaning of the result, not the syntactic structure of the JSON.

```python
def serialize_run(run: dict) -> str:
    pass_rate = run["pass_count"] / (run["pass_count"] + run["fail_count"])
    failures_str = ", ".join(run["failures"]) if run["failures"] else "none"
    return (
        f"Test suite {run['suite_name']} ran on {run['run_date']}. "
        f"{run['pass_count']} passed, {run['fail_count']} failed "
        f"({pass_rate:.0%} pass rate). "
        f"Duration: {run['duration_seconds']:.1f}s. "
        f"Failures: {failures_str}."
    )
```

## Pattern: Metadata-Enriched Storage

Store the structured fields as ChromaDB metadata alongside the serialized text. This enables both semantic retrieval (via the text embedding) and exact metadata filtering (via the metadata dict) from a single stored entry.

```python
metadata = {
    "suite_name": run["suite_name"],
    "run_date": run["run_date"],
    "pass_rate": round(pass_rate, 4),
    "fail_count": run["fail_count"],
    "duration_seconds": run["duration_seconds"]
}

collection.upsert(
    ids=[run_id],
    documents=[serialized_text],
    embeddings=[embedding],
    metadatas=[metadata]
)
```

## Pattern: Hybrid Filter + Semantic Query

When the query specifies a suite name, apply a metadata pre-filter before running k-NN search. This scopes retrieval to the relevant suite and improves result precision without sacrificing the natural-language query interface.

```python
where_clause = {}
if suite_name:
    where_clause = {"suite_name": {"$eq": suite_name}}

results = collection.query(
    query_embeddings=[query_vector],
    n_results=k,
    where=where_clause if where_clause else None,
    include=["documents", "metadatas", "distances"]
)
```
