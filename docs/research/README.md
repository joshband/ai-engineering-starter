# Research and supporting evidence index

**Status:** Inventory and retention index, 2026-10-22. This index is descriptive, not normative policy. See [documentation retention](../DOCUMENTATION_RETENTION.md).

## Why this exists

Keep the original reasoning and evidence behind the [starter kit](../../README.md) discoverable without duplicating or rewriting the [canonical engineering standard](../../core/standards/ENGINEERING_STANDARD.md). Preserve original sources when permitted; link to evidence in its existing authoritative location. An inferred reconstruction is **not** an original research document.

## Verified repository-held material

| Subject | Existing source | Kind | Evidence status |
| --- | --- | --- | --- |
| Core architecture choices ADR-001–ADR-006 | [Root README — Architecture decisions](../../README.md#architecture-decisions) | Summarized decisions | Present; fuller original deliberation not located in repository inventory |
| Canonical standards, risk and autonomy | [Engineering standard](../../core/standards/ENGINEERING_STANDARD.md), [taxonomy](../../core/standards/AUTONOMY_AND_RISK.md) | Implemented authoritative artifacts | Present; not historical research |
| Shared control semantics and validation scope | [M2 controls](../../core/controls/README.md), [traceability](../../validation/control-traceability.md), [acceptance matrix](../../validation/acceptance-matrix.md) | Implementation and evidence | Present |
| Claude Code instruction discovery | [Claude adapter](../../adapters/claude-code/README.md), [changelog](../../CHANGELOG.md) | Adapter and bounded observation | Present; not universal runtime proof |
| Codex instruction-discovery gap | [Codex adapter](../../adapters/codex/README.md), [runtime follow-up](../../validation/m4-codex-runtime-followup.md) | Adapter and deferred test record | Present; native discovery unverified |
| Optional engineering skills | [Skills index](../../skills/README.md) | Implemented optional procedures | Present; automatic invocation not implemented |
| Copy That adoption experiment | [M6 pilot plan and results](../M6_PILOT_PLAN.md) | Pilot record | Partial target verification; no accepted target publication |
| Adoption decision and reversal | [M7 planning](../M7_CANDIDATE_PLAN.md), [decision kit](../adoption-decision/README.md) | Plan and implemented guide | Present |
| Usability and evidence taxonomy | [M9 plan](../M9_USABILITY_PLAN.md), [capability status](../CAPABILITY_STATUS.md) | Plan and status | Present; some historical candidate-era labels |
| Runtime validation proposal | [M8 planning branch](https://github.com/joshband/ai-engineering-starter/blob/m8/runtime-validation-plan/docs/M8_RUNTIME_VALIDATION_PLAN.md) | External-to-main branch plan | Located on branch; not merged or executed |
| Milestone implementation trail | [Changelog](../../CHANGELOG.md), [GitHub pull requests](https://github.com/joshband/ai-engineering-starter/pulls?q=is%3Apr) | History and review provenance | Present; use PR revisions for exact evidence |
| Project overview and proposed future roadmap | [Accomplishments and roadmap](../PROJECT_ACCOMPLISHMENTS_AND_ROADMAP.md) | New retrospective and proposal | Draft PR #10; not a historical original |

## Research themes for source recovery — NOT retained original reports

The following subjects arose as potential future capabilities, but **no corresponding full original research documents were identified in the repository inventory**. Do not treat these headings as evidence that research has been recovered:

- Model selection, cost optimization, usage limits, and routing.
- Local versus cloud inference and authorized data boundaries.
- Agent runtime permissions, isolation, hooks, and trust models.
- Multi-agent orchestration, durable state, and recovery.
- Developer workflow and agent product comparisons beyond the retained adapter documentation.
- Original cross-provider benchmarks, notes, or external citations, if any.

To import such material later, locate its original file or source first; check ownership, licensing, secrets, confidentiality, and relevance; preserve the original with date and provenance; add a concise navigation summary; and update this index. Do not manufacture citations or imply the original is complete when only an excerpt is available.

## Current implementation profile (2026-10-23)

- [Claude + GitHub approved-tooling profile](../roadmap/APPROVED_TOOLING_PROFILE.md), [M10 execution plan](../roadmap/M10_EXECUTION_PLAN.md), [proposed architecture decision](../decisions/ADR-007-CLAUDE-GITHUB-FIRST.md), [native capability audit](../evaluations/M10_CLAUDE_NATIVE_AUDIT.md) and [pilot evaluation](../evaluations/M10_PILOT_EVALUATION_PROTOCOL.md). **Implementation plans, not executed experiments.** They preserve prior multi-provider research; alternatives are inactive in this working environment.

## New researched topics (2026-10-22)

- [Phase D/E: Claude-first provider-neutral execution coordinator, durable tasks, evaluation-driven self-improvement, adaptive routing and reinforcement-learning options](phase-d-e/README.md) — research dossier, sourced proposals, comparison matrix and bounded proof-of-concept; **not implemented**.

## Related indexes

- [Decisions and trade-offs](../decisions/README.md)
- [Evaluations and experiments](../evaluations/README.md)
- [Roadmap](../roadmap/README.md)
- [Retention rules](../DOCUMENTATION_RETENTION.md)
