# Expanded agent ecosystem review — Phase D/E

**Snapshot:** 2026-10-22. **Evidence class:** Official vendor/project documentation plus architecture analysis; **no hands-on benchmark**. Read with [technology options](TECHNOLOGY_OPTIONS.md), [native Claude feature map](CLAUDE_NATIVE_CAPABILITIES.md), [learning research](LEARNING_SYSTEMS.md), and [source register](SOURCE_REGISTER.md).

## First separate the layers

| Layer | Problem to solve | Candidate options | Recommendation |
| --- | --- | --- | --- |
| Coding harness | Tool use, repository edits, coding sessions, native skills and subagents | **Claude Agent SDK, Pi, OpenCode**, Codex SDK, OpenHands SDK, Goose, Aider, Cline | **Benchmark first three** with the same Claude model when permitted; keep Codex as a native portability reference |
| Coordinator / gateway | Persistent jobs, scheduling, remote access, dispatch to external harnesses | **OpenClaw**, lightweight custom coordinator, OpenHands automation | **Evaluate OpenClaw against minimal custom coordinator**, not as a drop-in coding harness |
| Durable workflow engine | Restart/replay, retries, durable state | SQLite state machine, LangGraph, Temporal, DBOS, Mastra, Pydantic AI | **Start simple**; research richer engines only on demonstrated requirements |
| Model gateway / inference | Multi-provider APIs, cost policies, local model serving | LiteLLM, direct APIs, LM Studio, Ollama, vLLM | Static approved routing first; gateway only if operational benefits outweigh new risks |
| Independent execution controls | OS permissions, filesystem/network isolation, credentials, approvals | Host/container/sandbox policies, separate identities, GitHub App grants | Required regardless of harness or coordinator |
| Evaluation and learning | Quality measurement, reviewed changes, adaptive selection, RL research | Deterministic checks, human/LLM graders, benchmark harness, constrained bandits | Begin instrumentation immediately; learning requires review and held-out evidence |

Do **not** compare OpenClaw with Pi as if they were interchangeable; they can be composed. Do **not** assume adding a second model to one harness provides native Claude Code or Codex parity.

## Harness shortlist — research, not empirical rankings

| Option | Documented strengths | Limitations / due diligence | Disposition |
| --- | --- | --- | --- |
| **Claude Agent SDK** | Claude Code tool loop, sessions, hooks, skills, subagents, permissions [S01] | Claude-centered; settings-source parity and allowed auth/billing must be tested | **Tier 1 / finalist** |
| **Pi** | Minimal terminal agent, SDK/RPC/JSON modes, TypeScript extensions, skills, packages, broad providers [S15] | Subagents/plan mode are extension-based; trust and inspect extension code; model compatibility ≠ harness parity [S16] | **Tier 1 / finalist** |
| **OpenCode** | JS/TS SDK for programmatic server control, event plugins, many provider integrations [S17–S19] | Plugin execution and auth storage require security review; server operational footprint; verify exact skill/subagent semantics | **Tier 1 / finalist** |
| **Codex SDK** | Native Codex thread start/continue/resume [S03] | Different agent semantics from Claude; no automatic shared feature parity | **Tier 2 / mandatory portability baseline** |
| **OpenHands Software Agent SDK** | Agents, tools, workspaces, events, security policies, Agent Server, remote execution; plugins and ACP delegation [S20] | Larger runtime/deployment surface; evaluate whether its isolation is more reliable than a custom worker | **Tier 2 / serious alternative** |
| **Goose / GDK** | Open source, model providers, extensions; SDK/GDK APIs [S21] | Shared-language SDK is alpha; verify full agent orchestration surface in chosen language | **Tier 2** |
| **Cline** | IDE-centered approval and coding experience | Less compelling for headless local coordinator; use as human-interaction reference | Tier 3 |
| **Aider** | Lightweight Git-oriented edit/test workflow | Limited justification as primary durable coordinator; use as lightweight baseline | Tier 3 |

**Pi clarification:** Pi's core intentionally omits built-in subagent/plan workflows; extensions implement them. Pi extensions can run arbitrary code with process permissions [S16]. That makes Pi highly flexible **and** an extension supply-chain/authority risk.

**OpenCode clarification:** Provider diversity and JS SDK are documented [S17–S19], but plugins and provider auth must be evaluated for permission isolation, lifecycle correctness and secret exposure.

## OpenClaw as a coordinator/gateway candidate

**Why evaluate:** OpenClaw can dispatch to external coding harnesses through ACP, supports persistent/bound sessions, and has separate native Codex app-server integration [S22, S23]. This could provide remote operation and existing session coordination without creating a bespoke gateway.

**Critical security finding from official docs:** OpenClaw ACP external harness sessions currently run **on the host**, outside the OpenClaw sandbox; the external harness controls filesystem/CLI permissions [S24]. OpenClaw session-tool visibility and cross-agent access can be broad by default [S25]. Thus **an OpenClaw sandbox switch alone does not make ACP-run Claude/Codex isolated**. A safe evaluation must use a separately restricted host/container/identity, deliberately scoped session visibility, and explicit denied-access tests.

**Fit decision:** OpenClaw is **Tier 1 for a coordinator comparison**, not an unconditional default. If remote access, persistent messaging, scheduled workflows, and multi-harness dispatch are central, it may save significant engineering. If the goal is a simple local controlled task runner, its gateway/channel/plugin surface may be unnecessary complexity.

## Explicit build-versus-adopt comparison

| Scenario | Candidate | What to prove |
| --- | --- | --- |
| Preserve the richest Claude Code semantics | Claude Agent SDK | Project setting sources, skills, hooks, plugins, subagents, MCP, native permissions, resume and cancellation |
| Small provider-flexible local harness | Pi | SDK/RPC, custom provider, safe extensions, skill import, isolation, comparable accepted task outcomes |
| Multi-provider integrated developer platform | OpenCode | Server/SDK event reliability, plugin controls, auth isolation, costs and tool semantics |
| Stronger remote sandboxed software agent | OpenHands SDK | Real workspace containment, replay/evidence, operations burden, Claude model quality |
| Always-on dispatch and remote workflows | OpenClaw + external harness | ACP lifecycle, gateway policy, host sandbox gap, cross-session visibility, auth and operational exposure |
| Minimum independently controlled system | Custom coordinator + selected harness | Effort to implement journal/reconciliation vs simpler architecture and verifiable controls |

## Head-to-head evaluation design

**Round 0 — document verification:** Pin versions, supported OS, license, model auth and billing, plugin provenance, required services and dependencies. Fail any candidate that cannot run legally or safely under an authorized test identity.

**Round 1 — same-model harness comparison:** Run Claude Agent SDK, Pi-with-Claude and OpenCode-with-Claude on the same 3–5 disposable coding fixtures, pinned model when supported, identical permitted tools/data/checks/budgets. Record deviations: native prompt/context/tool semantics mean even same-model comparisons are not perfect controlled experiments.

**Round 2 — portability:** Repeat selected fixture through Codex SDK, and Pi/OpenCode with a second approved model; optionally local LM Studio on read-only task. Mark unavailable features explicitly, never silently emulate them.

**Round 3 — coordinator:** Compare minimal SQLite coordinator with OpenClaw→Claude/other harness dispatch; optionally OpenHands remote worker. Force crash/resume, unknown external effects, denied network/path access, session visibility tests and budget exhaustion.

**Round 4 — learning:** Capture outcome/evaluation data and test a **reviewed** prompt/skill change on held-out tasks; no self-modifying permissions, no online policy RL.

Score each candidate on task acceptance (25%), independent security/isolation (25%), integration and extensibility (15%), portability (15%), recovery/evidence (10%), and operational cost/complexity (10%). Scores remain **unassigned** until tested; no vendor should win from feature-count alone.

## Decision / nondecision

- **Decision now:** Add Pi and OpenCode as equal harness finalists with Claude SDK. Add OpenClaw as a coordinator finalist and OpenHands as serious sandbox-oriented alternative.
- **Do not decide yet:** Whether Pi replaces Claude SDK; whether OpenClaw is required; whether a workflow engine is needed.
- **Selection gate:** At least one native-Claude and one second-provider test, plus negative security/recovery tests. The POC can remain Claude-first operationally while the **architecture selection stays open**.
