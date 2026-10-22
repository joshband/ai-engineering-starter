# Minimal adoption decision kit (M7 candidate)

**Use:** An optional, manual decision aid for an existing repository. This is not an installer, new policy, audit certification, or runtime permission system.

Start with the project's actual [instructions and governance](../ADOPTION.md#existing-repository), not this kit. The [M1 standard](../../core/standards/ENGINEERING_STANDARD.md) alone defines STD-01–STD-16; [M2 controls](../../core/controls/README.md) index and structurally validate optional records. [M5 skills](../../skills/README.md) are opt-in procedures, not automatically invoked.

## Choose the smallest useful adoption

1. [Inventory](INVENTORY.md) the existing authority, instructions, checks, and boundaries **read-only**.
2. Use the [decision matrix](DECISION_MATRIX.md) to choose **No adoption**, **Reference only**, or **Selective adoption**. All are legitimate outcomes.
3. If helpful, adapt the [worked example](EXAMPLE.md) to one bounded task; no form is needed for Quick work.
4. Record actual checks and human decisions. [Remove or revise](ROLLBACK.md) only material explicitly introduced by the pilot.

**Human gates:** Obtain permission for the actual repository edits and for any consequential actions. Do not infer approval to commit, push, open a PR, merge, deploy, or release from permission to draft guidance. Existing project instructions, stronger applicable governance, and real runtime permissions remain in effect.

**Evidence boundary:** Passing local links and structural tests does not prove that any external agent discovers guidance, follows it, or enforces permissions. The [M6 Copy That pilot](../M6_PILOT_PLAN.md#ct-m6-01-evaluation-and-deferred-verification) has only partial verification; it does not establish successful adoption.

This kit adds no dependencies, templates that must be completed, CI jobs, hooks, agent configuration, or external service.
