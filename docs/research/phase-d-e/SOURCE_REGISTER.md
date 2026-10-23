# Primary source register — Phase D/E options

**Research snapshot:** 2026-10-22. Expanded to include Pi, OpenCode, OpenClaw, OpenHands and Goose; original research preserved below. Source links were researched as public documentation; these are not executed integration tests. Follow the publisher's latest version and permission terms before coding. **Every claim in this dossier labeled [Snn] traces to an entry below.**

| ID | Source and URL | What it supports | Limit / follow-up |
| --- | --- | --- | --- |
| S01 | Anthropic, [Claude Agent SDK overview](https://platform.claude.com/docs/en/agent-sdk/overview) | Python/TypeScript embedded Claude Code harness, tools, permissions, hooks, sessions, skills; warning about third-party claude.ai login/rate-limit use | Verify actual plan/auth, security, SDK version |
| S02 | Claude Help Center, [Use the Claude Agent SDK with your Claude plan](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan) | Oct 7, 2026 guidance concerning plans/API credits and SDK access | Does not remove separate third-party product limitations; validate current user eligibility |
| S03 | OpenAI, [Codex SDK](https://learn.chatgpt.com/docs/codex-sdk) | Programmatic local Codex agent start, continue, resume | Verify available SDK, auth, sandbox and parity with Claude |
| S04 | OpenAI, [Codex as a platform](https://developers.openai.com/blog/codex-as-a-platform) | SDK vs deeper app-server interface | Requirements, models and managed services evolve |
| S05 | LM Studio, [Local LLM API server](https://lmstudio.ai/docs/developer/core/server) and [REST API](https://lmstudio.ai/docs/developer/rest) | Local serving, native and compatible endpoints, model management | Doesn't supply full agent harness or isolation; test actual model |
| S06 | LangChain, [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence) | Checkpointers, short/long-term state and persistent backends | A checkpoint is not authorization or an external effect ledger |
| S07 | Temporal, [Workflow Execution](https://docs.temporal.io/workflow-execution) | Durable execution, replay and activity-based side effects | Requires service/workers, deterministic workflow design, idempotent effects |
| S08 | LiteLLM, [Budgets and rate limits](https://docs.litellm.ai/docs/proxy/users) | Proxy spend/rate settings; DB requirements and optional fail-closed budget mode | Documented DB-less and stale-counter situations need independent stop limits |
| S09 | GitHub, [Choosing GitHub App permissions](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app) | Minimal permission selection for GitHub identities | Actual grants, token handling and bypass routes must be tested |
| S10 | OpenTelemetry, [GenAI agent spans](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md) | Evolving agent/tool tracing semantics | Status is Development; redact prompts, tokens, secrets |
| S11 | Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) (2026-01-09) | Code/model/human graders, capability and regression evaluation, dataset design | Industry methods, not an outcome guarantee for this system |
| S12 | [Self-Improvements in Modern Agentic Systems](https://selfimproving-agent.github.io/) (2026 survey) | Distinction between model-weight and scaffolding optimization | Research survey; verify particular papers before implementing |
| S13 | OpenAI, [Agents SDK documentation](https://openai.github.io/openai-agents-python/) | Alternative SDK for an application-owned tool loop | Not a drop-in Claude Code/Codex coding harness |
| S14 | Anthropic, [Automated Weak-to-Strong Researcher](https://alignment.anthropic.com/2026/automated-w2s-researcher/) (2026) | Example of AI-driven iterative research in specialized benchmark environments | Does not demonstrate safe recursive autonomous engineering outside its testbeds |

## Expanded ecosystem sources (added 2026-10-22)

| ID | Source and URL | What it supports | Limit / follow-up |
| --- | --- | --- | --- |
| S15 | Pi, [coding agent README](https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent) | Minimal harness, model providers, SDK, RPC/JSON, extensions, skills, packages; subagents via extensions | Pin exact upstream version; verify permissions, model access and extension provenance |
| S16 | Pi, [extensions documentation](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md) | Lifecycle events, tool interception, custom tools, subagent examples; extensions execute with process privileges | Extension gates are not OS isolation; test shell/other tool paths |
| S17 | OpenCode, [SDK](https://opencode.ai/docs/sdk/) | TypeScript client and server-driven programmatic control | Pin API/server version and events |
| S18 | OpenCode, [plugins](https://opencode.ai/docs/plugins/) | Event hooks and JS/TS plugin extensibility | Plugins run code; inspect installation and trust model |
| S19 | OpenCode, [providers](https://opencode.ai/docs/providers/) | Many cloud/local providers and provider configuration | Credential storage, billing, feature parity and local quality need testing |
| S20 | OpenHands, [Software Agent SDK](https://docs.openhands.dev/sdk) and [project SDK repo](https://github.com/OpenHands/software-agent-sdk) | Agent/workspace/event/server architecture, security policy and remote execution | More operational surface; isolation and persistence require hands-on proof |
| S21 | Goose, [SDK / GDK](https://goose-docs.ai/docs/gdk/sdk/) | Native Rust SDK, provider bindings and model support | Python/Kotlin shared bindings and SDK are alpha; do not assume full feature parity |
| S22 | OpenClaw, [ACP agents](https://docs.openclaw.ai/tools/acp-agents) | External coding harness dispatch (Claude, Codex, OpenCode, others), separate native Codex app-server path | Confirm ACP plugin versions, external harness auth and cancellation |
| S23 | OpenClaw, [ACP sessions](https://docs.openclaw.ai/tools/acp-agents/sessions) | Persistent/bound ACP sessions and spawn lifecycle | Session persistence is not external effect reconciliation |
| S24 | OpenClaw, [ACP delivery and sandbox boundary](https://docs.openclaw.ai/tools/acp-agents/delivery) | **ACP external harnesses execute on host outside OpenClaw sandbox** | Must independently restrict host, filesystem, network and credentials |
| S25 | OpenClaw, [session visibility and cross-agent controls](https://docs.openclaw.ai/gateway/config-tools/sessions-and-subagents) | Cross-agent access and session visibility configuration, including broad defaults | Explicitly set narrow visibility; test privacy and ACLs |
| S26 | OpenClaw, [ACP bridge](https://docs.openclaw.ai/cli/acp) | Gateway-backed ACP server bridge vs external harness ACP agent mode | These are different integration modes; avoid conflation |

### Supplementary reference candidates, not fully evaluated

- [Mastra documentation](https://mastra.ai/docs), [Pydantic AI durable execution](https://ai.pydantic.dev/durable_execution/), [DBOS documentation](https://docs.dbos.dev/): potential workflow/durability alternatives; verify current features and operational burden before shortlisting.
- [Cline](https://docs.cline.bot/) and [Aider](https://aider.chat/docs/): IDE-centric and lightweight Git editing baselines; not yet SDK/permission audited.
- [Agent Client Protocol](https://agentclientprotocol.com/): protocol-level integration concept; do not assume common protocol implies identical security or skill semantics.

## Research methods and caveats

- Prefer official API documentation for concrete feature claims, and vendor engineering notes for experience-based design guidance.
- **Availability changes quickly:** re-check APIs, model IDs, subscription terms, prices, and security defaults before an implementation PR.
- Vendor docs are evidence of *documented* behavior, not verified behavior under your actual account/OS/repo.
- Performance, accuracy, token cost and compatibility have **not** been benchmarked for this starter kit.
- Comparisons and priority scores are synthesized recommendations, not quoted vendor rankings.
- External research imported later must preserve provenance, original dates, attribution, and restrictions; see [retention guidance](../../DOCUMENTATION_RETENTION.md).

## Open factual questions to verify in spikes

1. Which SDK, authentication method, model access and charging pathway are authorized for this specific Claude-first coordinator?
2. Which hook/tool permission checks actually deny alternate filesystem, network, shell and MCP routes?
3. What event/usage fields are emitted reliably by Claude and Codex, including cancellations and failures?
4. Can sessions resume without replaying externally consequential side effects?
5. Is an independent process/container identity practical in both target macOS machines?
6. What local LM Studio models run acceptably for low-risk coding tasks on available memory/compute?
7. What measurable outcome would justify replacing SQLite with LangGraph/Temporal, or static routing with learned routing?
