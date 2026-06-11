# Agent 25 — Working Memory

## Purpose
Agent 25 implements working memory — a fast, ephemeral scratchpad for intermediate reasoning results within a single reasoning cycle. Unlike session memory (Agent 21), working memory is not about conversation history; it is about holding the partial outputs of a multi-step reasoning chain while that chain is running. It clears automatically at the end of each reasoning cycle, keeping it small and fast.

## What This Agent Introduces
A scratchpad memory layer — ephemeral, step-scoped, and purpose-built for multi-step reasoning chains where intermediate results must be passed between steps.

## How It Works
1. At the start of a reasoning cycle, working memory is initialized as an empty dict.
2. Each reasoning step writes its output to a named slot in the working memory dict.
3. Subsequent steps can read from earlier slots to chain their reasoning.
4. At the end of the cycle, working memory is cleared (or optionally flushed to session memory by the caller).

## What It Is NOT
- No persistence — working memory does not survive the end of a reasoning cycle
- No session history — it does not store conversation turns
- No vector search — it is a keyed scratchpad, not a retrieval system
- No LLM reasoning — it stores and returns values, it does not interpret them

## Scope
- Maintain a flat key-value store for the duration of one reasoning cycle
- Support READ, WRITE, and CLEAR operations
- Expose a SNAPSHOT operation to return all current slots
- Automatically clear at cycle end or on explicit CLEAR call

## Key Lesson
Multi-step reasoning requires intermediate storage. Working memory separates the concern of "reasoning" from the concern of "remembering my last step's output" — keeping both clean and purposeful.

## Next Step
Once Agent 25 is complete, proceed to Agent 26.
