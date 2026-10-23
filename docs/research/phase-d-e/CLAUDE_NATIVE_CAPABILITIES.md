# Claude Code vs Claude Agent SDK — native capability assessment

**Snapshot:** 2026-10-22. **State:** Documentation-based feature map; **no local parity test**. Source: Claude Agent SDK [S01] and Claude Code documentation; verify specific event names/SDK setting-source behavior against installed versions.

## Fundamental distinction

The SDK generally does **not** grant the model a new capability unavailable in interactive Claude Code. It **embeds Claude Code's agent harness** and makes sessions, messages, tool calls, approvals and configuration available to an application. The architectural gain is **programmatic orchestration**, not a stronger model.

| Feature | Claude Code | Agent SDK | Required parity test |
| --- | --- | --- | --- |
| File read/write/edit, shell tools | Native | Embedded agent tools | Same scoped test repo and denial cases |
| Lifecycle hooks | CLI/project configuration | SDK-configurable hooks/callbacks | Which events fire, order, blocking and bypass |
| Skills | Project/user skills | Available with correct setting-source/skill configuration | Skill discovery, explicit invocation and provenance |
| Plugins | Plugin ecosystem | Compatibility depends on SDK config and versions | Test actual plugin load, version pin, extension trust |
| Subagents | Native delegated contexts | Configurable native subagents | Tool scoping, parallelism, event capture, resource ceilings |
| MCP servers | Native | SDK MCP configuration | Credentials, tool listing, allowlists, denial |
| Permissions/approvals | Native permission modes/hooks | Programmatic permission configuration and callbacks | Negative tests outside harness and OS boundary |
| Session continuation | Interactive sessions | Programmatic resume/session identifiers | Crash, revision drift, unknown external effects |
| Streaming and structured results | Interactive outputs, supported modes | Machine-consumable messages and result handling | Event schema stability and complete cost telemetry |
| Provider diversity | Claude-centered | Claude-centered | Independent Pi/OpenCode/Codex adapters remain necessary |

### Hook inventory to validate

Candidate events include `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `UserPromptSubmit`, `SubagentStart`, `SubagentStop`, `Stop`, `SessionStart`, `SessionEnd`. **Do not assume every hook is available or blockable in every SDK version**. A hook is useful for auditing and model feedback but **not** an OS sandbox or a guarantee that all possible tool paths are mediated.

### Native subagents versus coordinator-managed workers

- **Native Claude subagents:** ideal for bounded research, implementation and review tasks *within Claude*. Their independent context is not equivalent to an independent OS identity.
- **Coordinator-managed workers:** necessary when different providers, worktree/credential boundaries, durable cross-provider handoff and independent acceptance matter.
- **Start sequentially:** native subagent research/review where useful, then separately authorized verification. Defer concurrent edits.

### Skills, plugins and MCP are different

- **Skills:** reusable instructions/resources, potentially with scripts.
- **Plugins:** package/install distribution for compatible skills, hooks, commands, agents and integrations; third-party plugin code is trusted execution surface.
- **MCP:** tool/data interface; authorization, credentials and output handling must be constrained outside model prompts.
- **Hooks:** event-driven callbacks/checks; useful observability and limited interception.
- **Subagents:** delegated agent contexts and tool configurations; not automatically independent enforcement.

### Recommended SDK-specific spike

1. Pin Claude Code and SDK versions; document auth/billing permitted for the user and application.
2. Compare interactive Claude Code and SDK on same fixture; verify AGENTS/CLAUDE instructions, skills, plugins and setting sources.
3. Exercise hook events and blocking outcomes for file write, shell, MCP and subagent paths.
4. Compare session resume, cancellation, output/event completeness and provider usage metrics.
5. Test external process restrictions, not just model-visible permission denials.
6. Produce a **native feature gap matrix** before writing coordinator replacements.

**Selection principle:** Use Claude-native functionality where it is sufficient; implement coordinator features only for independent authority, durable effects, cross-provider work, measured evaluation and governed improvement.
