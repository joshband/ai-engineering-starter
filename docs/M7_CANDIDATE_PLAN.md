# M7 — Candidate capability planning

**Status:** M7 implementation candidate prepared on a separate branch for draft-PR review. Human acceptance, merge, tag, release, and target-repository modifications remain unauthorized.

## Decision context

M1–M3 and M5 are accepted; M4 remains provisionally accepted with a deferred Codex runtime smoke test. The [M6 CT-M6-01 pilot](M6_PILOT_PLAN.md#ct-m6-01-evaluation-and-deferred-verification) reported a bounded docs-only example in Copy That. Relative links and whitespace passed; the target's `make verify` did not reach tests because of shell/environment setup. M6 adoption acceptance remains Deferred.

Copy That already has maintained shared agent instructions, Claude/Cursor integration, checks, and governance. This is evidence against mandatory wholesale installation. One partial documentation pilot does **not** validate native skill invocation, permission enforcement, or general usability.

## Problem worth solving

Help a maintainer decide **what to adopt, what to reference, and what to leave alone** in an existing repository. Preserve established project authority and keep adoption reversible, without introducing a new policy layer or service.

## Candidate M7 options

| Candidate | Benefit | Dependency / risk | Initial preference |
| --- | --- | --- | --- |
| **A. Minimal adoption decision kit**: concise inventory, conflict/ownership matrix, optional task/verification/handoff examples, rollback checklist | Responds directly to M6's duplication finding; useful without agent runtime access | Must not repeat M1 standards or force Quick records | **Preferred for scoping** |
| B. Additional independent pilot | Broadens evidence before general claims | Needs another target and human permission; may encounter environment blockers | Good complementary evidence, not a prerequisite for planning A |
| C. Native skill packaging/discovery | Tests agent-specific invocation | Requires separate adapter/runtime validation; portability risk | Defer until actual demand and available runtimes |
| D. Automated installer/enforcement | Potential convenience | High scope, authority and security risk; no demonstrated need | Do not pursue now |

## Proposed bounded M7 scope (subject to approval)

Create a **vendor-neutral, manual adoption decision kit** within this starter repository:
- a short existing-repository inventory checklist, including existing `AGENTS.md`, `CLAUDE.md`, scoped rules, hooks, CI, ownership, and project constraints;
- an adoption/skip decision matrix, emphasizing conflicts, evidence, and reversibility;
- one optional example of a low-ceremony task boundary, verification report, and safe handoff, referencing M1/M2/M5 rather than duplicating requirements;
- a removal/rollback path and validation of documentation links and canonical policy ownership.

No modifications to Copy That; no mandatory templates, runtime configuration, hooks, CI/CD, installer, schema revision, policy rewrite, agent permission claim, or external service.

## Proposed acceptance criteria

1. M1 remains the only normative STD policy authority; M2 retains its structural role.
2. An existing repo with mature controls can legitimately choose **reference-only** or **no adoption**.
3. Quick work remains form-free; higher-risk work follows existing approvals.
4. New material has valid links, an explicit conflict/ownership resolution path, and rollback guidance.
5. Run `python3 validation/validate.py`, `python3 -m unittest discover -s validation/tests -v`, and diff whitespace checks; report actual results.
6. Any integration or live-runtime claims are marked Unverified until observed.
7. Human reviews the proposal and implementation separately; no merge/tag/release without authorization.

## Dependency and gate assessment

- **Not blocked:** M7 problem definition, architecture/design review, and bounded documentation implementation in the starter repository, after separate authorization.
- **Blocked:** Claims of successful Copy That adoption or compliance with its full definition of done; anything requiring native skill discovery or live permission guarantees.
- **Follow-up:** CT-M6-01-V1 remains tracked in the M6 plan. It need not block an adoption decision kit that makes no runtime or release claim.

## Implementation review gate

Candidate A scope was approved for implementation and a draft PR. Review the [manual adoption decision kit](adoption-decision/README.md), deterministic tests, and validation evidence before deciding Accept, Revise, or Reject. A draft PR is not human acceptance or merge authorization.
