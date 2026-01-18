"""
Agent -3 - Prompt-Controlled QA agent short-term memory
- Local model
- Short-term memory using python list
- Memory is lost when program exits

"""

from gpt4all import GPT4All
import os

# model setup

model_dir = os.path.expanduser("~/openAI/agents_100_2026/models")
os.makedirs(model_dir,exist_ok=True)

MODEL_NAME = "orca-mini-3b-gguf2-q4_0.gguf"

model = GPT4All(
    MODEL_NAME,
    model_path=model_dir
)

# System prompt (restriction)

SYSTEM_PROMPT = """

You are a careful QA assistant. 
- Always only based on the conversation. 
- If you do not know the answer, say "I do not know".
- Be concise and factual
"""

"""
Short- term memory
"""
memory = [] # stores the conversation as text

"""
Agent loop
"""

def build_prompt():
    """Rebuild full prompt from memory."""
    conversation = "\n".join(memory)
    return SYSTEM_PROMPT + "\n" + conversation + "\nAgent: "
def ask_agent(user_input:str) -> str:
    #store memory input
    memory.append(f"user: {user_input}")

    # rebuild prompt with history
    prompt = build_prompt()

    # generate response
    response = model.generate(
        prompt,
        max_tokens= 300,
        temp=0.3
    )
    # store agent response
    memory.append(f"Agent: {response}")

    return response

if __name__ == "__main__":
    print("===Agent -3 - prompt + short-term Memory ===")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ("exit","quit"):
            print("Exiting. Memory cleared")
            break
        answer = ask_agent(user_input)
        print("\nAgent", answer)