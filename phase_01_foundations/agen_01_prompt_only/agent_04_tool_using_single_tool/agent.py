"""
Agent 04 - Tool-Using Agent with GPT4All and Short-Term Memory
"""

from gpt4all import GPT4All
import os
from tools import get_current_time

# -----------------------------
# Model setup
# -----------------------------
MODELS_DIR = os.path.expanduser("~/openAI/agents_100_2026/models")
os.makedirs(MODELS_DIR, exist_ok=True)

MODEL_NAME = "orca-mini-3b-gguf2-q4_0.gguf"
model = GPT4All(
    MODEL_NAME,
    model_path=MODELS_DIR
)

# -----------------------------
# System prompt
# -----------------------------
SYSTEM_PROMPT = """
You are a careful QA assistant.
- Answer only based on the conversation.
- If you do not know the answer, say "I don't know".
- Be concise and factual.
"""

# -----------------------------
# Short-term memory
# -----------------------------
memory = []

# -----------------------------
# Functions
# -----------------------------
def build_prompt() -> str:
    """Rebuild full prompt from memory"""
    conversation = "\n".join(memory) + "\n"
    return SYSTEM_PROMPT + "\n" + conversation + "Agent: "

def ask_agent(user_input: str) -> str:
    """Ask GPT4All model using memory"""
    memory.append(f"User: {user_input}")

    prompt = build_prompt()

    response = model.generate(
        prompt,
        max_tokens=300,
        temp=0.3
    )

    memory.append(f"Agent: {response}")
    return response

def agent_04(user_input: str) -> str:
    """
    First check if the user is asking for a tool (current time)
    Otherwise, fallback to GPT
    """
    if "time" in user_input.lower():
        return f"Current time is: {get_current_time()}"
    else:
        # fallback to GPT model
        return ask_agent(user_input)

# -----------------------------
# Agent loop
# -----------------------------
if __name__ == "__main__":
    print("Agent 04 is running. Type 'exit' or 'quit' to stop.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("Agent 04:", agent_04(user_input))