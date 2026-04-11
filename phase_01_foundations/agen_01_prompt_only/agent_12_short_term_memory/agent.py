_session_memory = []

def storeMemory(context):
    entry = {
        'user_input': context.get('user_input', ''),
        'timestamp': context.get('timestamp', ''),
        'memory_flag': context.get('memory_flag', 'ignore'),
        'tool_flag': context.get('tool_flag', 'no_tool'),
    }
    _session_memory.append(entry)
    updated_context = dict(context)
    updated_context['short_term_memory'] = list(_session_memory)
    return updated_context

def retrieveMemory():
    return list(_session_memory)

def clearMemory():
    _session_memory.clear()


if __name__ == '__main__':
    import datetime

    while True:
        userInput = input('You (or "show" / "quit"): ').strip()
        if userInput.lower() == 'quit':
            break
        if userInput.lower() == 'show':
            memory = retrieveMemory()
            print(f'Short-term memory ({len(memory)} entries):')
            for i, entry in enumerate(memory, 1):
                print(f'  {i}. {entry}')
            continue

        context = {
            'timestamp': datetime.datetime.now().isoformat(),
            'user_input': userInput,
            'memory_flag': 'store',
            'tool_flag': 'no_tool',
            'logs': [],
        }
        updated = storeMemory(context)
        print(f'Stored. Memory size: {len(updated["short_term_memory"])}')
