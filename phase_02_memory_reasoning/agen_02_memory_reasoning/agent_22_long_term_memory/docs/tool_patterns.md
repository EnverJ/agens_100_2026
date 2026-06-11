# Tool Patterns: Agent 22 — Long-Term Memory

## Pattern: ChromaDB Upsert

Use `collection.upsert()` rather than `collection.add()` to avoid duplicate entries when the same content is re-stored under the same ID. Upsert updates an existing entry if the ID already exists, or creates a new one if it does not. This is the correct default for long-term memory where the same fact may be re-encountered.

```python
collection.upsert(
    ids=[entry_id],
    documents=[text],
    embeddings=[embedding_vector],
    metadatas=[metadata_dict]
)
```

## Pattern: Embedding Generation

Generate embeddings using the same model for both STORE and QUERY calls. If the models differ between store time and query time, distances become meaningless. Keep the embedding model pinned to a fixed version in config.

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(text: str) -> list[float]:
    return model.encode(text).tolist()
```

## Pattern: k-NN Query with Distance Return

Always request distances alongside results so the caller can apply a distance threshold. Results beyond a threshold distance (e.g., > 0.8) are too dissimilar and should be filtered out before returning to the caller.

```python
results = collection.query(
    query_embeddings=[query_vector],
    n_results=k,
    include=["documents", "metadatas", "distances"]
)
```

## Pattern: Metadata Filtering Before Similarity Search

ChromaDB supports a `where` clause that pre-filters the candidate set before running similarity search. Use this to scope queries to a specific time range, session, or tag without scanning the entire collection.

```python
results = collection.query(
    query_embeddings=[query_vector],
    n_results=k,
    where={"source": "test_agent"},          # exact match filter
    include=["documents", "metadatas", "distances"]
)
```

Common `where` operators: `$eq`, `$ne`, `$in`, `$gt`, `$lt`. Combine with `$and` / `$or` for compound filters.
