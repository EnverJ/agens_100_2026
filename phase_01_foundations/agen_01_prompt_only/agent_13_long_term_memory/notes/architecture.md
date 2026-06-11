Agent 13 — Long-Term Memory Architecture

┌─────────────────────────────────────────────────────────────┐
│                      Incoming Request                        │
│         { context, mode: "store"|"query", text }            │
└───────────────────────────┬─────────────────────────────────┘
                            │
                  ┌─────────▼──────────┐
                  │   Mode Dispatcher  │
                  │  store  │  query   │
                  └────┬────┴────┬─────┘
                       │         │
          ┌────────────▼──┐   ┌──▼────────────────┐
          │ Embed Text    │   │  Embed Query       │
          │ (text→vector) │   │  (query→vector)    │
          └────────┬──────┘   └──────┬─────────────┘
                   │                 │
          ┌────────▼──────┐   ┌──────▼─────────────┐
          │  ChromaDB     │   │  ChromaDB           │
          │  .add()       │   │  .query()           │
          │  + metadata   │   │  top-k similarity   │
          └────────┬──────┘   └──────┬─────────────┘
                   │                 │
          ┌────────▼──────┐   ┌──────▼─────────────┐
          │ Confirmation  │   │  Matched Documents  │
          │ { stored: ok }│   │  [{ text, score }] │
          └───────────────┘   └────────────────────┘

Persistence Layer:
  ChromaDB collection stored on disk (./chroma_store/)
  Survives process restarts — data is NOT lost between sessions
