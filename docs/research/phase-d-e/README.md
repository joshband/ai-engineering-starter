# Phase D/E — Execution Coordinator and Learning Systems Research

**As of:** 2026-10-22 · **State:** Research proposal, not implementation or approved milestones\
**Initial workflow preference:** Claude-first, **provider-independent by architecture**. **Harness selection remains open** among Claude Agent SDK, Pi and OpenCode; coordinator selection remains open between a lightweight state machine and OpenClaw.\
**Scope:** Options, decisions, risks, source register, and bounded proof-of-concept specification for the [project roadmap](../../PROJECT_ACCOMPLISHMENTS_AND_ROADMAP.md).

## Current implementation overlay — M10 (2026-10-23)

**The full technology research below remains retained for future unconstrained environments.** In the user's current working environment **Claude and GitHub are the only approved tools**. For the next implementation stage, the active track is **[M10 Claude + GitHub reference workflow](../../roadmap/M10_EXECUTION_PLAN.md)**, governed by the [approved-tooling profile](../../roadmap/APPROVED_TOOLING_PROFILE.md) and [proposed ADR-007](../../decisions/ADR-007-CLAUDE-GITHUB-FIRST.md). Native Claude Code first; GitHub as approved review/evidence control plane; run the [native audit](../../evaluations/M10_CLAUDE_NATIVE_AUDIT.md) and [paired evaluation](../../evaluations/M10_PILOT_EVALUATION_PROTOCOL.md) before choosing SDK or coordinator.

**Research vs implementation:** The harness comparison and custom-coordinator proposal below are **future optional research paths**, not a requirement or authorized execution for M10. Pi, OpenCode, Codex runtime, OpenClaw, external gateways and workflow engines are **not being enabled**. No comparison results, runtime guarantees, or M10 pilot acceptance are claimed. **No coordinator may be the correct result** if native Claude meets acceptance gates.

## Original broad research decision summary

Build an **optional coordinator above the portable M1–M9 foundation**, not a replacement engineering standard or a parallel agent platform.

**Recommended first experiment:** a locally controlled, single-repository **head-to-head harness spike** with Claude Agent SDK, Pi and OpenCode using Claude where permitted, plus a Codex SDK portability baseline. After measuring capabilities and safety, choose a harness for the bounded coordinator POC. Compare **OpenClaw vs lightweight coordinator** separately. Preserve a common typed `AgentAdapter` contract. Use scoped task authority, independent worker restrictions, explicit spending/iteration limits, SQLite journal + effect ledger, deterministic checks, and human review. Keep raw external publications disabled until separately authorized.

**Learning strategy:** begin on day one with evaluation and outcome data. Allow a future *reviewed* improvement cycle for prompts, skills, task decomposition, tool profiles, and model routing. Explore online learning (e.g., contextual bandits) only after a sufficiently diverse task dataset and defensible rewards. Defer actual RL policy/model training and unrestricted self-modification.

### Read the dossier in order

1. [Technology and provider assessment](TECHNOLOGY_OPTIONS.md) — Claude-first vs Codex, other runtimes, orchestration, storage, gateways.
2. [Expanded ecosystem review](EXPANDED_ECOSYSTEM_REVIEW.md) — Pi, OpenCode, OpenClaw, OpenHands, Goose, and layered selection.
3. [Claude native feature parity](CLAUDE_NATIVE_CAPABILITIES.md) — hooks, skills, plugins, subagents, MCP, SDK differences.
4. [Priority and selection matrix](CAPABILITY_PRIORITIES.md) — recommended P0/P1/P2/P3 features and dependencies.
5. [Reference architecture](REFERENCE_ARCHITECTURE.md) — interfaces, enforcement boundaries, recovery, lifecycle, evidence.
6. [Proof-of-concept plan](POC_EXECUTION_PLAN.md) — acceptance tests, experiments, sequencing, failure injection.
7. [Self-improvement and reinforcement-learning track](LEARNING_SYSTEMS.md) — reward design, bandits, offline RL, evaluation and promotion gates.
8. [Phase E future options](PHASE_E_OPTIONS.md) — longer-term decision triggers.
9. [Primary-source register](SOURCE_REGISTER.md) — official documentation, observation boundaries, refresh questions.

## Selection rationale

The Claude Agent SDK embeds Claude Code capabilities (built-in tools, hooks, permissions, sessions, skills) in a programmable process. Its documentation also warns that third-party developers cannot assume entitlement to users' claude.ai logins or rate limits; test authorized authentication and charges for this use case. Source S01, S02. Codex exposes a programmatic SDK with thread continuation and resume; source S03. A **common coordinator contract** lets those differences remain inside harness adapters.

No model, framework, or provider is selected as the sole architecture. Model portability and **harness portability** are distinct: changing an API base URL does not reproduce Claude Code's tooling, skill-loading, or permission semantics.

## Critical boundaries

- Existing [STD-01–STD-16](../../../core/standards/ENGINEERING_STANDARD.md) remain canonical. This dossier introduces no new normative policy.
- Claims in this dossier are from provider documents, *not* local integration results. SDK behavior, costs, permissions, and availability need live verification.
- A prompt, sandbox label, framework checkpoint, or passing JSON schema is not independent permission enforcement.
- Start with a reversible fixture repository, no production secrets, one executor, no merges or deployments.
- Preserve source provenance and experiment outcomes per [documentation retention](../../DOCUMENTATION_RETENTION.md).

**Deferred broad-research decision:** a later environment may approve comparison spikes for Pi/OpenCode/OpenClaw. The current path is the narrower M10 native-Claude/GitHub evaluation, which **does not** require or authorize third-party harness execution. Do not approve a production coordinator, unrestricted implementation, or release from this research alone.
