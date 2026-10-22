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

## Candidate verification and remediation — 2026-10-22

The initial branch check found a prohibited private-project marker in the M6 context document added by this PR. `python3 validation/validate.py` exited 1; the full unit suite ran 24 tests with one failure because an existing test invokes that validator. `git diff main...HEAD --check` exited 0. The marker was replaced with a generic scope exclusion without changing the M6 decision. The M7 README also incorrectly said implementation was unauthorized, and the small local-edit example labeled autonomy A2; those statements were corrected to the actual draft status and bounded A1 editing authority. The M7 link test now checks heading fragments as well as target files.

After these corrections, from the repository root:

| Command or review | Observed result |
| --- | --- |
| `python3 validation/validate.py` | Passed, exit 0: 19 required files, 39 Markdown files, 218 relative links, 16 canonical definitions, 16 controls, five schemas, nine valid and 13 intentionally failing fixtures. |
| `python3 -m unittest discover -s validation/tests -v` | Passed, exit 0: 24 tests, including five M7 tests and 19 earlier regression tests. |
| `git diff main...HEAD --check` | Passed, exit 0, no output after the bounded fix commit. |
| M7 link and ownership review | Five kit documents and 32 Markdown links; focused test resolves relative files and fragments. No new STD definition headings, permission settings, native discovery, or mandatory Quick record. |

These checks establish documented structure and selected invariants, not semantic policy equivalence, agent behavior, or enforcement. The M6 Copy That verification blocker and M4 Codex runtime follow-up remain separate and open. **Implementation recommendation:** Accept the optional kit for human architecture review: `docs/ADOPTION.md` explains how to adopt, while this kit supplies explicit skip/reference/selective decisions, conflict ownership, a short example, and removal steps. A mature repository can choose No adoption; no kit form or file is mandatory. Human acceptance, merge, tag, and release remain pending.
