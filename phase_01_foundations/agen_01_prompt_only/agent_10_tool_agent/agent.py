use_tool = 'use_tool'
no_tool = 'no_tool'

tool_triggers = [
    'calculate',
    'sum',
    'divide',
    'weather',
    'time',
    'date'
]

def toolDecision(userInput):
    normalize_input = userInput.lower().strip().strip()

    needs_tool = any(
        phrase in normalize_input
        for phrase in tool_triggers
    )
    if needs_tool:
        return use_tool
    else:
        return no_tool


if __name__ == '__main__':
    userInput = input('You: ')
    decision = toolDecision(userInput)
    print(decision)