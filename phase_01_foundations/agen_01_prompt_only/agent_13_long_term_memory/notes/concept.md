## Core Concept – Agent 13

Agent 12 introduced short-term memory: a Python list that accumulates conversation turns and disappears when the process ends. Agent 13 changes the storage layer entirely. Instead of a list, it uses ChromaDB — a vector database that persists to disk. This means information written in one session is available in the next, and in every session after that.

The critical shift is how retrieval works. Agent 12 could replay the full history list because everything was in memory and ordered. Agent 13 has no guaranteed order and no concept of "recent" — it retrieves by semantic closeness. When you query "what did the user say about login errors?", ChromaDB finds entries whose vector representations are geometrically close to the query vector in high-dimensional space. This is not string matching. It is meaning matching.

The embedding step is what makes this possible. Every piece of text — whether stored or queried — is converted to a fixed-length numerical vector using an embedding model. The model has been trained so that sentences with similar meanings produce vectors that are close together. This is why the system can match a query about "authentication failures" with a stored entry about "login errors" even though those phrases share no words.

Agent 13 deliberately does not reason over the retrieved documents. That is a conscious architectural boundary. The agent retrieves raw content and returns it. What to do with that content — summarize it, act on it, compare it — is the responsibility of downstream agents. Keeping retrieval and reasoning separate makes each piece independently testable and replaceable.
