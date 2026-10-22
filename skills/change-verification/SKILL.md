# Skill: Change verification

**Use:** Before claiming implementation is complete, particularly for material changes. Small Quick edits may need only a diff inspection or an inexpensive targeted check.

**Read:** [Verification standard](../../core/standards/ENGINEERING_STANDARD.md), [completion contract](../../core/contracts/COMPLETION_CONTRACT.md), [workflow profiles](../../core/workflows/PROFILES.md).

## Procedure

1. Identify the authorized change, acceptance criteria, relevant failure modes, and the exact revision/working tree checked.
2. Choose checks proportionate to behavior and risk. Prefer targeted tests, diff inspection, and relevant existing project commands; add broader tests when warranted.
3. Execute only authorized checks. For each, capture command or review method, actual result, context, and material limitations. Do not present an unrun test as Passed.
4. Inspect changed files for unintended scope, dependencies, secrets, and documentation drift within available evidence. Structural validation is not semantic proof.
5. Report verification statuses exactly as defined by the [completion contract](../../core/contracts/COMPLETION_CONTRACT.md): Passed, Failed, Not run, Not applicable, or Unverified.
6. Report execution and acceptance separately. If an essential criterion remains unverified, use Partial or Blocked rather than Completed.

## Output

Concise verification matrix, execution state, acceptance state (typically Pending review), limitations, and next safe action. Merge and release are independent; do not claim either without evidence.
