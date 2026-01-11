from gpt4all import GPT4All
import os

# path to model folder(created if needed)
model_dir = os.path.expanduser("~/openAI/agents_100_2026/models")
os.makedirs(model_dir,exist_ok=True)

# Prefer a small, CPU-friendly model that is actively hosted
DEFAULT_MODEL = "orca-mini-3b-gguf2-q4_0.gguf"
FALLBACK_MODEL = "mistral-7b-instruct-v0.2.Q4_0.gguf"

# Load the model (will auto-download on firs run)
def load_model():
    try:
        return GPT4All(DEFAULT_MODEL, model_path=model_dir)
    except Exception as e:
        print(f"warning: failed to load'{DEFAULT_MODEL}':{e}")
        print("Trying fallback model...")
        return GPT4All(FALLBACK_MODEL, model_path=model_dir)
model = load_model()

def ask_agent(question:str) ->str:
    """send question to local model and return answer"""
    response = model.generate(question)
    return response
if __name__ == "__main__":
    print("=== Agent 02 -- Local GPT4All ===")
    while True:
        q = input ("\nAsk a question (or type 'exit'): ")
        if q.lower() in ("exit", "quit"):
            break
        answer = ask_agent(q)
        print("\nAgent", answer)