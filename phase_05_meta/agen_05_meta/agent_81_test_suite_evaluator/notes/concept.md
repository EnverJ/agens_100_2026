# Concept — Agent 81: Test Suite Evaluator

Agent 81 exists because passing tests are not the same as good tests. A CI pipeline that
shows all green gives engineers a sense of confidence, but that confidence may be entirely
misplaced if the test suite consists of fifty shallow happy-path checks and nothing else.
This agent was built to make the distinction visible and measurable. It is the quality
auditor for your testing investment, not the executor of it.

The direct predecessor is Agent 80 (test generator), which writes tests automatically.
Automated test generation is fast but tends to produce tests that assert the obvious.
Agent 81 was designed to sit downstream of Agent 80 and evaluate whether the generated
tests have sufficient depth, variety, and coverage distribution. Without evaluation, a
generator is just a quantity machine. Together they form a generation-evaluation loop.

The concept of weighted scoring is central here. Not all metric failures are equally
serious. A 5% skipped-test rate is mildly concerning; a happy-path to negative ratio of
20:1 is dangerous. The `ScoringConfig` dataclass allows project teams to express their
own weighting priorities rather than accepting a universal default. A payments platform
weights negative-test coverage more heavily than an internal dashboard tool.

Agent 81 feeds forward into Agent 86 (meta-learner), which tracks quality score trends
over time, and into Agent 90 (AI test runner), which uses the feature-area breakdown to
decide which test areas need prioritised execution. The scorecard JSON format is designed
specifically to be consumable by both downstream agents without transformation.
