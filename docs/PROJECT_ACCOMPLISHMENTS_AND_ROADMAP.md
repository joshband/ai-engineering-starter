# AI-Native Software Engineering Starter Kit — Accomplishments and Future Roadmap

**Report date:** 2026-10-22  
**Audience:** Maintainers, engineering leaders, contributors, and prospective adopters  
**Document type:** Descriptive project report and **proposed** roadmap, not a new policy, approved scope of work, or release commitment.

> **In plain language:** This effort created a reusable set of engineering rules, workflows, templates, agent-specific instruction guides, and checks to help people use AI coding assistants responsibly across projects. The foundation is implemented, but some real-environment testing and the first versioned release remain outstanding.

## Executive summary

The [AI-Native Software Engineering Starter Kit](../README.md) is a portable engineering foundation, not a new AI coding model or an autonomous execution platform. It helps teams define what an agent may do, scale process to risk, preserve decisions, verify actual changes, and distinguish work completed from work accepted, merged, or released.

The guiding architecture is **one authoritative engineering standard**, with optional machine-readable records, workflow guidance, reusable procedures, and thin adapters for individual agent products. Existing repositories can adopt none, some, or all of the useful material without overwriting their established governance.

As of this report, **M1, M2, M3, M5, M7, and M9 are accepted and merged**. **M4 is provisionally accepted and merged**, with live Codex instruction discovery unverified. **M6** is a partially verified pilot awaiting target verification and acceptance. **M8** is a runtime-validation plan on a separate branch; execution is deferred. The follow-up maintenance correction to the validator's stale M5 message was merged in [PR #8](https://github.com/joshband/ai-engineering-starter/pull/8). No v1.0 release or tag has been published.

The most recent maintenance closeout reported 24/24 unit tests passing, successful structural validation, and a clean diff whitespace check. These are **structural** checks, not evidence of runtime enforcement or universal agent compatibility.

## 1. What was created

### 1.1 Portable engineering standard (M1)

The [canonical standard](../core/standards/ENGINEERING_STANDARD.md) defines 16 requirements and expectations (STD-01 through STD-16) covering:

- Authorized task scope and consequential-action approval.
- Outcomes, acceptance criteria, recoverability, and controlled changes.
- Honest verification evidence and accountable review.
- Data restrictions, credentials, tool trust, and execution isolation.
- Cost limits, consequential retries, maintained engineering knowledge, operational evidence, and exceptions.

Only the M1 standard owns these normative STD definitions. Adapters, templates, and catalogs reference them instead of creating competing policy copies. The [risk/autonomy taxonomy](../core/standards/AUTONOMY_AND_RISK.md) and [workflow profiles](../core/workflows/PROFILES.md) scale guidance to consequences and uncertainty.

**Practical value:** A team does not need to rewrite its engineering expectations every time it changes AI assistants.

### 1.2 Proportionate workflows and contracts (M1)

The four workflow profiles are:

| Profile | Intended use | Typical example |
| --- | --- | --- |
| Quick | Small, low-risk local changes | Correcting a typo or comment |
| Standard | Routine material engineering changes | Implementing an endpoint with targeted tests |
| Structured | Uncertain or cross-cutting work | Refactoring a multi-service integration |
| Controlled | High-consequence actions | A production migration requiring actual approvals and safeguards |

The [task](../core/contracts/TASK_CONTRACT.md), [handoff](../core/contracts/HANDOFF_CONTRACT.md), [completion](../core/contracts/COMPLETION_CONTRACT.md), and [exception](../core/contracts/EXCEPTION_CONTRACT.md) contracts describe information needed for responsible engineering. The [templates](../core/templates/PROJECT_PROFILE.md) are optional aids; **Quick does not require a formal task file, branch, PR, or separate planning document by default**.

The lifecycle keeps these decisions separate: **implementation Completed; verification Passed/Failed/Unverified; human acceptance; merge; release**. Finishing a task does not automatically authorize publication.

### 1.3 Shared controls and deterministic fixtures (M2)

The [M2 control interface](../core/controls/README.md) provides a machine-readable index of the 16 standards, four optional record schemas, and deterministic fixtures. The Python standard-library validation tools check supported structural rules, catalog invariants, references, and expected positive/negative cases.

**Practical value:** Future tooling can consume consistent record shapes and detect documentation drift.

**Limit:** A valid record does not prove its evidence is true, its approver is authorized, or an agent's actions were restricted.

### 1.4 Claude Code and Codex adapters (M3–M4)

The [Claude Code adapter](../adapters/claude-code/README.md) uses a root `CLAUDE.md` entry point and canonical imports/navigation. A bounded cloud session observed root instruction discovery and imports. That observation does not establish universal adherence or permission enforcement.

The [Codex adapter](../adapters/codex/README.md) uses a root `AGENTS.md` entry point with links to maintained guidance. Its structural checks passed, but live native discovery remains [deferred](../validation/m4-codex-runtime-followup.md). Ordinary Markdown links should not be mistaken for automatic file imports.

Neither adapter installs security controls, permission configuration, hooks, or a sandbox.

### 1.5 Five optional engineering skills (M5)

The [skill library](../skills/README.md) contains task intake, change verification, review and acceptance, safe handoff, and exception review. They are reusable reference procedures, not automatically invoked capabilities. Each points back to the same authoritative standard.

### 1.6 Existing-repository adoption decision kit (M7)

The [M7 decision kit](adoption-decision/README.md) helps a maintainer inspect existing instructions and governance **read-only**, then select **No adoption**, **Reference only**, or **Selective adoption**. It includes conflict/ownership guidance, an optional example, and reversal instructions.

**Practical value:** Existing repositories can benefit without duplicating or replacing their mature engineering controls.

### 1.7 Reader-focused navigation (M9)

The [Start Here guide](START_HERE.md), [capability/evidence map](CAPABILITY_STATUS.md), and revised [adoption guide](ADOPTION.md) make the starter kit easier to understand. They distinguish structural validation, instruction discovery, observed behavior, and actual enforcement. M9 was accepted and merged in [PR #7](https://github.com/joshband/ai-engineering-starter/pull/7).

A separate [maintenance PR #8](https://github.com/joshband/ai-engineering-starter/pull/8) corrected the validator's stale M5 acceptance message without changing validation logic.

## 2. Current status and remaining commitments

| Workstream | State | Outstanding evidence or decision |
| --- | --- | --- |
| M1 — Portable engineering core | Accepted / merged | None for accepted scope |
| M2 — Shared controls and fixtures | Accepted / merged | None for accepted scope |
| M3 — Claude Code adapter | Accepted / merged | Broader compatibility remains unproven, not a blocker to accepted scope |
| M4 — Codex adapter | Provisionally accepted / merged | Native Codex instruction-discovery test |
| M5 — Engineering skills | Accepted / merged | Automatic invocation was intentionally out of scope |
| M6 — Copy That pilot | Partial verification; acceptance deferred | Configured target checks, review of local diff, adoption decision |
| M7 — Adoption decision kit | Accepted / merged | None for accepted scope |
| M8 — Runtime validation | Plan only; execution deferred | Controlled Claude Code/Codex sessions and evidence matrix |
| M9 — Documentation consolidation | Accepted / merged | None for accepted scope |
| Maintenance — M5 status message | Merged | No outstanding change in this scope |
| First versioned release | Not performed | Release policy, status reconciliation, release notes, tag approval |

### M4 and M8: native runtime evidence

In a working Codex environment, observe which instructions are automatically loaded, verify policy navigation, and record the runtime, version, configuration, and PASS/FAIL/UNVERIFIED results. Extend the bounded evidence approach to Claude Code. Coordinate M4 and M8 to avoid duplicating tests. **Reading an instruction is not proof that an agent follows it, and following it is not proof of independent enforcement.**

M8's planning document currently lives on the separate [runtime-validation branch](https://github.com/joshband/ai-engineering-starter/blob/m8/runtime-validation-plan/docs/M8_RUNTIME_VALIDATION_PLAN.md); it has not been merged as an implemented milestone.

### M6: Copy That pilot closeout

The [pilot plan](M6_PILOT_PLAN.md) records a bounded, local documentation example in [Copy That](https://github.com/joshband/copy-that). Documentation link and whitespace checks were reported passing, but `make verify` stopped before application tests because of shell and environment prerequisites. No target publication was authorized.

When an appropriate target environment is available: inspect the actual local diff, resolve the test environment, run the project's relevant checks, record results, and request a separate maintainer adoption/publication decision. Do not infer that a partial pilot proves successful adoption.

### Release readiness

Before v1.0, reconcile milestone status text in README, the capability map, M9 planning, and other candidate-era documentation **without erasing historical verification records**. Decide whether to publish a GitHub repository tag alone or an additional archive, define versioning and compatibility claims, and prepare concise release notes.

A v1.0 release **could** proceed with explicitly disclosed M4/M6/M8 limitations if the maintainer approves that boundary. It must not claim multi-agent runtime enforcement or completed tests that did not run.

## 3. Deliberately out of scope for the portable foundation

These are **not missing M1 requirements**:

- Automatic model selection or subscription/usage optimization.
- Automatic discovery and invocation of skills.
- Repository installation or generation tools.
- Agent permission enforcement, sandbox configuration, and hooks.
- CI/CD or deployment pipelines.
- Persistent task queues, checkpoints, and orchestration.
- Autonomous multi-agent execution.
- Central telemetry, operational dashboards, or organizational governance services.

These features can build on the standard, but would introduce runtime dependencies, security obligations, and maintenance costs. The existing foundation must remain useful without them.

## 4. Proposed future capability roadmap

The phases below are **options for future approval**, not implemented work, funded commitments, or an automatically scheduled release train.

### Phase A — v1.0: stable portable foundation

**Goal:** Publish an understandable, trustworthy baseline with bounded claims.

**Candidate work:** Reconcile status and changelog, finish or explicitly defer outstanding runtime/pilot evidence, decide packaging and versioning, confirm repository checks, and write release notes.

**Exit evidence:** A reader can determine what is included, how to adopt it, what checks passed, and which runtime behaviors remain unverified. A maintainer explicitly approves the release and tag.

**Indicative effort:** 1–3 focused working days for documentation and release preparation, excluding unavailable runtime environments.

### Phase B — v1.1: easier adoption and developer experience

**Goal:** Reduce repetitive setup without creating a required service.

1. **Optional scaffolding (`starter init`):** Inspect existing repository instructions; preview changes; support dry-run, conflict detection, backup, and reversible removal. Never silently overwrite existing policies.
2. **Environment diagnostics (`starter doctor`):** Check expected instruction paths, links, runtime availability, skill locations, and validation prerequisites. Distinguish configured from actually observed behavior.
3. **Native skill exposure:** Where supported, test platform-specific skill discovery for the five M5 procedures; retain explicit opt-in and authority boundaries.
4. **Version-aware upgrades:** Compare an adopted baseline with new versions, preserve local customization, and report migration conflicts.

**Acceptance experiment:** Try selective adoption in at least two repositories with different instruction structures; remove the pilot material from one and verify existing controls remain intact.

**Indicative effort:** 1–3 weeks for a bounded prototype, not a hardened installer.

### Phase C — v1.2: verification and integration

**Goal:** Collect reliable evidence before automating acceptance.

| Capability | Proposed behavior | Main benefit |
| --- | --- | --- |
| Optional CI checks | Run structural and contract validation in GitHub Actions or an equivalent system | Detect drift |
| Evidence artifacts | Capture actual commands, revisions, results, and limitations | Better reviews |
| Adapter compatibility suite | Test native instruction discovery in named agent versions/surfaces | Detect regressions |
| Policy drift checks | Identify duplicated or conflicting STD definitions | Maintain one source of truth |
| PR review summary | Present scope, checks, unresolved risk, and acceptance state | Faster human decisions |
| Contract interoperability | Stable structured output for external tools | Enable later integrations |

A successful check can support a review decision; it cannot automatically confer human acceptance, merge authorization, or release approval.

**Indicative effort:** 1–3 weeks for initial optional integrations.

### Phase D — v2.0: optional execution coordinator

**Goal:** Explore an independently controlled runtime **above**, not inside, the portable foundation.

Proposed components:

1. **Explicit model routing:** Select approved commercial or local models based on complexity, cost, latency, data rules, and measured results. Begin with inspectable policies; never promise to avoid provider session/weekly limits when reliable usage data is unavailable.
2. **Durable task state:** Preserve task contracts, repository revisions, decisions, checks, and recovery points. Reconcile uncertain external side effects before retrying.
3. **Bounded multi-agent work:** Separate implementation, verification, and review roles. Start with sequential handoffs; add parallelism only after proving isolation, conflict handling, and resource limits.
4. **Independent runtime controls:** Use actual credentials, sandbox/network/filesystem restrictions, approvals, and platform permissions. Markdown instructions are not enforcement.
5. **Cost and stopping controls:** Bound unattended consumption and repeated attempts; use provider telemetry only where available and trustworthy.
6. **Operational evidence:** Record authorized actions, tool calls, outcomes, and approvals with suitable privacy and retention controls.
7. **Optional delivery automation:** Prepare issues, branches, checks, and PRs within approved boundaries; keep consequential merge and deployment gates separate.

**Suggested proof of concept:** One low-risk, reversible workflow with explicit budget, no production credentials, repeatable checks, and human acceptance. Do not generalize a successful prototype to production safety.

**Indicative effort:** 4–8+ weeks for a constrained prototype, excluding production hardening and provider compatibility work.

### Phase E — exploratory longer-term capabilities

Consider only after real usage justifies the additional complexity:

- **Cross-repository engineering knowledge:** Search authorized architecture decisions, code patterns, and accepted changes with provenance and access controls.
- **Agent/model evaluation:** Compare accepted-task quality, cost, regressions, human interventions, and rework.
- **Hybrid local/cloud execution:** Choose permitted runtimes based on data sensitivity, compute availability, and demonstrated capabilities.
- **Reviewed workflow improvement:** Propose changes to checks or routing based on evidence, without permitting agents to expand their own authority.
- **Organization-level governance:** Versioned policy distribution, scoped exceptions, and audit evidence where organizational needs warrant it.

## 5. Priorities, dependencies, and decision gates

| Order | Recommendation | Dependency | Gate |
| --- | --- | --- | --- |
| 1 | Prepare v1.0 release candidate and reconcile documentation | Existing accepted repository | Maintainer reviews claims and release contents |
| 2 | Close M4/M8 discovery evidence when runtime access exists | Functioning Claude Code/Codex environments | Recorded session-level PASS/FAIL/UNVERIFIED |
| 3 | Close M6 pilot | Configured Copy That environment and target authorization | Actual tests and maintainer adoption decision |
| 4 | Prototype v1.1 adoption tooling | Real repository adoption needs | Demonstrated dry-run and safe reversal |
| 5 | Add v1.2 verification integration | Stable adoption and contract interfaces | Actual CI/evidence tests |
| 6 | Evaluate v2.0 execution coordinator | Repeated demonstrated need; security/operations capacity | Bounded proof of concept and separate approval |

The order is flexible: M4/M6/M8 can be completed before release if the maintainer chooses a stricter v1.0 bar. **Deferred is neither Passed nor Failed**, and a missing environment does not block unrelated documentation work.

## 6. Measures of future success

Measure outcomes rather than the number of features:

- Time and effort to adopt in new and existing repositories.
- Instruction-discovery success in explicitly named environments.
- Percentage of material changes with accurately reported verification.
- Human review effort and clarity of acceptance decisions.
- Regression/rework frequency and recoverability after interruption.
- Cost per accepted task when reliable provider data exists.
- Successful removal or upgrade without losing local instructions.

Collect a baseline from pilots before setting numerical improvement targets.

## 7. Final assessment

The project has achieved its primary purpose: a reusable, vendor-neutral engineering foundation for responsible AI-assisted software development. Its strongest features are proportionate workflows, a single normative source, optional adoption, clear human authority, and honest separation of structural checks from runtime guarantees.

The next best investment is **practical adoption and observed validation**, not another layer of policy documents. v1.0 should remain a useful standalone foundation; v1.1–v1.2 can improve developer experience and evidence; v2.0 should be pursued only if an optional execution platform demonstrates sufficient value to justify its complexity.

---

**Supporting history:** [Research index](research/README.md) · [Decisions](decisions/README.md) · [Evaluations](evaluations/README.md) · [Roadmap index](roadmap/README.md) · [Documentation retention](DOCUMENTATION_RETENTION.md)

**Reference documents:** [Start Here](START_HERE.md) · [Capability Status](CAPABILITY_STATUS.md) · [Adoption](ADOPTION.md) · [Security Boundaries](SECURITY_BOUNDARIES.md) · [M6 Pilot](M6_PILOT_PLAN.md) · [Canonical Standard](../core/standards/ENGINEERING_STANDARD.md)

**Status note:** This report reflects accepted PRs and reported verification as of 2026-10-22. Historical files may still contain candidate-era wording; the release-readiness task should reconcile those labels. Future versions and effort estimates in this report are proposals, not approvals.
