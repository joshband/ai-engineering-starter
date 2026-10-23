# Phase D/E — Execution Coordinator and Learning Systems Research

**As of:** 2026-10-22 · **State:** Research proposal, not implementation or approved milestones  
**Initial preference:** Claude-first, **provider-independent by architecture**.  
**Scope:** Options, decisions, risks, source register, and bounded proof-of-concept specification for the [project roadmap](../../PROJECT_ACCOMPLISHMENTS_AND_ROADMAP.md).

## Decision summary

Build an **optional coordinator above the portable M1–M9 foundation**, not a replacement engineering standard or a parallel agent platform.

**Recommended first prototype:** a locally controlled, single-repository coordinator using **Claude Agent SDK** as first harness integration; common typed `AgentAdapter` interface with a Codex adapter acceptance test before treating the platform as portable. Use scoped task authority, independent worker restrictions, explicit spending/iteration limits, SQLite journal + effect ledger, deterministic checks, and human review. Keep raw external publications disabled until separately authorized.

**Learning strategy:** begin on day one with evaluation and outcome data. Allow a future *reviewed* improvement cycle for prompts, skills, task decomposition, tool profiles, and model routing. Explore online learning (e.g., contextual bandits) only after a sufficiently diverse task dataset and defensible rewards. Defer actual RL policy/model training and unrestricted self-modification.

### Read the dossier in order

1. [Technology and provider assessment](TECHNOLOGY_OPTIONS.md) — Claude-first vs Codex, other runtimes, orchestration, storage, gateways.
2. [Priority and selection matrix](CAPABILITY_PRIORITIES.md) — recommended P0/P1/P2/P3 features and dependencies.
3. [Reference architecture](REFERENCE_ARCHITECTURE.md) — interfaces, enforcement boundaries, recovery, lifecycle, evidence.
4. [Proof-of-concept plan](POC_EXECUTION_PLAN.md) — acceptance tests, experiments, sequencing, failure injection.
5. [Self-improvement and reinforcement-learning track](LEARNING_SYSTEMS.md) — reward design, bandits, offline RL, evaluation and promotion gates.
6. [Phase E future options](PHASE_E_OPTIONS.md) — longer-term decision triggers.
7. [Primary-source register](SOURCE_REGISTER.md) — official documentation, observation boundaries, refresh questions.

## Selection rationale

The Claude Agent SDK embeds Claude Code capabilities (built-in tools, hooks, permissions, sessions, skills) in a programmable process. Its documentation also warns that third-party developers cannot assume entitlement to users' claude.ai logins or rate limits; test authorized authentication and charges for this use case. Source S01, S02. Codex exposes a programmatic SDK with thread continuation and resume; source S03. A **common coordinator contract** lets those differences remain inside harness adapters.

No model, framework, or provider is selected as the sole architecture. Model portability and **harness portability** are distinct: changing an API base URL does not reproduce Claude Code's tooling, skill-loading, or permission semantics.

## Critical boundaries

- Existing [STD-01–STD-16](../../../core/standards/ENGINEERING_STANDARD.md) remain canonical. This dossier introduces no new normative policy.
- Claims in this dossier are from provider documents, *not* local integration results. SDK behavior, costs, permissions, and availability need live verification.
- A prompt, sandbox label, framework checkpoint, or passing JSON schema is not independent permission enforcement.
- Start with a reversible fixture repository, no production secrets, one executor, no merges or deployments.
- Preserve source provenance and experiment outcomes per [documentation retention](../../DOCUMENTATION_RETENTION.md).

**Decision requested for the next stage:** approve the POC *scope* and the initial Claude adapter spike, not an unrestricted implementation or release.
