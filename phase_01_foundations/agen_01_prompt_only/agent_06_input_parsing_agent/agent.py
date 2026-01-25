"""agent 06 input parsing agent"""
from gpt4all import GPT4All
import os
import tools


def agent_06(user_input:str) -> str:
    # sum
   
    part = user_input.split()
    if len(part) == 3 and part[0].lower() == "add":
         try:
              a = float(part[1])
              b = float(part[2])
              return f"sum of the two number is : {tools.get_sum(a, b)}"
         except ValueError:
              return f"Error: please enter two valid numbers"
       
    
            
    command = user_input.lower()
    if command.startswith("time"):
        response = f"current time is : {tools.get_current_time()}"
        return response
    if command.startswith("date"):
            response = f"current date is : {tools.get_current_date()}"
            return response
    return f"unknown error"

      
#  Agent loop
if __name__ == "__main__":
    print("Agent 06 is running. Type 'exit' or 'quit' to stop.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("Agent 06:", agent_06(user_input))

            