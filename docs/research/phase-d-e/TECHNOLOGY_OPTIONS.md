# Technology options, trade-offs, and selection

**Research as-of:** 2026-10-22. **Recommendation:** Claude-first workflow; provider-neutral design; **Claude SDK, Pi and OpenCode are unranked harness finalists** pending comparison. Sources are enumerated in [SOURCE_REGISTER](SOURCE_REGISTER.md); no compatibility test has been run.

For the expanded alternatives, risks and proposed head-to-head rubric see [expanded ecosystem review](EXPANDED_ECOSYSTEM_REVIEW.md). For native hooks, skills, plugins, MCP and subagents see [Claude feature parity](CLAUDE_NATIVE_CAPABILITIES.md). The table below preserves the **initial** assessment, superseded where it implies a single predetermined harness.

## A. Agent harnesses

| Harness | Officially documented integration | Selection | Open evidence |
| --- | --- | --- | --- |
| **Claude Agent SDK** | Python/TypeScript programmable Claude Code agent loop with tools, sessions, hooks, permissions, subagents, skills [S01] | **First comparison adapter** because primary workflow uses Claude | Confirm SDK version, exact permission behavior, authentication/usage costs, clean cancellation, and native instructions in local environment |
| **OpenAI Codex SDK** | SDK starts, continues and resumes local Codex threads [S03] | **Second adapter, portability gate**; implement minimal equivalent fixture before calling platform provider-neutral | Test model selection, auth, sandbox/approval capabilities and lifecycle parity |
| **Codex app-server** | Lower-level long-lived streamed events and approvals [S04] | Fallback only if SDK cannot report required events / approval state | Additional protocol and transport surface |
| **LM Studio local API** | Native local API and OpenAI-/Anthropic-compatible endpoints [S05] | Later inference option and offline data-classification experiment | A compatible endpoint does *not* supply full Claude or Codex coding-agent harness; model/tool quality and exposed server must be tested |
| **New generic agent loop** | Agents SDKs can offer tools/handoffs [S13] | **Do not create first** | Reimplements coding-specific tool control, context, and debugging |

**Practical note:** Claude Agent SDK can run in a process controlled by us; it does not transfer authority to our coordinator automatically. The coordinator/worker must constrain actual operations independently of the model's instructions.

### Provider and billing policy

The Claude SDK documentation states third-party developers must not offer unauthorized claude.ai login or rate limits as their app's authentication [S01]. A 2026 Claude Help Center update discusses SDK usage with Claude plans and credits [S02], but account-plan and third-party-product contexts differ. **Do not assume either API-only billing or unlimited subscription reuse**; verify permitted authentication, current entitlements, and actual run charges for this exact prototype before implementation.

For Codex, verify account authorization and billing separately. Never create an unofficial login workaround or promise cross-provider quota avoidance.

## B. Orchestration and durability

| Alternative | Benefits | Costs / risk | Recommendation |
| --- | --- | --- | --- |
| **Small typed state machine + SQLite** | Few dependencies, easy local inspection, file-backed journal | Must write state transitions, recovery, locks, migration, effect reconciliation | **Minimal-coordinator comparison baseline** |
| **LangGraph** | Persisted graph checkpoints, stores, interrupts [S06] | Framework lifecycle and storage complexity; effects still need ledger | Trial only if branching or multi-stage resumes exceed state machine |
| **Temporal** | Durable workflow execution, replay and activity patterns [S07] | Workers/service operational cost, deterministic replay rules | Defer until multi-worker/long-lived reliability is demonstrated as necessary |
| **OpenClaw gateway/ACP** | External coding harness dispatch, bound sessions, remote/channel workflows [S22–S24] | **Tier 1 coordinator alternative**, test against minimal state machine | ACP harness runs on host outside OpenClaw sandbox; scope cross-session visibility [S24–S25] |
| **Provider sessions only** | Native context continuation [S01, S03] | Does not prove task authorization, Git revision match, or side effect outcome | Use for harness continuity but not source of truth |

**Nonnegotiable:** A successful checkpoint does not guarantee an external write happened once. When effects are unknown, reconcile before retrying.

## C. Model routing, gateways and inference

| Candidate | Documented capability | Decision |
| --- | --- | --- |
| **Static, visible routing table** | Proposed local design | **Select first.** Permit models only when approved for data/risk class; then compare quality, latency and cost |
| **LiteLLM** | Multi-provider proxy, budgets, rate limits [S08] | **Deferred gateway evaluation.** Budget enforcement requires correct database/counter configuration; some documented modes can fail open |
| **Direct SDK/provider interface** | Available provider APIs [S01, S03] | Start with this; avoid gateway until provider count/operations justify |
| **LM Studio** | Local models and compatibility APIs [S05] | Later comparison, not a drop-in production fallback |
| **Adaptive model router** | Future learned policy, not a baseline product feature | Defer until held-out, safe evaluation and monitoring exist |

## D. Controls and evidence

| Component | Candidate approach | Source/constraint |
| --- | --- | --- |
| Authentication & GitHub | Minimal GitHub App/token permissions, initially no write identity in agent worker | [S09] |
| Isolation | Separate worker identity, restricted temp worktree, allowlisted process/network; negative boundary tests | Local implementation and test required |
| Cost caps | Preflight estimated reservation + max iterations/time + fail-closed stop | Cannot depend only on gateway/provider telemetry [S08] |
| Observability | Versioned local event log and optional OpenTelemetry GenAI spans, redacted by default | GenAI conventions are in development [S10] |
| Evaluation | Deterministic tests + calibrated human judgments; held-out capability/regression sets | Anthropic agent-evaluation research [S11] |

## E. Relative POC fit (judgment, not benchmark)

| Approach | Simplicity | Provider portability | Control ownership | Recommendation |
| --- | --- | --- | --- | --- |
| Claude SDK/Pi/OpenCode + typed adapter + SQLite | To measure | High *if second adapter passes* | High | **Compare, then choose** |
| OpenClaw + independently restricted coding harness | Medium | Potentially high | Requires host isolation for ACP | **Compare as coordinator** |
| Claude-only orchestration via provider primitives | High initially | Low | Medium | Reject as long-term architecture |
| Framework-first LangGraph coordinator | Medium | Medium–High | High | Conditional backup |
| Temporal-first durable service | Low initial | High | High | Defer until demand |
| Fully custom multi-agent runner | Low | Medium | High but untested | Defer |

## Selection gates

Before choosing a long-term interface, run the **same fixture and human acceptance checks with Claude and Codex**; capture native instruction discovery; inspect actual permission enforcement, cancellation, budgets and privacy. A one-harness successful spike is a useful Claude prototype, **not proof of provider independence**.
