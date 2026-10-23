# M10 — Claude native capability audit and parity evidence

**Status:** Proposed test protocol, **not an executed assessment**.  
**Execution profile:** [Claude + GitHub](../roadmap/APPROVED_TOOLING_PROFILE.md).  
**Initial conceptual map:** [Claude Code vs Agent SDK](../research/phase-d-e/CLAUDE_NATIVE_CAPABILITIES.md).

## Hypothesis and method

Test the **minimum effective harness**: Claude Code already supports many agent-control mechanisms. Adding SDK wrappers, hooks, MCP tools, nested agents, or custom coordinators may not improve accepted task outcomes and can introduce complexity. Compare actual supported behavior *in the installed and authorized environment*, not a marketing feature checklist. The same-model comparison is still confounded by prompt/context and tool defaults; disclose differences.

Record environment *before* running: Claude Code version; SDK version **only if independently approved**; model identifier when observable; auth/billing category (no secrets); OS/container; local allowed tools; repository baseline revision; skill/plugin/MCP inventory; hook/config sources; GitHub security/branch review settings; task profile and data classification.

## Evidence labels

- **Documented:** linked official documentation describes it; no tested claim.
- **Observed:** reproducible output from one explicitly named environment/commit/version.
- **Enforced:** a bypass attempt blocked by a separate trusted boundary (OS identity, sandbox, GitHub permission, network policy); provide negative evidence.
- **Unavailable:** confirmed absent in a particular authorized version/configuration.
- **Unverified:** not tested or ambiguous; do not convert into PASS.

## Audit matrix (fill in during M10; no claimed test results)

| Native feature | What to inspect or exercise | Expected record | Observed |
| --- | --- | --- | --- |
| Root instructions/project guidance | Discover root `CLAUDE.md`, imported references, risk guidance without duplicating `AGENTS.md` | Auto-loaded vs manually referenced, conflicts and citations | **Unverified** |
| Task scope / permission mode | Attempt a prohibited fixture path write and command with explicit tool policy | Model refused vs external denial | **Unverified** |
| Hooks | Inventory configured events, `PreToolUse`/post-tool/stop availability; deliberately rejected action | Event fired, mediation surface, bypass/unknown behavior | **Unverified** |
| Skills | Try a relevant M5 optional procedure and a no-skill baseline | Discovery/invocation, unexpected authority, correctness, overhead | **Unverified** |
| Plugins | Inventory approved installed plugins; no unapproved install | Provenance, version, code trust, actual behavior | **Unverified** |
| Native subagents | Delegate read-only investigation; check context/tool restriction and join/cancellation | Separate contexts, tool calls, cost if observable | **Unverified** |
| MCP | Inventory; run read-only tool if **separately approved**; test denial | Server identity, scopes, outbound data path | **Unverified** |
| Session continuation | Interrupt safe fixture and resume with changed working tree/HEAD | Restoration vs manual reconciliation, no blind external retries | **Unverified** |
| Compaction/context | Bounded context-heavy task with/without built-in compaction | Evidence quality, lost instructions, tokens if measurable | **Unverified** |
| Structured outputs / events | Capture task result, tool call, stop cause and timing | Enough evidence for portable completion contract? | **Unverified** |
| Programmatic API | **Only if separately approved:** compare Agent SDK to Code for same fixture | What SDK adds beyond native Code, auth and cost | **Not authorized for this test by assumption** |
| GitHub workflow | Human-authorized issue/branch/draft PR/review/checks | Actual permission enforcement and accepted vs merged status | **Unverified** |

## Minimum native-only baseline

1. Select a fixed benign fixture and issue/task prompt with expected output and deterministic tests. Record input and commit.
2. Run native Claude Code with only repository's **already-present** instructions and approved tools. Do not add hooks, plugins, packages or MCP servers to improve baseline.
3. Run matched task using selective M1/M5 starter guidance; keep risk, tool scope, model and evaluation criteria stable.
4. If a clear gap remains, **one change at a time** add an already-approved native hook/skill/subagent configuration and rerun.
5. Record actual check commands/exit statuses, reviewer verdict and effort. Use [pilot protocol](M10_PILOT_EVALUATION_PROTOCOL.md).
6. Issue a feature-gap memo that maps each remaining gap to **native configuration**, **external enforcement**, **SDK-specific requirement**, or **not worth automating**.

## Guardrails

- Hooks are not an OS security boundary; model refusal is not independent enforcement.
- Native subagents may share host execution permissions; a separate context is not isolation.
- Skill instructions are neither automatically invoked nor enforced merely by their presence.
- Do not install new plugins/MCP servers or enable hosted agents to complete a check.
- Do not treat successful context compaction or recovery as exactly-once execution.
- Do not treat automatic PR generation as authorization to merge.

## References

- [Claude Code documentation](https://code.claude.com/docs/en/overview)
- [Claude Code hooks](https://code.claude.com/docs/en/hooks)
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview)
- [Existing starter kit Claude adapter](../../adapters/claude-code/README.md)

**Exit:** Filled versioned matrix, redacted run references, discrepancies, and an explicit **native sufficient / add minimal control / SDK spike / stop** recommendation; no self-certified security guarantee.
