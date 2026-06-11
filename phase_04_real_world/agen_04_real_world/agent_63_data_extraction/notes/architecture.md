# Architecture: Data Extraction Agent

```
┌─────────────────────────────────────────────────────────────────┐
│                         CALLER / USER                           │
│  { raw_text: "...", schema: { field: type, ... } }              │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Input Validator                               │
│                                                                 │
│   Check raw_text not empty                                      │
│   Check schema has at least one field                           │
│   Estimate token count — warn if > 6000 tokens                 │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Prompt Builder                                │
│                                                                 │
│   System: "You are a data extraction engine. Extract fields     │
│            from the text below. Return ONLY valid JSON.         │
│            Use null for missing fields. No hallucination."      │
│                                                                 │
│   User:   "Target schema: {schema}                              │
│            Raw text: {raw_text}"                               │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                         LLM (Claude)                            │
│                                                                 │
│   Returns JSON matching schema, nulls for missing fields        │
│                                                                 │
│   Example: {                                                    │
│     "timestamp": "2026-06-03T09:00:00Z",                       │
│     "error_code": "DB_CONN_TIMEOUT",                           │
│     "severity": "CRITICAL",                                     │
│     "service_name": "order-service",                           │
│     "user_id": null                                             │
│   }                                                             │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                  Output Parser & Validator                       │
│                                                                 │
│   json.loads(llm_output)                                       │
│   Type-check each field against schema                          │
│   Compute completeness: filled_fields / total_fields           │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
              { extracted: {...}, completeness: 0.8,
                missing_fields: ["user_id"] }
```
