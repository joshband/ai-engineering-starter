# Changelog

## 1.0.0 candidate — 2026-10-22

- Proposed first release of the repository-centered engineering standard, risk/autonomy taxonomy, contracts, workflows, adoption guidance, M2 structured control interface and deterministic fixtures, optional Claude Code and Codex instruction adapters, five optional procedures, and existing-repository decision/navigation guides. M1–M3, M5, M7, and M9 were accepted and merged; M4 was provisionally accepted and merged. PR #8 corrected the M5 validator status message after acceptance.
- Release scope is the maintained documentation and the documented standard-library structural validator at the eventual tagged revision. It does not promise automatic agent behavior, authorization enforcement, universal adapter compatibility, or a functioning agent security platform. The canonical M1 standard owns policy; M2 catalog/schema checks do not grant execution authority.
- Deferred evidence: M4 live Codex instruction discovery is [open](validation/m4-codex-runtime-followup.md); the M6 Copy That pilot has [partial verification and deferred adoption acceptance](docs/M6_PILOT_PLAN.md); M8 [runtime validation planning](https://github.com/joshband/ai-engineering-starter/blob/m8/runtime-validation-plan/docs/M8_RUNTIME_VALIDATION_PLAN.md) has not been executed. One bounded Claude Code discovery observation is documented for M3; it is not a general runtime guarantee.
- Candidate preparation only. Human review of scope, limitations, final validation evidence, and the exact release revision is required before a separate decision to tag or publish. No tag or release has been created.

## 0.5.0 candidate — 2026-10-22

- Added five optional portable engineering procedures for task intake, change verification, review and acceptance, safe handoff, and exception review.
- Skills reference M1 policy and M2 schemas; neither adapter auto-discovers or auto-invokes these procedures. No new authority, runtime permissions, enforcement, or M6 pilot.
- Added six deterministic skill-library regression cases (inventory, relative links, opt-in boundaries, Quick, Profile H exceptions, and acceptance separation).
- Verified from the exact PR tree: `python3 validation/validate.py` passed (16 policies, 16 controls, 9 valid/13 intentionally invalid fixtures); `python3 -m unittest discover -s validation/tests -v` passed (19 tests: 13 M1–M4, 6 M5); `git diff main...HEAD --check` passed. Strengthened the six M5 tests for exact inventory, canonical links, conditional exception schema behavior, and separate completion states.
- Clarified manual access to portable skill procedures and reconciled M4/M5 status reporting. Live native skill discovery and invocation remain Unverified; M4 Codex runtime follow-up remains open. M5 execution Completed; human acceptance Accepted and squash-merged in PR #5 (commit bd3a91be3974bca758ac9b2943b002c1dc24ce7e) on 2026-10-22. No tag or release.


## 0.4.0 candidate — 2026-10-22

- Added a root Codex `AGENTS.md` that navigates to the accepted M1 standard, M2 controls, contracts, and workflows without copying policy or configuring permissions.
- Added Codex adoption, configuration-boundary, control mapping, and Claude/Codex parity guidance.
- Added deterministic adapter tests and M4 acceptance checks; actual Codex CLI discovery remains Unverified in this environment.
- M4 provisionally accepted for architecture and structural checks and squash-merged in PR #4 (commit b460c1dddfe48751eced8f50e3a5bcdc6a086321). Live Codex instruction discovery deferred because the CLI was unavailable and the user's Codex cloud UI could not load environments (2026-10-22). Tracked in validation/m4-codex-runtime-followup.md. This is not evidence of an adapter defect. No tag or release.

## 0.3.0 candidate — 2026-10-22

- Added a root Claude Code instruction entry point importing the accepted M1 standard and taxonomy, with direct navigation to M2 controls and the contracts.
- Added incremental adoption, control mapping, permission-boundary, validation, and removal guidance.
- Added structural tests for discovery, contract cases, escalation, and operation without optional Claude Code runtime features.
- M3 accepted and squash-merged in PR #3 (commit 291e2d0bff2fb99cee784a599630a9721701d762). Bounded Claude Code cloud-session smoke test confirmed root instruction discovery and both M1 imports in `/context`; permission behavior, prompt adherence, and cross-environment compatibility remain Unverified. No hooks, project permissions, release, or later milestones.

## 0.2.0 candidate — 2026-10-22

- Added versioned structured controls for STD-01 through STD-16 and optional Task, Handoff, Completion, and Exception record schemas.
- Extended the original M1 validation entry point with standard-library catalog, schema-subset, drift, and fixture checks.
- Added 9 positive and 13 negative fixtures, traceability, and conditional boundary regression tests.
- M2 accepted following architecture/policy review and squash-merged in PR #2 (commit dcf7e41ce1553dd5ea4138c99c0bae46495a7db2). No runtime authorization, adapter, service, release, or tag implemented.

## 0.1.0 candidate — 2026-10-22

- Implemented M1 portable engineering policy, classifications, contracts, lifecycle, workflows, and minimal templates.
- Added incremental adoption and security-boundary guidance.
- Added a dependency-free structural checker and acceptance matrix.
- Clarified mandatory review/expiration triggers for material Profile H exceptions (STD-16); made required, conditional, and invariant contract semantics explicit without adding process for low-risk work.
- At candidate creation, human architecture/policy acceptance was pending. M1 was later accepted by the maintainer and merged in PR #1 (merge commit b21ef5e86f41d5715bd1eb727be58076e45a1e56). No release tag was created.
