# Architecture: Test Data Generator

```
┌─────────────────────────────────────────────────────────────────┐
│                         CALLER / USER                           │
│  { schema, count=10, mode="mixed" }                             │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Request Planner                               │
│                                                                 │
│   mode="realistic"  → request N realistic records               │
│   mode="boundary"   → request 1 record per boundary type        │
│   mode="mixed"      → request 0.7N realistic + 0.3N boundary   │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Prompt Builder                                │
│                                                                 │
│   System: "You are a test data generator. Generate records      │
│            matching the schema. For boundary mode, include:     │
│            empty strings, max-length strings (255 chars),       │
│            negative numbers, zero, null optionals,              │
│            special chars (!@#$%), Unicode (日本語, العربية),    │
│            past date extremes (1900-01-01) and future ones."    │
│                                                                 │
│   User:   "Schema: {schema}   Count: {count}   Mode: {mode}"   │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                         LLM (Claude)                            │
│                                                                 │
│   Returns: JSON array of records                                │
│   [ { "name": "Priya Sharma", "email": "p.sharma@ex.com", ... }│
│     { "name": "", "email": "not-an-email", ... }              │
│     ... ]                                                       │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                  Schema Validator                                │
│                                                                 │
│   Parse JSON array                                             │
│   Check each record has all required keys                       │
│   Report invalid records (not removed — they may be intentional │
│   boundary cases like missing required fields)                  │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
            { records: [...], count: 10,
              mode: "mixed", invalid_count: 0,
              boundary_types_covered: [...] }
```
