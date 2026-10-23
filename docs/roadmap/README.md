# Roadmap and future capability proposals

The maintained human-readable roadmap is the [Project Accomplishments and Future Roadmap](../PROJECT_ACCOMPLISHMENTS_AND_ROADMAP.md).

For detailed Phase D/E implementation choices, selection criteria, self-improvement/RL research, and a bounded POC charter, see the [Phase D/E research dossier](../research/phase-d-e/README.md).

## Fresh-session handoff

**[Cross-assistant handoff and reusable prompts](SESSION_HANDOFF.md)** is the canonical short-form entry point for fresh ChatGPT, Claude chat and cloud Claude Code sessions. It identifies the working branch, live PR/issue verification, current execution scope, evidence labels, and branch/publication risks. The document is on the research branch pending PR #11, not necessarily on `main`.

## Near-term reference milestone

**[M10 — Claude + GitHub reference implementation](M10_EXECUTION_PLAN.md)** is the recommended next **evaluation and implementation milestone**, with an explicit [current approved-tooling profile](APPROVED_TOOLING_PROFILE.md), [native capability audit](../evaluations/M10_CLAUDE_NATIVE_AUDIT.md), [paired pilot protocol](../evaluations/M10_PILOT_EVALUATION_PROTOCOL.md), [run log](../evaluations/M10_RUN_LOG.md) (primary evidence record, empty) and [proposed ADR-007](../decisions/ADR-007-CLAUDE-GITHUB-FIRST.md). It does **not** discard the broader provider-neutral Phase D/E design. No M10 runtime tests have been performed.

## Proposed sequence

| Phase | Focus | Status |
| --- | --- | --- |
| M10 (near-term, cross-cutting) | Claude-native + GitHub reference workflow, evaluation and M6/M8 follow-up | **Proposed / documentation prepared; not executed** |
| v1.0 | Release-readiness review and bounded claims | Proposed; no release/tag |
| v1.1 | Optional adoption tooling, diagnostics, skill exposure | Proposed |
| v1.2 | CI, evidence capture, compatibility tests | Proposed |
| v2.0 | Optional runtime coordinator, routing, state, policy gates | **Research preserved; implementation deferred pending M10 evidence** |
| Beyond | Cross-repository knowledge, evaluation, hybrid execution, organizational governance | Exploratory |

These are **not approved milestones, funding commitments, or release dates**. Deferred M4, M6, and M8 evidence remains tracked in existing milestone records.

For the origin of architecture choices see [decisions](../decisions/README.md); for evidence see [evaluations](../evaluations/README.md); for source preservation see [research](../research/README.md).
