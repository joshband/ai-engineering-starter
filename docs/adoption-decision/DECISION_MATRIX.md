# Adoption decision and conflict matrix

This is guidance for a maintainer, not a policy override. Select **one primary posture** and note any narrowly justified exception.

| Situation | Default posture | Rationale / safe next action |
| --- | --- | --- |
| Mature maintained agent instructions and verification | **Reference only** or **No adoption** | Existing project authority stays primary; link to useful [M5 procedures](../../skills/README.md) only when they add value |
| Existing instructions conflict with a proposed copied rule | **No adoption pending owner decision** | Identify both sources, owner, applicable organizational obligations, and exact conflict; do not silently replace |
| No shared guidance but a bounded task would benefit | **Selective adoption** | Add only agreed references or one procedure; preserve links and existing conventions |
| Quick low-risk edit with clear authority | **No new form** | Brief outcome, edit, inspect, and report check; [workflow profiles](../../core/workflows/PROFILES.md) |
| Material/high-risk or consequential action | **Escalate to responsible owner** | Apply actual project governance and [M1 standard](../../core/standards/ENGINEERING_STANDARD.md); no inferred approval |
| Agent-native skill discovery or permissions untested | **Manual references only** | Mark runtime claims Unverified; do not imply automatic invocation or enforcement |
| Required verification unavailable | **Defer acceptance / record blocker** | Report exact command and status; no fabricated pass, no automatic waiver |

## Minimal conflict/ownership note

For each material conflict, capture: **existing source**, **proposed reference**, **responsible owner**, **stronger applicable obligation**, **decision**, **evidence**, and **removal path**. A sentence or a small table is sufficient. An agent cannot authorize its own exception.

## Explicit skip criteria

Choose **No adoption** if the existing process is clear and testable, the new material would duplicate guidance, or no owner can resolve a conflict. Choose **Reference only** when existing instructions are adequate but an occasional task can benefit from a linked M5 procedure. Choose **Selective adoption** only for a concrete gap and an approved, reversible change.

See [inventory](INVENTORY.md), [example](EXAMPLE.md), [rollback](ROLLBACK.md), and [existing-repository adoption](../ADOPTION.md#existing-repository).
