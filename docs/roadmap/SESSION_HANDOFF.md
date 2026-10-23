# Cross-assistant session handoff — ChatGPT, Claude, Claude Code

**As of:** 2026-10-23. **State:** Operational handoff and prompt templates; not acceptance evidence, authorization, or a substitute for live GitHub verification.\
**Canonical repository:** [joshband/ai-engineering-starter](https://github.com/joshband/ai-engineering-starter)\
**Current working research branch:** `research/phase-d-e-execution-options`\
**Draft research + M10 PR:** [#11](https://github.com/joshband/ai-engineering-starter/pull/11) — stacked on `docs/project-accomplishments-roadmap` ([draft PR #10](https://github.com/joshband/ai-engineering-starter/pull/10)); **do not assume either is merged**.\
**Next-work tracking issue:** [#12 — M10 kickoff](https://github.com/joshband/ai-engineering-starter/issues/12).

## Review order and related PRs

Three PRs form a proposed review chain. **Nothing here is merged or accepted.** Verify live states.

| Order | PR | Purpose | Base |
| --- | --- | --- | --- |
| 1 | [#9](https://github.com/joshband/ai-engineering-starter/pull/9) | v1.0.0 candidate scope and deferred-evidence notes (README, CHANGELOG, `docs/CAPABILITY_STATUS.md` M9 row); draft, no tag or release | `main` |
| 2 | [#10](https://github.com/joshband/ai-engineering-starter/pull/10) | Project accomplishments and roadmap | `main` |
| 3 | [#11](https://github.com/joshband/ai-engineering-starter/pull/11) | Phase D/E research, M10 plan, handoff guide | PR #10 branch |

**Proposed order: #9 → #10 → #11.** PR #11 is stacked on #10, so #10 should be reviewed and landed before #11. PR #9 touches the M9 row of `docs/CAPABILITY_STATUS.md`; PR #11 deliberately does **not** edit that row and adds its M10 status in a separate section, so the two should merge without conflict. If #9 or #10 changes after review, re-check merge compatibility. The order is a recommendation for the maintainer, not an approval.

## Cloud session branch behavior

Observed on 2026-10-23 while preparing this work: cloud Claude Code sessions started with the **research branch selected** still came up checked out on `main` (HEAD `1ecb07c`, instructions loaded from `main`) in three separate attempts. The repository's `research/phase-d-e-execution-options` branch (`e2acbe3`) was fetchable but not checked out. A cloud session's branch is whatever the platform created for the task, which may differ from the branch the requester intended.

Handling:

- **Verify, do not assume.** Begin every session with `git branch --show-current`, `git rev-parse HEAD`, `git status --short`, and a fetch of the intended branch. Compare to the expected SHA.
- A platform-created task branch (for example `claude/<task-name>-<suffix>`) is acceptable **if** its starting HEAD equals the intended base and the requester has authorized it by name. A different name alone is not a failure; an unexpected HEAD is.
- If the session is on the wrong revision, stop. Do not switch branches in order to work around the pin without authorization, because the repository instructions loaded at start came from the original revision.
- Commits on a task branch are not on the research branch or in PR #11 until separately integrated (reviewed fast-forward or cherry-pick, authorized separately). Label such work "awaiting integration".
- Checkpoints are posted to issue #12 only when the GitHub integration permits it independently of the branch.

## One-minute context

Build a **portable AI-native software engineering starter kit**, not a new agent platform. Existing M1–M9 materials provide authoritative standards (STD-01–16), risk/autonomy profiles, task/handoff/completion contracts, validation schemas/fixtures, optional skills, Claude Code and Codex adapters, and adoption guidance. Retain all prior work.

**Current implementation constraint:** only **Claude and GitHub** are approved tools for the near-term execution workflow, subject to exact environment/runner/plugin/auth approval. This is an **operating profile**, not an architectural rewrite. The Codex adapter and broader Pi/OpenCode/OpenClaw, model routing, orchestration, learning/RL research remain **preserved but inactive**. No new harness, gateway or coordinator is assumed necessary.

**Next proposed milestone M10 (primary evidence record: [run log](../evaluations/M10_RUN_LOG.md), read-only entries only):** Test the *minimum effective Claude + GitHub reference workflow*, from authorized bounded task to actual verification and separate human GitHub review, comparing native-only Claude with selective starter-kit guidance. **A no-SDK/no-custom-coordinator result is valid.** M10 planning artifacts exist; **M10 runtime tests have not been executed**.

**Unfinished evidence:** M4 Codex-native instruction discovery deferred; M6 Copy That pilot only partially verified (target checks blocked, no publication authorized); M8 runtime-validation plan not executed and lives on its own branch. Do not upgrade status by inference. No v1 release/tag claimed.

**Independent deep research:** A separate research effort was requested to reassess whether custom harness engineering remains worthwhile. Its findings are **not confirmed as incorporated** into PR #11; verify and review any delivered report separately before changing priorities.

## M10 evidence state and next steps (as of 2026-10-23)

**Observed so far (read-only; [run log](../evaluations/M10_RUN_LOG.md)):** M10.1-INV-01 inventory, M10.1-ARMA-01 and M10.1-ARMA-02 Arm A load checks. A fixture outside the checkout, with no ancestor `CLAUDE.md`/`AGENTS.md`/`.claude`, reported no starter-kit instruction files in two runs. **No task fixture has been run and no arm outcome measured.** ARMA-01 and ARMA-02 are merged via PR #13; verify the live state before relying on them.

**Done since:** action 1 below ran as M10.1-ARMA-03 (independent no-repository session, no instruction files or starter-kit content reported; model-reported, no `/status`). ARMA-01 and ARMA-02 merged in [PR #13](https://github.com/joshband/ai-engineering-starter/pull/13). ARMA-03 is on branch `claude/m10-arma-03-run-log`, **awaiting integration**.

**Next actions, in order. Each needs the approval noted:**

1. ~~**Independent Arm A load check.**~~ Done as ARMA-03. Open point: capture `/status` or an init record for counts in the first real fixture session.
2. ~~**Decide user-level scope.**~~ Decided (run log D-01, maintainer): run every arm in a fresh no-repository cloud session with the smaller user-level set seen in ARMA-03, and record the actual set per run.
3. **F1 pair: rerun both arms.** Run 1 (F1A-02 and F1B-01, 2026-10-23, local only, 0.473 USD cumulative) is not comparable: the constraint allowed reading only docs/USAGE.md, Arm A read docs/CONFIG.md anyway, and Arm B stopped to ask. Fix: allow read-only access to the whole repo, edits to docs/USAGE.md only. Arm B's fixture repo is `joshband/m10-f1-fixture` (main at c4b57af, created by the maintainer). Put load check, setup and task in the session's first prompt; follow-up messages between sessions are not treated as instructions. About 0.18 USD remains of the 1 USD ceiling after the rerun, so a new ceiling is needed for anything further.

**Open items that do not block action 1:** effort setting is unverified in every entry; hook firing and permission denial are untested (enforcement is not shown); the earlier ARMA-01 transcript was not retained; the Codex path stays inactive.

## Authority and reading order

**First read, with actual GitHub branch/HEAD verification:**

1. [This handoff](SESSION_HANDOFF.md) and [M10 plan](M10_EXECUTION_PLAN.md) — scope and next action.
2. [Approved tools profile](APPROVED_TOOLING_PROFILE.md) and [proposed ADR-007](../decisions/ADR-007-CLAUDE-GITHUB-FIRST.md) — current vs future architecture.
3. [Native Claude audit](../evaluations/M10_CLAUDE_NATIVE_AUDIT.md), [paired evaluation protocol](../evaluations/M10_PILOT_EVALUATION_PROTOCOL.md) (fixture isolation, how Arms A/B/C receive guidance) and the [M10 run log](../evaluations/M10_RUN_LOG.md) (primary evidence record) — method and evidence requirements.
4. [Issue #12](https://github.com/joshband/ai-engineering-starter/issues/12), [PR #11](https://github.com/joshband/ai-engineering-starter/pull/11), [PR #10](https://github.com/joshband/ai-engineering-starter/pull/10) and [PR #9](https://github.com/joshband/ai-engineering-starter/pull/9) — check actual current state and base/head.
5. **Only when relevant:** [project accomplishments/roadmap](../PROJECT_ACCOMPLISHMENTS_AND_ROADMAP.md), [canonical standard](../../core/standards/ENGINEERING_STANDARD.md), [Phase D/E research dossier](../research/phase-d-e/README.md), [M6 partial pilot](../M6_PILOT_PLAN.md), [capability/evidence status](../CAPABILITY_STATUS.md).

**Precedence:** (a) GitHub *current branch and live PR/issue states* over this snapshot for facts that can change; (b) canonical M1 standards over descriptive plans; (c) approved tooling profile and task-specific authority over agent suggestions; (d) actual check logs and independent reviewer disposition over agent self-reporting. If two documents conflict, report the discrepancy and proposed fix; do not silently overwrite history.

**Branch trap:** Research/M10 content exists on PR #11's **feature branch**, not necessarily `main`. A session that reads `main` alone will incorrectly conclude M10 files are missing. Confirm `git branch --show-current`, `git rev-parse HEAD`, or use the explicit `ref` in a connector. Do not commit directly to `main`.

## Required new-session output

After reading the live sources, return a **handoff checkpoint** before modifying files:

- Repository / observed branch and HEAD SHA; PR #10/#11 status and issue #12.
- Confirmed milestone/evidence statuses, with **observed vs documented vs inferred** labels.
- Current exact task, authority and approved tools, plus an inventory of available-but-unapproved tools and connectors (see [approved versus available](APPROVED_TOOLING_PROFILE.md#approved-versus-merely-available)); what must not be touched.
- Up to **three** prioritized next actions, each with a completion gate and expected artifact.
- Blockers/unknowns, and whether a new approval is required.
- **Explicit confirmation that no unapproved runtimes, target-repo changes, merges or releases were performed.**

Avoid restating the entire project history. Read detailed source documents only on demand. If a repo/tool link cannot be opened, ask for the specific document (or report inaccessible), never infer its contents.

## Prompt A — fresh ChatGPT conversation (architecture, coordination, audit)

```text
Please continue the AI-Native Software Engineering Starter Kit as a new session.
Source of truth: https://github.com/joshband/ai-engineering-starter
IMPORTANT: Read branch research/phase-d-e-execution-options, not only main.
Begin at docs/roadmap/SESSION_HANDOFF.md, then the M10 execution plan,
approved-tooling profile, proposed ADR-007, native audit, and pilot protocol.
Verify live draft PR #11 (stacked on PR #10) and issue #12.

The current execution constraint is Claude + GitHub only. Preserve the
provider-neutral M1–M9 foundation and dormant Codex/Phase D/E alternatives.
Do not assume custom harness/coordinator needed. Do not conflate plans
with experiments, Completed with Accepted, or PR with merged/released.
M4/M6/M8 evidence remains outstanding; verify all mutable statuses.

Act as an independent engineering architect and program reviewer.
First perform a READ-ONLY state reconciliation and return:
1. Current branch/HEAD/PR and issue status with evidence;
2. Known capabilities and unverified/blocked outcomes;
3. Three most valuable next actions with definitions of done;
4. Risks, approvals needed, and recommended first M10 fixture.
Do not modify repositories, create PRs, dispatch runs or merge yet.
If repository access is unavailable, explicitly identify missing
documents instead of guessing.
```

**Model/effort:** ChatGPT GPT-6, High thinking for architecture reviews (if available); Medium for routine follow-up.

## Prompt B — fresh Claude chat (architecture and decision synthesis)

```text
You are the independent principal engineer reviewing a portable AI-native
software engineering starter kit. Treat GitHub as the source of truth:
https://github.com/joshband/ai-engineering-starter
Read branch research/phase-d-e-execution-options and first load
docs/roadmap/SESSION_HANDOFF.md plus its minimum reading order.
Check live PR #10, draft PR #11, and issue #12 rather than trusting
any historical chat summary.

Goal: preserve the full M1–M9 and provider-neutral Phase D/E work while
delivering a Claude + GitHub-only M10 reference workflow now.
Do not mistake research proposals for validated capabilities. No new
provider, Pi/OpenCode/OpenClaw, extra MCP/plugin, SDK service, CI action,
autonomous merge or hosted job is automatically approved.

For this first turn, READ ONLY. Reconcile current status; identify the
highest-value, smallest next M10 experiment; map native Claude Code
capabilities vs demonstrated missing controls; and produce a concise
execution brief: task scope, expected evidence, negative tests, acceptance
gate, risks and necessary authorization. Do not make code/PR changes.
If GitHub cannot be read, state that and request the handoff files.
```

**Recommended setting (as of 2026-10):** Opus 5.5, **High** effort; use **Max** for a difficult one-off architecture/security decision, not every turn. Select actual available model/effort in Claude's UI; don't rely on prompt text to control runtime settings.

## Prompt C — fresh cloud Claude Code session (planning / bounded M10 execution)

```text
Repository: joshband/ai-engineering-starter
SOURCE BRANCH: research/phase-d-e-execution-options (draft PR #11),
STACKED on docs/project-accomplishments-roadmap (draft PR #10).
Tracking: https://github.com/joshband/ai-engineering-starter/issues/12

FIRST: Confirm the checked-out branch, HEAD SHA, current PR/issue states.
Read docs/roadmap/SESSION_HANDOFF.md, M10_EXECUTION_PLAN.md,
APPROVED_TOOLING_PROFILE.md, ADR-007 and the M10 native audit/pilot
evaluation protocol. Do not proceed based only on default-branch files.

MODE FOR THIS SESSION: READ-ONLY PLAN/RECONCILIATION. Do NOT edit files,
push, create a PR, merge, release, install dependencies, add plugins/MCP,
invoke other providers, or start new hosted/CI jobs without new approval.
If the cloud product will automatically push/create a PR on task
completion, STOP BEFORE DISPATCH or use an approved read-only planning
surface instead: instructions cannot disable platform behavior.

Deliver:
1. Actual repo/branch/HEAD and current issue/PR state;
2. M10.0/M10.1 audit observations that can be made read-only,
   distinguishing documented from observed vs unverified;
3. A concrete, minimal disposable F1 baseline fixture proposal and
   corresponding A-vs-B comparison plan (same base/model/permissions);
4. Exact files and commands for a follow-up authorized execution task;
5. Approval needed for any branch writes, PR, runner, network or billing;
6. Handoff checkpoint suitable for a fresh ChatGPT or Claude chat.

Preserve existing STD-01–16 and all research. Do not alter Copy That:
its M6 work was uncommitted and did not authorize publication.
Do not claim tests ran unless you actually ran them.
```

**Model/effort:** Opus 5.5 **xhigh** for the first complex branch/state audit and plan; Sonnet 5.5 **High** for an already approved small documentation or fixture implementation; Opus 5.5 xhigh/Max for genuinely complex debugging if available. Configure through the supported cloud UI/model selector when present; model/effort selection **is not achieved by writing it in the prompt**.

**Cloud-session caveat:** Claude Code cloud may create or offer a branch/PR as part of its normal workflow. Verify the product's current behavior **before** dispatch when task approval says read-only. Choose a local read-only Claude session or Claude chat if the cloud interface cannot honor the required no-write/no-PR boundary.

## Prompt D — authorized follow-on implementation (use only after approval)

```text
Read the current handoff and issue #12; verify branch/HEAD and authority.
Perform ONLY the exact approved M10 task: [FIXTURE / FILES / OPERATIONS].
Allowed repo: [REPO]. Base SHA: [SHA]. Branch: [BRANCH].
Allowed files: [PATHS]. Allowed commands: [COMMANDS].
Publication level: [LOCAL ONLY | COMMIT | PUSH | DRAFT PR].
Model/version and approved tools: [DETAILS].
Acceptance and independent checks: [CHECKS].
Stop conditions: [BUDGET / UNEXPECTED EFFECT / PERMISSION / FAILED CHECK].

Use native Claude first, no new services or adapters. Record exact
command exit statuses, changes, skipped checks, reviewer decision and
rollback path. Never auto-approve, merge, deploy or expand scope.
Return a handoff checkpoint with resulting commit/diff/PR refs
and verified-vs-unverified outcomes.
```

This template is intentionally **not executable without substituting exact approved facts**. Approval of this documentation does not authorize a cloud run or a new PR.

## Between-session checkpoint — append to issue #12 or versioned evidence

Use a concise comment in the issue (or a dedicated evidence file if approved):

```text
Date / session / tool + model + effort:
Repo / branch / starting HEAD / ending HEAD:
Active issue / PR links:
Approved scope and publication authority:
What changed (commit/paths), or READ-ONLY:
Commands actually run and outcomes:
Checks blocked or UNVERIFIED:
Reviewer / acceptance disposition:
New risks or external effects:
Current next action and gating approval:
Links to durable evidence:
```

Before a new session: read the newest checkpoint, then verify mutable GitHub facts. Do not rely on vendor conversation memory, uncommitted local files, or exported transcripts as sole truth. Never put secrets, private client code or raw credentials in the issue.

## Session hygiene

- Claude Code CLI: `/model`, `/effort`, `/status`, `/context`; use `/clear` **between distinct tasks**, `/compact` only within a continuous task, `/export` to preserve a necessary transcript. A compacted memory is convenient but **not authoritative evidence**.
- Claude cloud Code: verify GitHub repository and working branch **before** run; isolated sessions may not see local uncommitted files. Cloud setup/runners and PR behavior require separate approval under the tooling profile.
- ChatGPT/Claude chat: begin with the same repository handoff URL and ask for read-only reconciliation; allow the assistant to ask only for inaccessible source material. Long chat history is optional context, not the spec.
- At every decision gate, maintain a short **fact / interpretation / proposal / unverified** distinction, and update GitHub before changing surfaces.

## Source links and version caveat

Current Anthropic references (subject to product/account availability):
- [Claude chat model, thinking and effort controls](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)
- [Claude Code models and cost/usage](https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code)
- [Claude Code cloud sessions](https://support.claude.com/en/articles/12618689-use-claude-code-in-the-cloud)
- [Claude Code user FAQ and CLI commands](https://support.claude.com/en/articles/14554922-claude-code-user-faq)

The configured model, actual effort and billing/permission context must be **observed in the target account/session**; this document does not provision any entitlements or guarantee cloud interface capabilities.
