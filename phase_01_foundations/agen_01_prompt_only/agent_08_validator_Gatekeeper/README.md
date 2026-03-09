## Agent 08 - Validator / Gatekeeper

### Purpose

Agent 08 validates user input before it reaches the LLM system.
It acts as a control layer that prevents invalid or disallowed input from entering the AI pipeline.

### Position in the System

System flow:

User
|
Agent 08 - Validator / Gatekeeper
|
Agent 07 - Response Agent
|
LLM
|
Response

Agent 08 is the first validation layer of the architecture.

### Definition

Agent 08 examines incoming user input and determines whether the input is valid or invalid according to predefined structural rules.

The agent does not modify the input.
It only returns a decision.

### Validation Rules

Agent 08 performs three checks:
1. Empty Input Check
- Input must not be empty.
2. Maximum Length Check
- Input must not exceed the defined maximum length.
3. Blocked Phrase Check
- Input must not contain prohibited phrases.

If any rule fails, the input is rejected.

### Output Contract

Agent 08 returns one of the following tokens:

VALID
INVALID

These tokens are used by the system pipeline to decide whether execution continues.

### Scope

Agent 08 is responsible for:
- Validating user input
- Detecting empty input
- Enforcing maximum input length
- Detecting blocked phrases
- Returning a validation decision

### Out of Scope

Agent 08 is not responsible for:
- Generating responses
- Calling the LLM
- Editing or rewriting input
- Storing memory
- Logging conversations
- Detecting complex malicious intent
- Tool usage
- Multi-agent orchestration

These responsibilities belong to other agents in the system.

### Completion Criteria

Agent 08 is considered complete when:
- It accepts user input.
- It performs the three defined validations.
- It returns VALID or INVALID.
- Invalid input does not proceed to the response agent.