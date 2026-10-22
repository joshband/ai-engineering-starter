# Read-only inventory for an existing repository

Use short notes or a conversation. This is a checklist of **questions**, not a required record or a demand to scan secrets. Preserve any uncommitted work.

| Inspect | Record only what matters |
| --- | --- |
| Repository and task | Owner, revision, intended bounded task, known constraints |
| Instruction entry points | Root/nested `AGENTS.md`, `CLAUDE.md`, Cursor rules, other native guidance; precedence and maintainers |
| Existing authority | Organizational policies, project-specific rules, sensitive operations, approval owner |
| Execution controls | Actual runtime permissions, hooks, tool access, network/data boundaries; distinguish observed behavior from written intent |
| Verification | Existing Make/package commands, CI, tests, lint, security gates, required environment, known blockers |
| Change and release | Branch protection, required reviews, commit/push/PR/merge/deploy authority |
| Existing documentation | Architecture, testing, task intake, review and handoff locations; duplication risks |
| Reversibility | Where optional references could live and how to remove them without losing project-owned guidance |

## Decision boundary

- Do not read credentials, private `.env` files, or unrelated restricted material just to complete an inventory.
- Label uninspected or inaccessible controls **Unverified** rather than assuming they exist or work.
- Before proposing a change, identify the owning maintainer and the precise files/operations allowed.
- If the repository already covers the need, choose [No adoption or Reference only](DECISION_MATRIX.md).

For normative boundaries, see [M1](../../core/standards/ENGINEERING_STANDARD.md), the [taxonomy](../../core/standards/AUTONOMY_AND_RISK.md), and [security interpretation](../SECURITY_BOUNDARIES.md).
