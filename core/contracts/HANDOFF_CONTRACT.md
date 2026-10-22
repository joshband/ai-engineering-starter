# Handoff Contract

Owner of continuation semantics. References STD-01, STD-06, STD-14, STD-15 in the [standard](../standards/ENGINEERING_STANDARD.md).

## Required fields (substantive handoffs)

A usable handoff identifies:

- Current objective and authorized scope
- Work completed and relevant repository/revision (including branch and dirty working state)
- Checks actually run and their outcomes
- Decisions and supporting sources
- Unresolved issues
- Next safe action

These may be concise prose rather than a formal document for low-risk work.

## Conditional fields

Include relevant approval boundaries, evidence locations, recovery/backup locations, uncertain external side effects, and execution/acceptance states when they affect safe continuation. If a revision is unknown, say so; resolve it before relying on revision-specific claims.

## Invariants

- A handoff does not increase delegated authority or supply a missing approval.
- A summary is not automatically a durable execution checkpoint: it cannot restore processes, credentials, runtime state, or external operation outcomes.
- Reinspect actual repository state and reconcile uncertain external effects before acting on them.
- Preserve valuable uncommitted work through an appropriate recovery mechanism.

## Example

Objective: Fix empty input parsing. Scope: local parser/tests, no release. Repository: example/parser, branch fix-empty, base revision recorded in task; one uncommitted parser edit. Completed: guard added. Checks: focused test Failed (expected result differs). Decision: retain API, per task. Issue: expected empty result needs confirmation. Next safe action: inspect documented behavior and resolve expectation with maintainer before further edits. No external actions performed.

[Continuation template](../templates/HANDOFF.md) · [Result semantics](COMPLETION_CONTRACT.md)
