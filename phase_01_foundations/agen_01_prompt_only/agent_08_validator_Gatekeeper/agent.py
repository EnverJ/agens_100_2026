VALID = "VALID"
INVALID = "INVALID"
maxInput = 100
blocked_value = ["kill", "mad", "die"]

def validate(user_input):
    normalized_input = user_input.lower()
    contains_blocked_phrase = any(phrase.lower() in normalized_input for phrase in blocked_value)

    if len(user_input) == 0 or len(user_input) > maxInput or contains_blocked_phrase:
        return INVALID

    return VALID