# Agent Fundamentals — Agent 26: Retrieval

## What This Agent IS
- A pure read-only vector search engine
- Embeds the input query using the same model used at storage time
- Executes k-nearest-neighbor search against a named ChromaDB collection
- Applies optional metadata pre-filters before the k-NN step
- Returns ranked results sorted by cosine distance (ascending), with document text, metadata, and distance score
- A prerequisite building block for any RAG pipeline

## What This Agent IS NOT
- Not a generator — no LLM is called, no answer text is produced
- Not a reranker — results are ordered only by k-NN cosine distance, no secondary scoring
- Not a summarizer — raw document chunks are returned as-is
- Not a writer — it does not ingest, update, or delete documents in the store
- Not a fallback engine — there is no keyword search fallback when vector similarity is low
- Not a multi-collection aggregator — queries target exactly one collection per call

## Input Schema
```
{
  "query":      str,           # natural-language question or search phrase
  "collection": str,           # name of the ChromaDB collection to search
  "k":          int,           # number of top results to return (default: 5)
  "where":      dict | null    # optional metadata pre-filter, e.g. {"type": "bug"}
}
```

## Output Schema
```
{
  "results": [
    {
      "id":       str,    # document ID as stored in ChromaDB
      "text":     str,    # raw document text
      "metadata": dict,   # metadata dict stored with the document
      "distance": float   # cosine distance (0.0 = identical, higher = less similar)
    },
    ...                   # up to k entries, sorted ascending by distance
  ],
  "query_embedding_dim": int,  # dimensionality of the embedding vector used
  "collection":          str   # name of the collection that was queried
}
```

## Behavioral Notes
- If fewer than k documents exist in the (filtered) collection, all available documents are returned.
- Distance scores are collection-relative — a distance of 0.35 in one collection may indicate high relevance while the same score indicates low relevance in another, depending on document diversity.
- The `where` filter uses ChromaDB's metadata query syntax and is applied before k-NN, not after.
