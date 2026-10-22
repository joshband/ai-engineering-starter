# M8 — Runtime validation and adoption evidence (planning candidate)

**Status:** Proposed scope for human review; implementation, external pilot edits, acceptance, merge, tag, and release are not authorized by this document.

**Baseline:** M7 Minimal Adoption Decision Kit accepted and squash-merged in [PR #6](https://github.com/joshband/ai-engineering-starter/pull/6). M4 Codex instruction discovery remains [deferred](../validation/m4-codex-runtime-followup.md). M6's bounded documentation pilot has partial verification and deferred adoption acceptance ([record](M6_PILOT_PLAN.md#ct-m6-01-evaluation-and-deferred-verification)).

## Purpose

Collect reproducible, **observed** evidence about how Claude Code and Codex discover and navigate this repository's existing instructions, and whether a maintainer can use the optional adoption kit without duplication. Distinguish static validity, native instruction discovery, agent response behavior, and technical permission enforcement. A single successful session does not establish universal compatibility or security enforcement.

## Proposed scope

1. **Read-only runtime baseline:** Record platform/surface, runtime version if available, starting directory, checkout SHA, instruction files reported active, session freshness, configuration relevant to instruction discovery, and evidence provenance. Never collect secrets or private configuration values.
2. **Two independent adapter smoke tests:** In fresh Claude Code and Codex sessions, check root instruction discovery and canonical routing to the M1 standard, taxonomy, M2 catalog, and Quick/acceptance distinctions. Explicitly distinguish automatically loaded text from links opened by request. Reuse the [M4 Codex follow-up](../validation/m4-codex-runtime-followup.md) as the Codex case, without claiming it closed until its own criteria pass.
3. **Manual adoption decision exercise:** On an approved, non-sensitive repository or a disposable fixture, run a **read-only** inventory using the [M7 kit](adoption-decision/README.md). Record a justified No adoption / Reference only / Selective adoption recommendation and conflicts/owners. No target changes unless separately authorized.
4. **Evidence and comparison:** Report each scenario PASS / FAIL / UNVERIFIED, with transcript excerpts or reproducible commands, environment limits, false positives, and deviations. Record actual runtime behavior without implying permissions are enforced by instructions.
5. **Disposition:** Recommend Accept / Revise / Reject for the M8 evidence package, and identify focused follow-ups rather than expanding scope.

## Scenario matrix

| ID | Scenario | Expected observation | Boundary |
| --- | --- | --- | --- |
| C1 | Fresh Claude Code root session | Root `CLAUDE.md` and M1 imports are shown in actual active context | No claim about all versions |
| C2 | Claude Code policy routing | Correct M1 owner, M2 structural role, Quick no-form option, Completed vs Accepted | Distinguish import from explicit read |
| X1 | Fresh Codex root session | Active root `AGENTS.md` discovered, with any other applicable instructions recorded | Markdown links do not auto-import contents |
| X2 | Codex policy routing | Correct STD owner, Profile H trigger, M2 catalog role, Quick and acceptance boundaries | Read-only, no consequential action |
| A1 | Manual M7 inventory | Decision is justified by observed existing controls and owner; no compulsory adoption | No target edits |
| B1 | Permission boundary | Report actual sandbox/approval configuration if visible; mark enforcement **Unverified** unless independently tested under separate authorization | No destructive/security-bypass experiments |

For each test, record **Observed / Not observed / Unable to test**, supporting evidence, and PASS / FAIL / UNVERIFIED disposition. A correct model answer without proof of automatic discovery does **not** pass the discovery check.

## Entry gates and approvals

- A maintainer must approve the M8 implementation scope, chosen runtimes, environment, and any test repository before execution.
- Read-only tests must not change repository content, credentials, permissions, network policy, hooks, CI, deployment, or project instructions.
- If CLI or cloud runtime is unavailable, mark the affected case UNVERIFIED and preserve the blocker; do not simulate a live test.
- Any external repository edits, paid service usage outside existing authorization, or consequential operations require new explicit approval.

## Proposed deliverables

- Versioned test protocol and minimal environment/evidence capture form (optional Markdown).
- Claude Code and Codex read-only smoke-test transcripts or reproducible command records.
- An M7 adoption decision example with observed inventory and owner/conflict resolution.
- Evidence matrix separating structural checks, discovery, behavior, and enforcement.
- Final M8 acceptance recommendation and follow-up ledger; update the M4 item only if its exact closure criteria are actually met.

## Proposed acceptance criteria

1. The test protocol is reproducible, bounded, read-only, and records version, revision, and active instruction sources where observable.
2. At least one real Claude Code and one real Codex session is attempted; missing runtime evidence is explicitly UNVERIFIED, not a pass.
3. Discovery evidence differentiates native loading from user-requested document reads.
4. Canonical M1 policy ownership and M2 non-authority are preserved; M5/M7 remain optional.
5. A manual adoption decision is grounded in actual inventory, without modifying the target.
6. Results distinguish execution, verification, human acceptance, merge, and release; no automatic enforcement or cross-environment compatibility claims.
7. Structural checks (`python3 validation/validate.py`, unit tests, and diff whitespace check) pass on the M8 implementation branch before any acceptance recommendation; human policy review remains separate.

**Milestone decision requested:** Approve, revise, or reject this bounded M8 scope. This planning branch does not constitute implementation or runtime validation.
