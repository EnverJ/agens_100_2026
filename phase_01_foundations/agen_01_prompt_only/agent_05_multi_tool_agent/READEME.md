# Agent 05 — Multi-Tool Dispatcher

## Purpose

Agent 05 exists to practice **tool selection**, not intelligence.

The agent receives a user message and decides **which one tool** to call based on simple rules.

This agent does **not** try to be smart.  
It tries to be **correct and predictable**.

---

## What Agent 05 Introduces

**One new concept only:**

Selecting between multiple tools using deterministic logic.

---

## What Agent 05 Does

1. Accepts user input from the terminal
2. Analyzes the input using simple keyword checks
3. Chooses **one** tool
4. Executes that tool
5. Returns the tool result to the user

---

## Tools Used

Agent 05 uses **exactly three local tools**:

- **Time Tool**  
  Returns the current time

- **Date Tool**  
  Returns the current date

- **Math Tool**  
  Adds two numbers provided by the user

Each tool:
- Is a plain Python function
- Has no memory
- Has no side effects
- Returns a simple value

---

## Decision Flow

User Input  
↓  
Keyword Check (`if / elif`)  
↓  
Select ONE Tool  
↓  
Execute Tool  
↓  
Return Result  

There is **no learning**, **no memory**, and **no fallback to GPT** for tool selection.

---

## What Agent 05 Is NOT

Agent 05 does NOT include:

- Memory
- GPT-based reasoning
- Tool chaining
- External APIs
- JSON schemas
- LangChain
- Planning or reflection
- Multi-agent communication

If any of these appear, the scope has been violated.

---

## Why This Agent Matters

This pattern is the foundation of:

- Command routers
- Keyword-driven automation
- Test orchestration engines
- CI/CD job selection
- AI-assisted SDET tools

Before systems can be intelligent, they must be **reliable**.

---

## Completion Criteria

Agent 05 is considered complete when:

- Three tools exist
- Exactly one tool is called per input
- The agent runs in a terminal
- The logic is easy to read
- The code was typed, not pasted




---

## Key Lesson

Intelligence comes later.  
Control comes first.


---

## Next Step

Once Agent 05 is complete and committed, the project proceeds to **Agent 06**.