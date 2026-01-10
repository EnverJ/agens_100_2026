#!/usr/bin/env python3
"""
Agent 01: Prompt-only QA Agent
Fully working on Mac/Linux with Python 3 and latest OpenAI library.
"""

import os
from openai import OpenAI

# Initialize OpenAI client with API key from environment
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Please set your OPENAI_API_KEY environment variable.")
client = OpenAI(api_key=api_key)

def ask_agent(question: str) -> str:
    """
    Simple prompt-only QA agent.
    """
    prompt = f"Answer this question concisely:\n{question}"
    response = client.chat.completions.create(
        # model="gpt-4o-mini",
        # model="gpt-3.5-turbo",
        # messages=[{"role": "user", "content": prompt}],
        # temperature=0.5
        model = "gpt-3.5-turbo",
        messages=[{
            "role":"system", "content":"You are a concise and helpful assistant."},
            {"role":"user", "content":"questions"}]
    )
    return response.choices[0].message.content.strip

if __name__ == "__main__":
    print("=== Agent 01 – Prompt-only QA Agent ===")
    while True:
        question = input("\nAsk a question (or type 'exit' to quit): ")
        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        try:
            answer = ask_agent(question)
            print("Agent 01 Response:", answer)
        except Exception as e:
            print("Error:", e)