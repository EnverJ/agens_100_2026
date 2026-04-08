import datetime

def buildContext(userInput, memoryFlag=None, toolFlag=None, logs=None):
    context = {
        'timestamp': datetime.datetime.now().isoformat(),
        'user_input': userInput.strip(),
        'memory_flag': memoryFlag if memoryFlag is not None else 'ignore',
        'tool_flag': toolFlag if toolFlag is not None else 'no_tool',
        'logs': logs if logs is not None else [],
    }
    return context


if __name__ == '__main__':
    userInput = input('You: ')
    context = buildContext(userInput)
    print('Context Object:')
    for key, value in context.items():
        print(f'  {key}: {value}')
