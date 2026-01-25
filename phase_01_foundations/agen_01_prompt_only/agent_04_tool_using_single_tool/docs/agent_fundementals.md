Teach teh agent to use a tool/function instead of just replying with text.

Core concept introduced
Tool/Function Calling
The agent:

1. Understand user intent
2. Decides when to use a tool
3. Calls the tool
4. Return the result

Note: No memory upgrades yet.
no frameworks
no LangChain
no distraction

Mental Model:
Think of Agent 04 as:
"A chatbot that knows it can delegate work"
Example:
. User: "What time is it?"
. Agent: "calls get_current_time()"
. Agent: return results

Agent 04 scope(STRICT)
. One agent
. One tool
. Once decision path

X No database
X no vector stores
X no multi-agent system
X no APIs yet