# M10 run log — primary evaluation record

**Status:** Four read-only entries (M10.1-INV-01 inventory, M10.1-ARMA-01, -02 and -03 Arm A pre-run load checks). **No task fixture has been executed**; no arm has been run on a task and no outcome measured.\
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
| [M10.1-ARMA-02](#m101-arma-02--arm-a-pre-run-load-check-repeat) | none (load check, no task) | A (pre-run check only) | 2026-10-23 | **Instruction isolation Observed again; path leak fixed; independence still missing** | REPEAT in an independent session; decide user-level scope |
| [M10.1-ARMA-03](#m101-arma-03--arm-a-pre-run-load-check-independent-session) | none (load check, no task) | A (pre-run check only) | 2026-10-23 | **Instruction isolation Observed in an independent session; model-reported, no `/status`** | Decide user-level scope (action 2) |

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

### M10.1-ARMA-02 — Arm A pre-run load check (repeat)

```text
Run ID / date:                 M10.1-ARMA-02, 2026-10-23 (check only; no task given). Repeats M10.1-ARMA-01 per its recommendation; ARMA-01 is not edited
Fixture / M8 mapping:          disposable repo /home/user/armA-fixture-02 (one README, commit 4397a1aa6a6b8ce15169285aa02f8f668658256d); supports M8 C1 as the Arm A absence check
Arm:                           A, pre-run check only
Approved scope / publication:  Read-only load check. Entry recorded in the working tree only; not committed, pushed or published
Repository / base / result:    Starter-kit checkout HEAD 523faff370ab1266f0327b4a57a868b4582b74ef, detached (`git branch --show-current` printed nothing). Unchanged by the check
Fixture location:              Outside the checkout; path does not contain the repo name (Observed: grep count 0). Ancestor scan from the fixture up to / found no CLAUDE.md, AGENTS.md, .claude or .mcp.json
Method:                        Child `claude -p` (stream-json, no tools requested) started from the fixture directory by this cloud session. Prompt: "List the instruction files (CLAUDE.md, AGENTS.md, imports), skills, and MCP servers you have loaded, and say whether you see any content from an engineering-standards starter kit (e.g. STD-01..16). Do not use tools." Init record and reply captured
Claude Code version / model:   2.1.309 / claude-sonnet-5-5 (Observed in init record). Effort UNVERIFIED
Instruction files loaded:      Observed (model report): NONE. No CLAUDE.md, AGENTS.md, imports or STD-numbered content. The reply named only the user email and the commit/PR attribution reminder as context. Note: the prompt itself named "STD-01..16", so the absence report is not a blind test of that string
Native feature inventory:      Init record: 39 tools, 77 skills, 10 plugins, 25 MCP servers, 7 agents. ARMA-01 recorded 70 tools and 30 MCP servers; skills, plugins and agents match. MCP counts differ because servers were still connecting or failing; do not compare them across runs. No starter-kit skill was listed. The reply listed engineering:* skills as generic, not the starter kit
Tools actually used:           None (no tool_use events in the transcript)
Isolation leaks:               None of the repo name or starter-kit content (ARMA-01 leak 1 is fixed). Still present: user-level skills, plugins and MCP servers, shared by every arm
Limits:                        Child process inherited this session's environment and account, so it is not an independent session. The instruction-file result is the model's own report; no separate Observed list of loaded files. The model cannot see on-disk files it was told not to read, so this shows what was loaded, not what is absent from disk. Hook behavior not exercised. Interactive-session behavior UNVERIFIED
External effects:              none. Tokens and cost UNVERIFIED. Raw transcript kept in the session scratchpad only (not linked here; it may be lost when the session ends)
Commands + exit codes:         fixture creation, git init, ancestor scan, `claude --version` (0); `claude -p` load check (0); transcript parse (0)
Evidence labels:               Observed: version, model, fixture path and ancestor scan, init counts, model-reported absence of instruction files. Unverified: effort, independent-session behavior, interactive load report, hook effects, enforcement
Findings:                      (1) The path leak from ARMA-01 is fixed. (2) Instruction-file absence reproduced from a second fixture. (3) Neither check is independent or blind, so the protocol's pre-run check is still only partly satisfied. (4) The user-level capability set is unchanged and still undecided
Reviewer / minutes / cost:     Not reviewed. Minutes not tracked
Recommendation:                REPEAT: independent session (not a child process of a starter-kit session) with a neutral prompt that does not name the kit; decide declare-or-strip for user-level skills, plugins and MCP servers before any task run
```

### M10.1-ARMA-03 — Arm A pre-run load check (independent session)

```text
Run ID / date:                 M10.1-ARMA-03, 2026-10-23 (check only; no task given). Follows the ARMA-02 recommendation; earlier entries are not edited
Fixture / M8 mapping:          none created. The session started in a no-repository working directory; supports M8 C1 as the Arm A absence check
Arm:                           A, pre-run check only
Approved scope / publication:  Read-only load check, authorized by the maintainer as "action 1". Entry recorded on a local branch; not pushed
Session:                       New cloud session session_01PFLGv4oiu9n64LjQUxftFe, created with the session-creation tool from the starter-kit session (parent_session_id recorded), no repository source, tags config:no-git-repo and config:auto-create-pr:off. Permission mode auto
Working directory:             /home/user, not a git repository (Observed by the session: `git rev-parse` failed). Path does not contain the repo name
Method:                        Neutral read-only prompt that did not name the starter kit or STD IDs: report working directory, instruction files loaded, a parent-directory scan for CLAUDE.md/AGENTS.md/.claude, skills/plugins/agents/MCP servers, model and version, and label each as observed or inferred. The session ran one read-only Bash command. Transcript retrieved with list_events
Claude Code version / model:   2.1.309 (Observed by the session: `claude --version`). Model: configured claude-sonnet-5-5, taken from the system prompt; the session did not confirm the serving model. Effort UNVERIFIED
Instruction files loaded:      Observed (model report plus its command output): NONE. No CLAUDE.md or AGENTS.md in /home/user or any parent up to /; no .claude directory in the working directory or its parents. /root/.claude exists with no CLAUDE.md; its other contents were not listed. No starter-kit skill appears among the skill names it listed
Native feature inventory:      Self-reported from its context, not exercised: 30 skills (16 unprefixed, 14 anthropic-skills; it first miscounted 28 and 20, then corrected), plugins not observed, 6 agent types, 11 MCP servers by UUID (Claude Docs, Google Slides/Calendar/Drive/Docs/Sheets, Mermaid Chart, a PDF viewer, Hugging Face, Cloudflare bindings, Gmail) plus the built-in session/routine tool server
Tools actually used:           One read-only Bash command. No connector or MCP tool; no file written (per its report)
Isolation leaks:               None of starter-kit content or repo name seen. The user-level capability set is NOT the same as in ARMA-01/-02 (77 skills, 10 plugins, 25-30 MCP servers there): this session shows 30 skills and no named plugins
Limits:                        The session shares the maintainer's account and environment id, so it is independent of the starter-kit session's context and working directory but not of the account. The report is the model's own, with one command's output as support; `/status` and `/context` were not run. /root/.claude contents were not listed. The prompt asked for instruction files, so absence of starter-kit content is inferred from none being loaded and no kit skill being named. Hook behavior and permission denial were not exercised. Different environment setups can differ, so one session does not establish that every fresh session looks the same
External effects:              A new session exists on the maintainer's account (it can be archived). Observed cost: 0.101 USD for the session's one turn (result record); the cost basis is list price
Commands + exit codes:         session creation (ok); list_events reads (ok); in-session command output returned the paths and version above. No exit codes were captured for the in-session command
Evidence labels:               Observed: no ancestor instruction files, working directory, version, one-turn cost. Model-reported: loaded instructions, skill/agent/MCP names and counts. Unverified: effort, serving model, /status report, hook effects, enforcement
Findings:                      (1) An independent no-repository session loaded no instruction files and no starter-kit content, so the Arm A absence check is satisfied at the model-reported level, without the child-process and prompt-wording limits of ARMA-01/-02. (2) The capability set differs by session setup, so a fresh no-repository session offers a much smaller user-level baseline (30 skills, no named plugins) than the 77-skill, 10-plugin set seen under `claude -p` from the starter-kit session. That is input to the declare-or-strip decision. (3) Self-reported counts were unreliable on first pass; use init records or `/context` for counts
Reviewer / minutes / cost:     Not reviewed. Minutes not tracked. Cost above
Recommendation:                REVISE then proceed: record the user-level scope decision (action 2) before any task run; capture `/status` or an init record for counts in the first real fixture session
```

### Decision D-01 — user-level scope for Arm A (2026-10-23)

```text
Decision:                      Option 1. Arm A (and, for comparability, Arms B and C) run in a fresh no-repository cloud session with the smaller user-level set observed in ARMA-03 (about 30 skills, no named plugins, 11 MCP servers), not as child processes of a starter-kit session
Decided by:                    Maintainer (joshband), in session, 2026-10-23. Recorded by the assistant from that instruction
Basis:                         ARMA-03 (Observed, model-reported) versus ARMA-01/-02 (77 skills, 10 plugins, 25-30 MCP servers under `claude -p` from a starter-kit session)
Still to do per run:           Record the actual skill, plugin and MCP set from an init record or `/context` in each run entry, and confirm it matches across arms. Available-but-unapproved connectors remain not approved (only Claude Code and GitHub are approved)
Not decided:                   Whether to remove the unapproved connectors from the account; effort setting; hook behavior
Revisit when:                  A run shows the capability set differs between arms, or the account's plugins or connectors change
```
