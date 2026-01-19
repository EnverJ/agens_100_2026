"""Agent 05 multi tool agent"""
from gpt4all import GPT4All
import os
import tools

# -------
# Model set up
# -------
MODEL_DIR = os.path.expanduser("~/openAI/agents_100_2026/models")
os.makedirs(MODEL_DIR, exist_ok=True)

MODEL_NAME = "orca-mini-3b-gguf2-q4_0.gguf"
model = GPT4All(
    MODEL_NAME,
    model_path=MODEL_DIR
)

# ---------
# system prompt
# ---------
SYSTEM_PROMPT = """
You are a careful QA assistant
- Answer only question on the conversation
- if you do not know the answer, say "I do not know".
- Be concise and factual
"""

#---------
"""
short term memory
"""
# --------
memory = []

#---------
# Function
# --------

def build_prompt() -> str:
    """Rebuild full prompt from memory"""
    conversation = "\n".join(memory) + "\n"
    return SYSTEM_PROMPT + "\n" + conversation + "Agent: "

def ask_agent(user_input:str) -> str:
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

def agent_05(user_input: str) -> str:
    """Check if the user is asking for a tool, otherwise fall back to GPT"""
    
    # --- SUM TOOL ---
    if user_input.lower().startswith("sum"):
        parts = user_input.split()
        if len(parts) == 3:
            try:
                a = float(parts[1])
                b = float(parts[2])
                response = f"Sum of the two numbers is: {tools.get_sum(a, b)}"
                memory.append(f"Agent: {response}")
                return response
            except ValueError:
                response = "Error: both inputs must be numbers. Please try again like: sum 5 7"
                memory.append(f"Agent: {response}")
                return response
        else:
            response = "Error: please provide exactly two numbers like: sum 5 7"
            memory.append(f"Agent: {response}")
            return response

    # --- TIME TOOL ---
    elif "time" == user_input.lower():
        response = f"Current time is: {tools.get_current_time()}"
        memory.append(f"Agent: {response}")
        return response

    # --- DATE TOOL ---
    elif "date" == user_input.lower():
        response = f"Current date is: {tools.get_current_date()}"
        memory.append(f"Agent: {response}")
        return response

    # --- FALLBACK TO GPT ---
    else:
        return ask_agent(user_input)
    
# -----------------------------
# Agent loop
# -----------------------------
if __name__ == "__main__":
    print("Agent 05 is running. Type 'exit' or 'quit' to stop.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("Agent 05:", agent_05(user_input))

