# Phase E — future capabilities and option triggers

**Status:** Exploratory, explicitly not approved. The goal is to prevent premature investment while preserving credible options.

## 1. Cross-repository engineering knowledge

**Opportunity:** Query maintained engineering decisions, tests, and source patterns across selected permitted repositories, with each answer traceable to an owner, repository, path, revision, and visibility policy.

**Choose when:** repeated cross-repo work requires the same knowledge; repository inventory and ACL tests demonstrate value.

**Risks:** stale embeddings, authorization leakage, embedding source content in third-party stores, copying superseded guidance, cross-client confidentiality.

**First experiment:** read-only, owner-approved retrieval over two low-sensitivity repositories; require citations and per-user access filters at query and retrieval stages. A missing permission must produce no result.

## 2. Agent/model evaluation and improvement

**Opportunity:** Compare Claude, Codex and local models on repeatable task fixtures, accepted change quality, safety and human effort.

**Choose when:** the first 10–20 baseline tasks have established instrumentation and enough varied tasks can support evaluation.

**First experiment:** evaluate a proposed prompt or verification skill revision against an unchanged baseline; hold out a representative set of tasks; track reviews and costs. See [learning systems](LEARNING_SYSTEMS.md).

**Extension:** adaptive selection or contextual bandits only after statistically defensible outcomes. Separate model-weight reinforcement learning as a research program; don't let self-improvement modify the controls it must obey.

## 3. Hybrid local/cloud execution

**Opportunity:** Route approved tasks among Claude, Codex and LM Studio-hosted local models based on quality, sensitivity, observed memory/latency and budget.

**Choose when:** representative local tasks show acceptable correctness and permission boundaries in the actual environment.

**First experiment:** compare read-only code explanation or test suggestion on a fixed fixture against cloud agents. **Do not equate a compatible inference API with a complete coding-agent runtime.**

## 4. Reviewed workflow improvement

**Opportunity:** Agent proposes changes to skill sequences, prompts, task classification and verification templates based on failure taxonomies.

**Choose when:** evidence records are stable; a real repetitive failure is documented.

**First experiment:** generate a proposed skill diff, benchmark it, and require human approval to promote. Record rollback and superseding results.

## 5. Organization-level governance

**Opportunity:** Versioned team policy distribution, centrally approved exception processes, and audit evidence linked to native repo instruction entry points.

**Choose when:** multiple independent teams actually need centralized management and have accountable owners.

**First experiment:** two teams, limited policy subset, manually controlled distribution and conflict reporting. Do not centralize secrets or grant repository-wide execution authority.

## 6. More capable multi-agent execution

**Opportunity:** Parallel non-conflicting tasks, specialty reviewers, durable multi-worker jobs, and isolated orchestration.

**Choose when:** the sequential design's accepted-task throughput and latency are demonstrably limiting.

**First experiment:** parallel **read-only** review agents, then isolated nonoverlapping worktrees after proving resource ceilings and merge-conflict reconciliation.

## Decision table

| Phase E option | Near-term choice | Prerequisite | Stop signal |
| --- | --- | --- | --- |
| Evaluations and reviewed improvements | **Begin instrumentation now** | Task IDs, revisions, evidence | Reward gaming or safety regression |
| Cross-repository knowledge | Defer | Verified permissions/provenance | ACL leakage |
| Hybrid local/cloud | Targeted experiment | Local model quality baseline | Unapproved exposure or unacceptable reliability |
| Contextual-bandit routing | Research later | Adequate unbiased outcome data | Poor confidence or costs |
| Policy/model RL | Research only | Trustworthy reward, sandbox and cost feasibility | OOD regression or reward hacking |
| Parallel agent workers | Defer | Sequential recovery and isolation | Collisions/unbounded resource use |
| Organization governance | Demand-driven | Multiple accountable teams | Policy-owner ambiguity |

## What this phase is NOT

No unattended model retraining, hidden self-modification, implicit authority escalation, subscription-limit bypass, or deployment autonomy. No guarantee that an external benchmark predicts your project's outcomes.

For source context see [source register](SOURCE_REGISTER.md); for the implementation-neutral roadmap see [project report](../../PROJECT_ACCOMPLISHMENTS_AND_ROADMAP.md).
