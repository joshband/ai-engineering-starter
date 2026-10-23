# M10 run log — primary evaluation record

**Status:** Empty template. **No M10 run has been executed**; every row below is a placeholder, not a result.\
**Protocol:** [Pilot evaluation protocol](M10_PILOT_EVALUATION_PROTOCOL.md). **Audit matrix:** [Native Claude audit](M10_CLAUDE_NATIVE_AUDIT.md).

## Role of this log

This log is the **single primary evidence record** for M10. One entry is made per attempt, including failed, blocked and abandoned attempts. The audit matrix, pilot protocol, issue #12 checkpoints and PR descriptions may summarize or link to entries here; they do not hold competing results. When a summary and a run-log entry disagree, the run-log entry (with its linked command logs) governs, and the discrepancy is reported.

Rules:

- Append entries; do not rewrite a past entry. Correct an error with a dated addendum that cites the original.
- Record `UNVERIFIED`, `BLOCKED` or `NOT RUN` rather than leaving a field silent. Never record a planned check as passed.
- Keep secrets, private client code and raw credentials out of entries. Link to redacted logs.
- An entry records Completed, Verified and Accepted as separate states. Merge and release are not recorded here unless separately authorized.
- Keep the placeholder rows below until a real run replaces them.

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
| _none_ | _none_ | _none_ | _none_ | **NOT RUN** | _none_ |
