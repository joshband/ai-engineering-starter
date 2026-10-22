# M6 — Pilot adoption plan (planning candidate)

**Status:** Pilot CT-M6-01 evaluated with partial verification; adoption recommendation **Revise**, human acceptance **Deferred**. Follow-up is tracked below. M6 is not fully accepted or released.

**Baseline:** Accepted M1–M3 and M5; provisionally accepted M4. [M4 runtime follow-up](../validation/m4-codex-runtime-followup.md) remains open. No release tag is implied.

## Purpose

Evaluate whether the portable standard and five optional procedures help with **one real, bounded engineering task** in an existing repository without adding disproportionate ceremony, duplicating existing policy, or confusing instructions with permissions. This is an adoption experiment, not an automation rollout.

## Selected pilot — CT-M6-01

- **Target:** [joshband/copy-that](https://github.com/joshband/copy-that), baseline `main` at `bdd428281eef6d3fc0dc22874b9283b3ab163d77`.
- **Approved task:** Documentation-only example of task intake, verification, review, and safe handoff. Approval did **not** authorize commit, push, PR, or merge.
- **Local-only work:** `m6/ct-m6-01-docs-pilot`; clean before edits. Reported two-file diff: new `docs/guides/ENGINEERING_TASK_PILOT.md` and one index link in `DOCUMENTATION_INDEX.md` (48 insertions, one deletion). No target publication.
- **Existing controls:** Copy That already maintains root `AGENTS.md`, `CLAUDE.md`, Cursor rules, hooks, CI, and protected `main`. These were not changed.
- **Evidence provenance:** The implementation and command outcomes below were reported by the pilot executor; this starter-kit repository has not independently inspected the uncommitted local diff or rerun target checks.

## Target selection (requires maintainer decision)

Choose one existing repository with a small, reversible, non-production task, available test commands, and existing instructions that can be inventoried. Record repository name, maintainer, baseline SHA, language/tooling, current instruction entry points, and proposed pilot task. Do not default to a production or client repository.

## Phases and evidence

1. **Baseline:** Inspect repository instructions, CI, existing policies, tests, branch protections, secrets boundaries, and current task workflow. Record what is already working. No edits.
2. **Adoption proposal:** Specify which M1/M2 documents and optional M5 skills would be copied or referenced. Propose minimal native entry-point changes, with exact relative links. Identify conflicts and owners. Obtain approval before writing to target.
3. **Bounded task:** Execute one authorized Quick or Standard task with stated risk (L/S/H), autonomy (A0–A4), complexity (T0–T3), and acceptance criteria. Keep an equivalent non-adopted baseline or document why comparison is unavailable.
4. **Verification:** Run the target's actual relevant checks; record commands, results, time/effort, interruptions, and required human interventions. Record agent/runtime/version and observed instruction discovery when available. Mark missing evidence Unverified.
5. **Evaluation:** Compare usefulness, instruction conflicts, overhead, review quality, handoff clarity, and unexpected behavior. Preserve Completed versus Accepted and merged versus released.
6. **Disposition:** Recommend Adopt, Revise, or Reject with evidence. Do not generalize from a single pilot to universal compatibility.

## Success measures

- Existing instructions and security controls preserved; no destructive replacement.
- One bounded task completed and independently reviewed with honest verification.
- Canonical STD requirements remain owned by M1; M2 shape validation is not authorization.
- Quick work has no mandatory record; use skills only when helpful.
- Evidence of practical value or an explicit finding that overhead outweighs benefit.
- Clear limitations and a repeatable adoption checklist.

## Out of scope

No auto-installation, agent skill discovery, production deployment, release automation, model routing, orchestration, SSMX integration, or changes to M1–M5 normative interfaces. No assumption that a pilot validates runtime permission enforcement.

## Required human gate

**Before touching any pilot target:** maintainer confirms the repository, exact task, allowed files/operations, and whether a PR is desired. Until then, M6 remains planning-only.

## CT-M6-01 evaluation and deferred verification

| Check | Reported outcome | Interpretation |
| --- | --- | --- |
| `git diff --check` | Passed, exit 0 | Whitespace only |
| Pilot relative links | Passed, five links resolve | Link integrity in local pilot |
| `make verify` | Failed, exit 2 before tests | Existing Make recipe uses Bash-specific `source` under `/bin/sh` |
| `make SHELL=/bin/bash verify` | Failed, exit 2 before tests | `.venv/bin/activate` absent in the environment |
| Application tests | Not run | No application regression evidence |

**Finding:** The example reportedly improves the visibility of task boundaries, check results, approval points, and next safe actions, but the target already has a mature agent workflow. Selective, optional adoption may be useful; a wholesale copy would duplicate existing guidance. This is qualitative evidence from one docs-only task, not proof of agent runtime compliance or cross-repository effectiveness.

**Disposition:** **Revise / partial outcome**. Execution Completed for the bounded local documentation edit; Verification Partial (two documentation checks passed; full target gate blocked); Acceptance Deferred; publication Not authorized. The target's definition of done remains unmet. Do not represent this as accepted target adoption or a passing application test suite.

**Deferred follow-up (CT-M6-01-V1):** In a configured Copy That environment, confirm the actual Make shell and dependency setup, run `make verify` with an appropriate shell (for example `make SHELL=/bin/bash verify` only if compatible with local tooling), record full output and exit code, inspect the final uncommitted diff, then request human acceptance and separate publication approval. Do not change the target Makefile or bypass checks under this follow-up without a new scope approval. Retain the local branch and do not commit/push/PR/merge.

**M6 milestone boundary:** This partial pilot can inform later planning. It does not close full M6 acceptance. Further independent pilots and design work may proceed, but any feature or release claim requiring validated target behavior must wait for relevant evidence. Separate target-repository required gates from milestone evaluation evidence without waiving either.

## Deliverables

A target inventory, approved adoption diff, one-task execution report, measured evaluation, rollback/removal notes, and M6 acceptance recommendation. Track unknowns and any blocked action explicitly.
