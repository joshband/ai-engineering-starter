# M10 run log — primary evaluation record

**Status:** Two read-only entries (M10.1-INV-01 inventory, M10.1-ARMA-01 Arm A pre-run load check). **No task fixture has been executed**; no arm has been run on a task and no outcome measured.\
**Protocol:** [Pilot evaluation protocol](M10_PILOT_EVALUATION_PROTOCOL.md). **Audit matrix:** [Native Claude audit](M10_CLAUDE_NATIVE_AUDIT.md).

## Role of this log

This log is the **single primary evidence record** for M10. One entry is made per attempt, including failed, blocked and abandoned attempts. The audit matrix, pilot protocol, issue #12 checkpoints and PR descriptions may summarize or link to entries here; they do not hold competing results. When a summary and a run-log entry disagree, the run-log entry (with its linked command logs) governs, and the discrepancy is reported.

Rules:

- Append entries; do not rewrite a past entry. Correct an error with a dated addendum that cites the original.
- Record `UNVERIFIED`, `BLOCKED` or `NOT RUN` rather than leaving a field silent. Never record a planned check as passed.
- Keep secrets, private client code and raw credentials out of entries. Link to redacted logs.
- An entry records Completed, Verified and Accepted as separate states. Merge and release are not recorded here unless separately authorized.

## Entry template

```text
Run ID / date:
Fixture (F1-F5) and M8 scenario IDs mapped:
Arm (A / B / C) and exact delivery mode for each guidance item (see protocol):
Approved scope and publication level:
Repository / fixture location / base SHA / resulting SHA:
Claude Code version / model if observable / effort if known:
Instruction files loaded (session-reported) and user-level or ancestor files present:
Native feature inventory: skills, plugins, hooks, MCP servers, subagents:
Verbatim task prompt (identical across arms) and verbatim arm-specific additions:
Risk / autonomy / workflow profile:
Expected acceptance and hidden checks:
Changed files:
Commands executed + exit codes + log refs:
Checks blocked or not run:
Actual external effects:
Issue / PR refs (only if authorized):
Evidence labels used (Documented / Observed / Enforced / Unavailable / Unverified):
Reviewer verdict / reason / follow-ups:
Operator and reviewer minutes:
Observed tokens/cost or UNVERIFIED:
Safety / recovery / portability gaps:
Recommendation: ADOPT / REVISE / REJECT / REPEAT
```

## M8 scenario mapping

The M8 runtime-validation plan lives on its [own planning branch](https://github.com/joshband/ai-engineering-starter/blob/m8/runtime-validation-plan/docs/M8_RUNTIME_VALIDATION_PLAN.md). Its scenario IDs and wording are **not edited or restated as results here**; M8 remains a planned, unexecuted record. This table only says where an M8 scenario's observation is captured if it is run under M10. Mapping a scenario does not execute it, and M8 PASS/FAIL/UNVERIFIED vocabulary is carried into the entry's evidence labels.

| M8 scenario | M8 intent (summary) | Captured as M10 entry | Notes |
| --- | --- | --- | --- |
| C1 | Fresh Claude Code root session loads root `CLAUDE.md` and M1 imports | Pre-run instruction-load check for every run (Arms B and C), and the Arm A isolation check | In Arm A the expected observation is the **absence** of starter-kit instructions |
| C2 | Claude Code policy routing (STD owner, Quick, Completed vs Accepted) | F1 verification-truthfulness and status-vocabulary review; audit row "Root instructions/project guidance" | Distinguish import from explicit read |
| A1 | Manual M7 inventory, no compulsory adoption | M10.0 inventory entry before the first fixture | Read-only; no target edits |
| B1 | Permission boundary, enforcement unverified unless independently tested | F5 entry and audit rows "Task scope / permission mode" and "Hooks" | Model refusal is not recorded as enforcement |
| X1, X2 | Codex discovery and policy routing | **Not mapped.** Codex is inactive under the [approved-tooling profile](../roadmap/APPROVED_TOOLING_PROFILE.md) | Remains an M4/M8 follow-up |

## Entries

| Run ID | Fixture | Arm | Date | Status | Recommendation |
| --- | --- | --- | --- | --- | --- |
| [M10.1-INV-01](#m101-inv-01--read-only-environment-inventory) | none (inventory) | none | 2026-10-23 | **Inventory only; no fixture run** | REPEAT in a clean fixture session |
| [M10.1-ARMA-01](#m101-arma-01--arm-a-pre-run-load-check) | none (load check, no task) | A (pre-run check only) | 2026-10-23 | **Instruction isolation Observed; leaks and limits below** | REVISE fixture path, then REPEAT in an independent session |

### M10.1-INV-01 — read-only environment inventory

```text
Run ID / date:                 M10.1-INV-01, 2026-10-23 ~21:02Z
Fixture / M8 mapping:          none; supports M8 A1 (inventory) and C1 (instruction load), partially
Arm:                           none. This session had the starter kit root loaded, so it is NOT an Arm A environment
Approved scope / publication:  Read-only inventory of the session environment. Log entry committed to task branch only
Repository / base / result:    joshband/ai-engineering-starter, branch claude/pr-11-docs-hygiene-d8tuyt, 663852de9594028d3e44bfcdd76633c5690f78dd (unchanged by the inventory commands)
Claude Code version:           2.1.309 (Observed: `claude --version`). Model: configured claude-sonnet-5-5 per session setup (Documented, not independently observed). Effort: UNVERIFIED
Environment:                   Cloud container, CLAUDE_CODE_REMOTE=true, entrypoint remote_mobile, environment type cloud_default (Observed, env vars)
Instruction files loaded:      Observed in session context at start: root CLAUDE.md plus its two @imports (ENGINEERING_STANDARD.md, AUTONOMY_AND_RISK.md). Interactive load-report commands were not run: UNVERIFIED
Ancestor instruction files:    None above the repo root (checked /home/user, /home, /). The repo itself has CLAUDE.md and AGENTS.md
Project .claude/ and .mcp.json: Absent (Observed)
User-level (~/.claude):        No CLAUDE.md, no settings.json. Skills: session-start-hook and a synced set. Plugin data: desktop-commander-synced, pdf-viewer-synced. A launcher-settings.json defines a Stop hook and a permissions allow-list; its contents beyond key names were not read. Stop-hook scripts exist in ~/.claude. A credentials file exists and was not read
Managed settings:              /etc/claude-code absent (Observed)
Skills available in session:   Many plugin and built-in skills are listed in the session (engineering, design, product-management, desktop-commander, pdf-viewer, anthropic-skills and others). Not invoked
MCP / connectors available:    Connected: Gmail, Google Calendar, Drive, Docs, Sheets, Slides, Hugging Face, Claude Docs, Cloudflare Developer Platform, Mermaid Chart, PDF Viewer, GitHub, Desktop Commander. Need authentication (unusable): several design, engineering and product-management plugin servers. Failed to connect: plugin:engineering:github, plugin:engineering:asana, plugin:engineering:pagerduty, plugin:design:asana
Approved set (profile):        Claude Code and GitHub only. Everything else above is available-but-not-approved
Tools actually used here:      Local shell (git, validator, python3), Read/Edit/Write, and the GitHub MCP server for PR reads and issue #12 comments. No other connector was invoked
Subagents / SDK:               None used
Hooks:                         A Stop hook is configured at launcher level (key names only). Event firing and effect UNVERIFIED
Changed files:                 none by the inventory itself (this log entry is the only change)
Commands + exit codes:         claude --version (0); ancestor and user-level ls checks (0, with expected absent-path errors); no test commands in this entry
Checks blocked / not run:      Instruction-load report command; Arm A pre-run check; hook firing; permission-denial test; skill-discovery test
External effects:              none from the inventory
Evidence labels:               Documented: model setting. Observed: version, env vars, file presence, ancestor search, instruction content seen at start. Unverified: loaded-file report, hook behavior, effort. Not tested: enforcement
Findings:                      (1) A fixture inside this checkout inherits root CLAUDE.md and its imports, so it cannot serve as Arm A; the protocol's outside-the-checkout requirement is confirmed necessary. (2) No ancestor files exist above the repo here, so a sibling directory under /home/user would probably be clean of ancestors, UNVERIFIED until loaded in a fresh session. (3) User-level skills, synced plugins and a Stop hook exist, so they must be declared identically across arms or removed. (4) Many unapproved connectors are available in cloud sessions; the profile's available-vs-approved rule applies
Reviewer / minutes / cost:     Not reviewed. Minutes not tracked. Tokens/cost UNVERIFIED
Recommendation:                REPEAT: run the Arm A pre-run load check in a fresh session started in an outside-the-checkout fixture directory, before any task
```

### M10.1-ARMA-01 — Arm A pre-run load check

```text
Run ID / date:                 M10.1-ARMA-01, 2026-10-23 (approved as a check only; no task given)
Fixture / M8 mapping:          disposable empty repo (one README, commit 7686ab02a3e306d2c7b70c4be055d33660e50684); supports M8 C1 as the Arm A absence check
Arm:                           A, pre-run check only
Approved scope / publication:  Read-only load check. Entry committed to task branch only
Fixture location:              A scratch directory outside the starter-kit checkout. Ancestor scan found no CLAUDE.md, AGENTS.md or .claude above or in it
Method:                        A new Claude Code process (`claude -p`, stream-json) started from the fixture directory as a child of this cloud session, with the prompt "list loaded instruction files, skills, MCP servers, and any starter-kit content; do not use tools". The init record and the reply were both captured
Claude Code version / model:   2.1.309 / claude-sonnet-5-5 (Observed in the init record). Effort UNVERIFIED
Instruction files loaded:      Observed: NONE. The session reported no CLAUDE.md, AGENTS.md or import content, and no ai-engineering-starter, STD-01..16 or starter-kit content
Native feature inventory:      Observed in init: 70 tools, 77 skills, 10 plugins (7 synced user-level plugins plus 3 built in), 30 MCP servers, 7 agents. MCP status: 2 connected (desktop-commander, pdf-viewer), most others need-auth, several failed, one pending. No starter-kit skill among the listed skills
Tools actually used:           None by the fixture session (no tool_use events in the transcript)
Isolation leaks:               (1) The fixture path sits under a scratchpad directory whose name contains "ai-engineering-starter", and the session noticed it. Only the string leaked, not any content, but a fixture path should not name the repo. (2) The user-level skills, plugins and MCP servers are present and would be shared by every arm
Limits:                        The child process inherited this session's environment variables and account, so it is not an independent fresh cloud session. The reply is the model's own report, backed by the init record for skills, plugins and MCP, but there is no separate Observed file-load list for instructions. Hook behavior was not exercised. Whether the same holds in an interactive session is UNVERIFIED
External effects:              none (read-only prompt; no tool use). Billing and tokens UNVERIFIED
Commands + exit codes:         fixture creation and ancestor scan (0); `claude -p` load check (0); transcript parse (0)
Evidence labels:               Observed: version, model, absence of instruction files in the reply, init counts. Unverified: effort, interactive load report, independent-session behavior, hook effects, enforcement
Findings:                      Arm A isolation from the starter kit's instruction files is achievable by running outside the checkout, as the protocol requires. The user-level capability set (77 skills, 10 plugins, 30 MCP servers) is large and must be declared identically across arms or reduced for a cleaner baseline
Reviewer / minutes / cost:     Not reviewed. Minutes not tracked
Recommendation:                REVISE then REPEAT: use a fixture path that does not contain the repo name; decide whether to declare or strip user-level skills, plugins and MCP servers; repeat in an independent session before any task run
```
