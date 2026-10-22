# M6 — Pilot adoption plan (planning candidate)

**Status:** Planning started; target repository and pilot task not yet selected. No target-repository changes authorized by this plan.

**Baseline:** Accepted M1–M3 and M5; provisionally accepted M4. [M4 runtime follow-up](../validation/m4-codex-runtime-followup.md) remains open. No release tag is implied.

## Purpose

Evaluate whether the portable standard and five optional procedures help with **one real, bounded engineering task** in an existing repository without adding disproportionate ceremony, duplicating existing policy, or confusing instructions with permissions. This is an adoption experiment, not an automation rollout.

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

## Deliverables

A target inventory, approved adoption diff, one-task execution report, measured evaluation, rollback/removal notes, and M6 acceptance recommendation. Track unknowns and any blocked action explicitly.
