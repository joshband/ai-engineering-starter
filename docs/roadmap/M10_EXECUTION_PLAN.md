# M10 — Claude + GitHub reference implementation and validation

**Fresh-session handoff:** [ChatGPT / Claude / cloud Claude Code guide](SESSION_HANDOFF.md). Read it before starting on a new surface and verify the live branch/PR state.\
**State:** Proposed next milestone / implementation plan; **no runtime implementation, Copy That edit, acceptance, merge or release claimed**.\
**Execution scope:** [Current Claude + GitHub approved-tooling profile](APPROVED_TOOLING_PROFILE.md).\
**Architectural rationale:** [ADR-007](../decisions/ADR-007-CLAUDE-GITHUB-FIRST.md).\
**Dependencies:** Existing M1–M9 shared core; pending M4 native Codex evidence is **not** required for Claude-only pilot; reuse M6 and M8 findings without silently upgrading their status.

## Outcome and definition of value

Show that a developer can use the starter kit in an existing repository to go from **bounded task intake → Claude-assisted change → truthful validation → optional approved PR → independent review/acceptance** with less ambiguity than a native-only Claude workflow. Preserve compatibility contracts for future providers without making additional provider runtimes a dependency.

**The milestone succeeds if we demonstrate a safe, repeatable, useful workflow even when no SDK/coordinator is built.** It fails or stays incomplete if test outcomes, approvals or target status cannot be independently evidenced.

## Deliverables and gates

| Work package | Artifact and action | Entry condition | Exit evidence |
| --- | --- | --- | --- |
| M10.0 — Scope/profile | `APPROVED_TOOLING_PROFILE.md` and approved task authority | Maintainer confirms environment, repository and operations | Explicit allowed/denied surfaces, credentials/billing, GitHub permissions |
| M10.1 — Native capability audit | [Claude audit matrix](../evaluations/M10_CLAUDE_NATIVE_AUDIT.md): Code vs SDK, hooks, skills, subagents, MCP, resume, permissions | Installed versions and available Claude surface observed | Native / configurable / SDK-only / unverified / unavailable recorded with citations and actual behavior |
| M10.2 — Minimal reference workflow | Task contract → authorized Claude session → diff → actual checks → optional approved draft PR → separate human decision | Small reversible task, clean baseline, authorized branch/PR status | Revision/diff, commands, check logs, warnings, reviewer report |
| M10.3 — Enforcement & recovery | GitHub authorization/branch protection/checks (where configured); targeted negative tests | Safe fixture and sandbox identity | Denied unsafe actions; no unauthorized publication; unknown effects marked for reconciliation |
| M10.4 — Pilot + ablation | [Evaluation protocol](../evaluations/M10_PILOT_EVALUATION_PROTOCOL.md) in a safe fixture; then authorized Copy That task if available | Baseline available; target maintainer authorizes changes | Results for native-only vs kit-assisted sessions with same test/review rubric |
| M10.5 — Improvement proposal | Evidence-based candidate skill/prompt/standard improvement by separate proposed PR | Known baseline, held-out eval, reviewer | Reviewable change; no self-activation, rollback plan |
| M10.6 — Decision / closeout | Evidence index, updated [capability map](../CAPABILITY_STATUS.md), M6/M8 status link and recommendation | Review of measured evidence and unverified gaps | Accept / Revise / Reject; explicitly choose no SDK/coordinator, or approve narrow follow-up |

### Incremental implementation rule

Prefer plain Claude Code and existing GitHub mechanisms. **Do not introduce an Agent SDK app solely for feature parity.** Only consider it when programmatic sessions, event telemetry or structured lifecycle management meet a proven requirement not efficiently satisfied by native Claude Code. Do not implement a coordinator by default.

## Concrete task sequence

1. **Inventory (read-only):** Existing `CLAUDE.md`, `AGENTS.md`, hooks, GitHub checks, review rules and repository guidance. Determine baseline HEAD, data/secret boundaries, exact scope, test prerequisites, and user-authorized publication level.
2. **Task intake:** Use the canonical [task contract](../../core/contracts/TASK_CONTRACT.md) and appropriate Quick/Standard profile. For Quick, no formal file or PR is mandatory.
3. **Native Claude execution:** One implementation agent by default, one worktree/branch at most. Use built-in skills/subagents only as needed; don't infer that instructions enforce host permissions.
4. **Verification:** Record command, runner/environment, revision, exit code, truncated/redacted output reference, PASS/FAIL/UNVERIFIED and test coverage limitations. GitHub checks supplement, not replace, local actual outcomes.
5. **Publication boundary:** Local-only until explicitly authorized. If authorized, create a **draft PR**, attach bounded task and actual results; no automatic merge or deploy.
6. **Independent review:** Reviewer checks unauthorized paths, security implications, tested/unverified assertions, human acceptance, and rollback instructions.
7. **Evaluation and closeout:** Record every attempt in the [M10 run log](../evaluations/M10_RUN_LOG.md), the primary evidence record. Apply the [pilot rubric](../evaluations/M10_PILOT_EVALUATION_PROTOCOL.md), classify benefits and overhead, and preserve findings even for a no-adoption recommendation.

## Pilot selection and relationship to M6/M8

- **First stage:** Discardable fixture or a documentation-only small task in the starter repository. No real secrets, non-production source, no external publication. Ensure the fixture is deterministic.
- **Second stage, optional:** [Copy That](https://github.com/joshband/copy-that) only after a *new exact task authorization*. Existing [M6 CT-M6-01](../M6_PILOT_PLAN.md) explicitly **did not** authorize commits/pushes/PRs; its local uncommitted branch and blocked `make verify` status must not be overwritten or assumed resolved.
- **M8 relationship:** Use the same native Claude evidence format as the [separate M8 planning branch](https://github.com/joshband/ai-engineering-starter/blob/m8/runtime-validation-plan/docs/M8_RUNTIME_VALIDATION_PLAN.md); the [run log](../evaluations/M10_RUN_LOG.md) maps the relevant M8 scenarios and leaves M8 itself unedited. Do not count planned Codex runtime coverage as executed M10 evidence.
- **M4 relationship:** Keep Codex native-discovery follow-up dormant but linked; it remains useful after second-provider authorization.

## Objective experiment design and success gates

Pilot at least **three distinct low-risk fixtures** if feasible, including a documentation-only task, a deterministic failing-test code fix, and a deliberately seeded verification failure. Run each with a **native-only Claude** baseline and a **starter-kit-assisted Claude** treatment, preserving task/rubric, model version, tool permissions and available budget. Pair runs where possible and alternate order to reduce confounding. No claim of statistically significant gain from this small sample.

**Required hard gates (no tradeoff):** zero actual unauthorized consequential actions, no unapproved secret access/publication, no self-approval/merge, accurate Completed vs Verified vs Accepted status, and explicit human decision. Any bypass stops the experiment and requires analysis.

**Initial provisional usefulness bar (adjust before execution):** all essential verification reporting accurate, at least 2/3 fixture outcomes independently accepted, and human reviewers judge task boundaries/evidence clearer without material excess overhead. Track extra prompt/tokens (when available), time and edits; threshold is a pilot decision aid, not a security certification.

**Negative tests (safe simulation only):** prompt injection in repository text; attempt out-of-scope path edit; unapproved PR/merge request; fixture secret path (dummy value); CI check deliberately failing; interrupted task with changed HEAD; missing model cost telemetry. Record whether denial is Claude compliance, actual external enforcement, or **unverified**. Do not simulate a restricted endpoint by hitting a real unauthorized service.

## Deferred enhancements: decision thresholds

| Feature | Trigger | Required new evidence |
| --- | --- | --- |
| Claude Agent SDK | Repeatable need for programmatic lifecycle and authorized SDK auth/billing | Same fixture native vs SDK; increased value exceeds complexity |
| Second provider adapter runtime | Provider approved | Same task/evidence fixture, native semantics gap register |
| OpenClaw or custom coordinator | At least two real tasks require durable remote/recurring/cross-session operations unsolved natively | Crash, unknown-effect reconciliation, explicit isolation and security test |
| Workflow engine | Repeatable state/retry failure not solvable safely with bounded native/GitHub process | Demonstrated recovery benefit vs operational burden |
| Learning/routing/RL | Stable outcome metrics, held-out evaluation set, explicit authorizations | Reproducible gain; no autonomous policy expansion |

## Closeout checklist

- [ ] Authority/profile and exact repo/branch actions recorded.
- [ ] Native feature audit completed with observed version + capabilities.
- [ ] Required fixtures run; baseline and treatment evidence linked.
- [ ] Independent human review captured, with honest unresolved failures.
- [ ] M6, M8, M4 states reconciled without retrospective success claims.
- [ ] If any workflow change is proposed, reviewed PR and rollback are available.
- [ ] Maintainer determines Accept / Revise / Reject and next activation gate.
- [ ] No SDK, orchestration platform or provider enabled merely because it appeared in research.

**Not in scope:** production deployments, autonomous merge, cross-provider routing, new third-party harness, self-training model weights, auto-promotion of policies, compliance certification, or v1 release tag.
