# Agent Fundamentals — Agent 44: Consensus

## What This Agent IS

- A majority voter that calls N independent agent instances with the same question and counts their answers
- A reliability layer that reduces single-agent error rates through independent repetition and vote aggregation
- An ensemble coordinator that treats N agent calls as an ensemble of independent predictors
- A confidence reporter that quantifies certainty as the fraction of agents that voted for the winning answer
- A transparency provider that includes the full vote breakdown in its output, not just the winner

## What This Agent IS NOT

- Not a debate moderator — agents do not see each other's answers; there is no exchange of arguments or rebuttals between agent instances
- Not an answer synthesizer — the output is the winning vote, not a synthesized explanation that merges the reasoning from all agents
- Not a weighted judge — every agent instance has the same vote weight; an agent that expresses high confidence does not count more than one that expresses uncertainty
- Not a guarantee of correctness — if all N agents independently produce the same wrong answer, the consensus will be wrong; ensemble methods reduce but do not eliminate error rates

## Input

```python
question: str          # The question or task requiring a discrete decision
n_agents: int = 3     # Number of independent agent calls to make (use odd numbers)
```

## Output

```python
{
    "answer": str,           # The winning answer (majority vote)
    "votes": dict,           # Full tally: { answer_value: vote_count, ... }
    "confidence": float      # Fraction of agents that voted for the winner (0.0 to 1.0)
}
```

## Answer Types Supported

Consensus works for discrete, parseable answer types:
- Binary: yes/no, true/false, pass/fail
- Categorical: A/B/C, bug/feature/question, critical/high/medium/low
- Numeric (discretized): 1-5 rating, 0-100 score rounded to nearest 10

Consensus does NOT work for open-ended answers where two responses can be semantically equivalent but lexically different ("The answer is B" vs "B" vs "Option B").
