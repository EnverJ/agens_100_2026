Agent 02 – Prompt-Constrained Text Agent

Overview

Agent 02 builds directly on Agent 01 but introduces prompt constraints to guide and restrict the agent’s behavior. The core model is the same (a stateless text-to-text transformer), but the prompt now acts as a control layer.

This agent demonstrates how prompt engineering functions as a lightweight form of alignment and control, without adding memory, tools, or external state.

⸻

Key Idea

By changing the prompt, we restrict the agent’s behavior to follow specific requirements instead of responding freely.
	•	The agent no longer chooses responses arbitrarily
	•	The output space becomes narrower
	•	Token prediction is biased toward desired behavior

This leads to more consistent and relevant answers, even though the agent still has no memory.

⸻

How Agent 02 Works (Step-by-Step)
	1.	User Input
	•	User provides a text prompt
	2.	System / Instruction Prompt (New)
	•	A predefined instruction is added, such as:
	•	“You are a helpful assistant that answers concisely.”
	•	“Only answer using facts.”
	•	“Do not speculate.”
	3.	Tokenization
	•	Both the instruction prompt and user input are converted into tokens
	4.	Next-Token Prediction
	•	The model predicts the next token based on:
	•	The instruction tokens
	•	The user input tokens
	•	Learned probabilities from training
	5.	Output Generation
	•	Because the prompt restricts behavior, the model’s token choices are limited to a narrower scope

⸻

What Changed from Agent 01

Aspect	Agent 01	Agent 02
Memory	❌ None	❌ None
Prompt	Minimal / neutral	Explicitly constrained
Behavior	Free-form	Restricted
Output Quality	Variable	More controlled
Hallucination Risk	Higher	Reduced (but not eliminated)


⸻

Important Insight

Even with prompt constraints:
	•	The agent is still predicting the next token
	•	It does not understand truth
	•	It does not verify facts

The improvement comes from probability shaping, not reasoning guarantees.

⸻

Limitations
	•	No memory across turns
	•	No awareness of previous answers
	•	Can still be confidently wrong
	•	Prompt constraints can conflict or be ignored under ambiguity

⸻

Why Agent 02 Matters

Agent 02 teaches a critical lesson:

Prompt engineering is the first level of agent control, but it is not intelligence.

This agent shows how much behavior can be shaped without adding architecture complexity.

⸻

Files Suggested for Agent 02

agent_02/
├── README.md          # High-level description
├── concepts.md        # Prompt constraints & theory
├── prompts.md         # Example prompts
└── experiments.md     # Observed behaviors


⸻

Transition to Agent 03

Next, we will introduce memory.

That is the point where the system stops being just a text generator and starts behaving like an agent over time.