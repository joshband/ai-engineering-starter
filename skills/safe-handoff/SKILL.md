# Skill: Safe handoff

**Use:** When work is interrupted, transferred, or may have uncertain external side effects.

**Read:** [Handoff contract](../../core/contracts/HANDOFF_CONTRACT.md), [completion contract](../../core/contracts/COMPLETION_CONTRACT.md), [M1 standard](../../core/standards/ENGINEERING_STANDARD.md).

## Procedure

1. Record current objective, authorized scope, repository and exact revision/dirty state, work performed, and actual checks/results.
2. Preserve decisions, dependencies, blockers, unknowns, and any pending approval; distinguish observed facts from assumptions.
3. For an externally consequential operation with uncertain outcome, stop automatic retry. Reconcile its actual external state before repeating; a checkpoint is not idempotency.
4. Identify the next **safe** authorized action and what evidence a successor must inspect.
5. Use a concise narrative or the [handoff template](../../core/templates/HANDOFF.md). Optional structured records can use the [M2 Handoff schema](../../core/controls/schema/handoff.schema.json).

## Output

Resumable context without invented completion, authorization, or side-effect certainty. Record execution and acceptance separately where relevant.
