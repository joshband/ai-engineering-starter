# Current approved-tooling profile — Claude + GitHub

**State:** Working implementation constraint for the next proposed pilot, recorded 2026-10-23. **Not** an organization-wide policy, a modification to the M1 canonical standard, or evidence that a particular tool/integration is authorized in every environment.

## Intent and invariants

- **Current executable scope:** Claude (Claude Code in an approved interactive/automation environment) plus GitHub (repositories, issues, branches, PRs, reviews and explicitly approved Actions). The starter kit's Markdown standards, contracts, existing Claude adapter, and its existing local standard-library validation code remain available as project materials; this does not authorize running arbitrary third-party services.
- **Portable design scope:** Keep provider-neutral task, handoff, completion, exception and evidence formats; keep the pre-existing Codex adapter, other-provider research and coordinator options **intact but inactive**.
- **Never infer approval from brand names.** GitHub Actions runners, third-party Actions, MCP servers, Claude plugins, Claude API/Agent SDK credentials, managed agents, hosted executors, and network connections each require review under the actual organization's approved configuration.
- **No new normative STD requirements.** The [canonical standard](../../core/standards/ENGINEERING_STANDARD.md) and [risk/autonomy guidance](../../core/standards/AUTONOMY_AND_RISK.md) remain authoritative. This profile records a local implementation choice.
- **No default autonomous merge, deployment, publish, cloud creation, production credentials, silent provider fallback, or unbounded unattended work.** Consequential actions retain human authorization and independent platform control.

## Allowed, conditional and deferred

| Surface | Status for M10 planning | Conditions and limits |
| --- | --- | --- |
| Existing Claude Code interactive use | **Candidate active execution** | Authorized account/environment; check installed version, permissions, tools, skills and plugin list |
| Claude built-in tools, skills, hooks and native subagents | **Evaluate within Claude** | Use version-pinned capabilities; do not treat hooks/instructions as OS isolation; inspect scripts and outbound paths |
| Claude Agent SDK | **Conditional / do not require** | Introduce only if native interactive workflow demonstrably lacks programmatic lifecycle/structured telemetry; separately confirm approved API authentication, costs and execution environment |
| GitHub issues, branches, draft PRs, review and evidence links | **Candidate active control plane** | Scoped repository permissions; PR creation only after exact target authorization; approval is separate from implementation |
| GitHub Actions | **Conditional** | Existing approved runners/actions only; least-privilege `GITHUB_TOKEN`; lockfile or reviewed full-SHA actions as supported; avoid risky untrusted PR execution and unnecessary secrets |
| GitHub-hosted Claude automation | **Conditional** | Requires explicit approval of Action/runner, model API path, identity, network access, charging and secrets handling |
| Third-party Claude plugins, extra MCP tools, custom shell scripts | **Not implicitly approved** | Audit installed/introduced code, provider connections, data paths and privileges individually |
| Codex runtime, Pi, OpenCode, OpenClaw, OpenHands, Goose, LiteLLM, LM Studio, LangGraph, Temporal, other services | **Deferred implementation** | Retain reports, interfaces and design artifacts; require new approval before use |
| Self-updating skills/prompts/policies | **Proposal only** | Changes by PR, fixed evaluation corpus, maintainer approval before activation |
| RL policy/model training, autonomous policy promotion | **Research only** | Not part of M10 |

## Local execution workflow (first reference)

1. Human establishes repository, baseline commit, task scope, allowed paths, autonomy/risk profile, prohibited actions, and acceptance criteria.
2. Read current repository instructions and existing standard. Prefer native Claude Code capabilities and minimal workflow aids; do not install a second harness just for feature parity.
3. Execute only inside authorized environment/branch. Distinguish **model compliance** from actual host and GitHub enforced controls.
4. Run available deterministic checks and capture exact outputs (command, commit, exit/status, timestamp); mark skipped/blocked **Unverified**, never Passed.
5. Present a diff and evidence to an independent reviewer; PR only if publication to that repository was authorized. Never infer Accepted or Merged from Completed.
6. Compare observed results to the native-only baseline and record whether added guidance improved accepted outcomes enough to offset overhead.

## Portability contract

The durable interfaces are **not** Claude-specific: the existing M1 task/handoff/completion/exception contracts, optional M2 structured records and their documented validation semantics remain stable. The run adapter must disclose `provider`, `harness`, `model` (if observed), effective permissions, actual tools used, artifact refs, observed test results, and unavailable metrics. These are **observations**, not an assertion that all backends expose identical hooks, billing, permission semantics or skills.

When another provider becomes approved: validate its existing adapter against an identical fixture and the core contracts, list gaps explicitly, and only then enable that path. Do **not** eagerly build a universal runtime.

## Owner decision checklist (before the first M10 run)

- [ ] Which Claude account/edition and execution environment may run? Record version and billing route.
- [ ] Which repository, baseline revision, files and task operations are authorized?
- [ ] May the agent create a branch, commit, push and/or **draft PR**, or local edits only?
- [ ] Which GitHub Actions runners and actions are approved; are they already configured?
- [ ] Which shell/MCP/plugins or outbound network paths exist, and which are denied?
- [ ] What checks and human approval gates are required?
- [ ] What sensitive data and secrets are prohibited? Where may evidence be retained?

**Approval state:** M10 documentation planning is authorized. A future target-repository modification, cloud job, token purchase, or automated workflow launch still requires a task-specific authorization.

**References:** [M10 plan](M10_EXECUTION_PLAN.md), [ADR-007](../decisions/ADR-007-CLAUDE-GITHUB-FIRST.md), [GitHub Actions security guidance](https://docs.github.com/en/actions/reference/security/secure-use), [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview).
