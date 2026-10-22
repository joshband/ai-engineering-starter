# AI-Native Software Engineering Starter Kit

M1 — Portable Engineering Core: Accepted (PR #1). M2 — Shared Controls and Fixtures: Accepted (PR #2). M3 — Claude Code Adapter: Accepted (PR #3). M4 — OpenAI Codex Adapter: provisionally accepted and merged (PR #4); live instruction discovery remains [deferred](validation/m4-codex-runtime-followup.md). M5 reusable engineering skills: Accepted and squash-merged in PR #5 (2026-10-22). M6 pilot: partial verification, adoption deferred. M7 adoption decision kit: Accepted and merged in PR #6. M8 runtime validation: planned but deferred. M9 usability documentation: candidate under review. No release tag published.

A documentation and contract baseline for individual developers, technical leads, and small teams using AI coding agents in new or existing repositories. It helps define bounded work, select proportionate workflows, verify changes, review outcomes, and preserve engineering knowledge.

Standardize engineering behavior, authority, verification, and knowledge rather than AI products. Models generate outputs; agents combine models with tools; tools perform operations; workflows organize work; runtimes determine execution guarantees. These are separate concerns.

This starter kit is not a functioning agent security platform. M2 supplies a structured catalog, optional contract schemas, and deterministic validation fixtures. M3 adds a [Claude Code entry point](CLAUDE.md); M4 adds a [Codex entry point](AGENTS.md) and [adapter guide](adapters/codex/README.md). It supplies no automated enforcement, routing, hooks, orchestration, CI/CD, or deployment. No external service or model provider is required. A bounded M3 cloud session confirmed Claude instruction discovery; Codex CLI loading remains Unverified here.

For the shortest route through the kit, use [Start here](docs/START_HERE.md); for milestone status and evidence limitations, see the [capability map](docs/CAPABILITY_STATUS.md).

For a human-readable account of what was built, outstanding validation, release readiness, and proposed v1.1–v2.0+ capabilities, see the [project accomplishments and future roadmap](docs/PROJECT_ACCOMPLISHMENTS_AND_ROADMAP.md). The [research and evidence index](docs/research/README.md) and [documentation retention guidance](docs/DOCUMENTATION_RETENTION.md) preserve supporting history without creating competing policy.

## Individual quick start

1. Read the [standard](core/standards/ENGINEERING_STANDARD.md) and [classifications](core/standards/AUTONOMY_AND_RISK.md).
2. Inventory existing instructions. Follow [adoption](docs/ADOPTION.md) to merge the [AGENTS entry point](core/templates/AGENTS.md) and fill the [project profile](core/templates/PROJECT_PROFILE.md).
3. Choose a [workflow](core/workflows/PROFILES.md). For trivial local work, state the outcome and boundary, make the edit, inspect it, and report the check. No formal task document is needed.
4. For material work, use the [task template](core/templates/TASK.md), verify the result, and review it. Completed is distinct from Accepted.

## Read and navigate

MUST is mandatory when its conditions apply; SHOULD is the default recommendation with justified exceptions; MAY is optional. SHOULD is not MUST. The standard is the sole owner of STD requirements. Other files reference IDs; templates collect evidence rather than create additional policy.

| Location | Owns |
| --- | --- |
| [core/standards](core/standards/ENGINEERING_STANDARD.md) | Canonical policy; taxonomy in AUTONOMY_AND_RISK |
| [core/contracts](core/contracts/TASK_CONTRACT.md) | Task, handoff, completion, exception semantics |
| [core/workflows](core/workflows/LIFECYCLE.md) | Lifecycle and workflow selection |
| [core/templates](core/templates/PROJECT_PROFILE.md) | Optional working forms and project instructions |
| [docs](docs/ADOPTION.md) | Adoption and security interpretation |
| [validation](validation/acceptance-matrix.md) | Checks, limits, and review evidence |
| [core/controls](core/controls/README.md) | M2 structured representations and schema conventions; M1 policy remains authoritative |
| [adapters/claude-code](adapters/claude-code/README.md) | M3 instruction discovery and adoption; no permission settings or hooks |
| [adapters/codex](adapters/codex/README.md) | M4 instruction routing, adoption, and cross-adapter comparison; no runtime settings |
| [skills](skills/README.md) | M5 optional task, verification, review, handoff, and exception procedures; no automatic invocation |
| [docs/adoption-decision](docs/adoption-decision/README.md) | M7 manual existing-repository inventory, adoption/skip decisions, example, and reversal |

Project profiles own technical details. Both adapters expose the same standard without redefining it. Applicable organizational governance remains externally authoritative. Repository records are authoritative engineering context; agent memory is not a substitute.

## Architecture decisions

| Decision | M1 interpretation |
| --- | --- |
| ADR-001 | Repository-centered contracts and maintained knowledge |
| ADR-002 | Risk determines authority, isolation, approvals, and checks |
| ADR-003 | Explicit workload selection: Fast for simple work, Standard for routine implementation, Deep for uncertainty, Local when suitable for approved data/runtime constraints; labels imply no vendor or automatic routing |
| ADR-004 | Plain Markdown shared core; agent-specific instruction entry points supplied by M3 and M4 |
| ADR-005 | Commercial and local inference are valid; no required gateway |
| ADR-006 | Durable and multi-agent infrastructure deferred until justified |

## Validation and contribution

Run `python3 validation/validate.py` from this directory for M1 and M2 checks, or `python3 validation/validate_controls.py` for M2 alone (Python standard library only). Adoption itself does not require Python or structured task files. See the [acceptance matrix](validation/acceptance-matrix.md) and [control traceability](validation/control-traceability.md) for exact check scope and editorial review still needed.

Propose focused changes with rationale, affected policy IDs, verification evidence, and migration implications. Change canonical definitions at their owning file and update references together. No PR or separate reviewer is universally required for adopting projects; follow their governance. M1–M3 and M5 were accepted and merged; M4 is provisionally accepted subject to a tracked live Codex discovery follow-up. M6 CT-M6-01 has a documented partial pilot outcome with target verification deferred. M7's optional adoption decision kit was accepted and merged in PR #6. M8 runtime tests remain deferred; M9 documentation is a candidate under review. No release or tag is implied. Structured validation remains limited to the documented checks.

## M6 pilot adoption

M6 CT-M6-01 in Copy That produced a [partial pilot outcome](docs/M6_PILOT_PLAN.md): local documentation checks reportedly passed, but the target's full verification was blocked before tests. Adoption acceptance and publication remain deferred. M7's [manual decision kit](docs/adoption-decision/README.md) is accepted and merged. [M8 runtime validation planning](https://github.com/joshband/ai-engineering-starter/blob/m8/runtime-validation-plan/docs/M8_RUNTIME_VALIDATION_PLAN.md) is deferred; [M9 usability consolidation](docs/M9_USABILITY_PLAN.md) is a documentation-only candidate.

## Security limitations

Instructions, schemas, and passing validators do not enforce permissions or isolate execution. Review [security boundaries](docs/SECURITY_BOUNDARIES.md) before granting tools, credentials, network access, or consequential authority. Neither local inference nor a sandbox label proves isolation. Neither adapter installs permission configuration; observe each runtime before relying on its behavior.
