## Core Concept – Agent 11

Agent 11 is the Context Builder Agent.

It aggregates user input, memory flags, tool flags, and logs into a single unified context object.

This context object is passed to downstream agents so they have everything they need in one place.

Agent 11 is purely deterministic and does not reason or make decisions.
It assembles data, adds a timestamp, and returns a structured dictionary.

The purpose of Agent 11 is to establish a single source of truth for each interaction,
ensuring that all downstream agents work from the same consistent context.

Without a context builder, each agent would need to independently gather its own inputs,
leading to inconsistency and duplication across the system.
