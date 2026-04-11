## Core Concept – Agent 12

Agent 12 is the Short-term Memory Agent.

It receives a context object from Agent 11 and stores the current interaction in a session-scoped memory list.
The memory only lives as long as the session is running — it is not persisted to disk or a database.

Each stored entry captures the user input, timestamp, memory flag, and tool flag from the context.
After storing, it returns an updated context object that includes the full short-term memory list.

This allows downstream agents to see the history of the current session and make decisions based on it.

Agent 12 does not reason, filter, or summarize.
It simply appends to the session list and returns.

The purpose of Agent 12 is to give the system a short-term view of what has happened so far in the conversation,
enabling continuity across multiple turns within a single session.
