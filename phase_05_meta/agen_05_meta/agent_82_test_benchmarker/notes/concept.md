# Concept — Agent 82: Test Benchmarker

Agent 81 asked "are our tests good?" Agent 82 asks "are our tests fast?" These are
complementary but distinct questions. A test suite can score highly on Agent 81's quality
scorecard — excellent negative test coverage, low skip rate, good feature distribution —
and still take two hours to run. Speed is not quality, and quality is not speed. Agent 82
was built to close the measurement gap and treat the testing infrastructure as a
first-class performance concern.

Why test performance matters is not obvious until you've sat through a 45-minute CI
pipeline waiting for a merge to unblock. The developer feedback loop is the single most
important determinant of sustained development velocity. When tests are slow, developers
batch their commits to avoid the wait, which means each batch is larger and harder to
debug when the suite fails. Parallel runner efficiency compounds this: an under-configured
xdist setup on a 16-core machine may run no faster than a single-core setup due to worker
contention or test isolation overhead. Agent 82 makes these inefficiencies visible.

Benchmark comparison is the conceptual centrepiece of this agent. A single timing
measurement is a data point; a comparison against a baseline is a signal. The agent
introduces the concept of a rolling benchmark baseline — a stored JSON file that
accumulates per-run measurements and allows delta computation. The statistical choice of
p95 over mean is deliberate: mean durations are dominated by fast tests and mask slow
outliers, while p95 captures the "long tail" that actually determines how often developers
are blocked waiting for the suite to clear.

The benchmark data feeds directly into Agent 90 (AI test runner), which uses per-category
duration data to make intelligent decisions about test scheduling — running fast unit tests
first to give early feedback while long integration tests run in parallel. Without Agent
82's structured timing output, Agent 90 has no objective basis for scheduling decisions.
The relationship is producer-consumer: Agent 82 measures, Agent 90 acts on the
measurements.
