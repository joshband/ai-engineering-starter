# Worked example — small documentation change

**Illustrative only:** This example is not a claim that the work was executed or that an adopting repository passed its checks. The repository's own instructions take precedence for commands and approvals.

**Request:** Clarify one outdated paragraph in a setup guide. Do not edit code, configuration, agent instructions, permissions, CI, or dependencies.

**Task boundary:** Change the identified paragraph and, if the existing documentation index requires it, its link. Acceptance: accurate wording, no broken relative links, no unrelated diff. For a routine, bounded docs edit, a brief request can be sufficient; no mandatory task form.

**Classification:** Proposed risk **L**, autonomy **A2** (only within explicitly delegated local editing authority), complexity **T1**, workflow **Standard** for the illustrated reviewable edit. These are proposed labels, not a grant to write or publish. Reclassify if the actual task or authority differs; use [taxonomy](../../core/standards/AUTONOMY_AND_RISK.md) and [profiles](../../core/workflows/PROFILES.md).

**Plan:** Read the existing guide and linked source of truth; edit only the authorized text; inspect diff; run the repository's required checks. If there is already an effective process, use it rather than introducing a new one.

**Verification report example (hypothetical, not executed):**

| Check | Example state | What to report |
| --- | --- | --- |
| Relative links | Passed **only if run** | Checked paths and result |
| `git diff --check` | Passed **only if run** | Command and exit code |
| Project verification | Not run / Blocked / Passed / Failed | Exact command, environment, outcome; never imply tests ran |
| Runtime instruction discovery | Unverified | No claim without direct observation |

**Review:** Human reviewer checks scope, accuracy, checks, and whether the added ceremony was useful. **Completed** implementation is not **Accepted** work; merge and release are separate decisions. See [completion contract](../../core/contracts/COMPLETION_CONTRACT.md) and [review procedure](../../skills/review-and-acceptance/SKILL.md).

**Safe handoff:** Record current revision/branch, files changed, what was checked, blockers, unresolved owner decisions, and next safe action. Use the [handoff procedure](../../skills/safe-handoff/SKILL.md) when needed; no mandatory form.

**Optional M5 references:** [task intake](../../skills/task-intake/SKILL.md), [verification](../../skills/change-verification/SKILL.md), [review](../../skills/review-and-acceptance/SKILL.md), [handoff](../../skills/safe-handoff/SKILL.md). No automatic skill invocation is implied.

**Outcome choices:** Adopt the useful reference, revise it, or remove it. If project-required verification is blocked, keep acceptance pending rather than bypassing the gate.
