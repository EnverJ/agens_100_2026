# Architecture — Agent 44: Consensus

## Full Vote Flow

```
Question
   │
   ├──► [Agent Instance 1] ──► Answer: "B"
   │
   ├──► [Agent Instance 2] ──► Answer: "B"  ← majority
   │
   └──► [Agent Instance 3] ──► Answer: "A"

Vote Tally: B=2, A=1  →  Winner: "B"
Final Output: { answer: "B", votes: { "B": 2, "A": 1 }, confidence: 0.67 }
```

## 5-Agent Variant

```
Question
   │
   ├──► [Agent 1] ──► "C"
   ├──► [Agent 2] ──► "B"
   ├──► [Agent 3] ──► "C"
   ├──► [Agent 4] ──► "C"
   └──► [Agent 5] ──► "B"

Vote Tally: C=3, B=2  →  Winner: "C"
Final Output: { answer: "C", votes: { "C": 3, "B": 2 }, confidence: 0.60 }
```

## Internal Logic

```python
def run_consensus(question: str, n_agents: int = 3) -> dict:
    responses = []
    for i in range(n_agents):
        response = call_agent(question)          # independent call, no shared context
        answer = parse_answer(response)          # extract discrete answer value
        responses.append(answer)

    vote_tally = Counter(responses)
    winner, winner_count = vote_tally.most_common(1)[0]
    confidence = winner_count / n_agents

    return {
        "answer": winner,
        "votes": dict(vote_tally),
        "confidence": confidence
    }
```

## Independence Requirement

```
[Agent 1]  ──┐
[Agent 2]  ──┤──►  No shared context between calls
[Agent 3]  ──┘      Each call is a fresh API request
                     Temperature > 0 for sampling variation
```
