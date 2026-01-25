Agent Memory Reminder

Statement

The agent does forget, but we remind it every time.

Purpose

This document exists to explicitly restate critical context at each interaction, ensuring consistent behavior despite the agent’s lack of persistent memory.

Key Characteristics
•	✔️ Agent 03 builds on Agent 02
•	✔️ It enables related / multi-turn questions
•	✔️ The agent does not truly remember
•	✔️ Memory is short-term
•	✔️ Memory is lost when the program exits
•	✔️ Stored in a Python list

Usage
•	Include this reminder at the start of each session or prompt.
•	Restate essential rules, goals, or constraints as needed.
•	Treat memory as ephemeral; repetition is intentional.

Note

For true persistence, external storage or explicit memory mechanisms must be used.