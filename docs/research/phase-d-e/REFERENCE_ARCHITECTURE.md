# Optional execution coordinator — proposed reference architecture

**Design status:** unimplemented reference. Security guarantees require actual host/platform tests.

## Logical architecture

```text
Human maintainer -> authorized Task Contract (M1/M2)
                 -> COORDINATOR: task authority, static routing, limits, state machine
                    |          event journal + effect ledger + evidence index
                    |
                    +-> AgentAdapter [interface only]
                         |-- ClaudeAgentAdapter (finalist)
                         |-- PiAdapter (finalist; multiple models)
                         |-- OpenCodeAdapter (finalist; multiple models)
                         |-- CodexAdapter (native portability baseline)
                         |-- LocalModelAdapter (future; capability-limited)
                    |
                    +-> RESTRICTED WORKER: isolated test worktree + allowlisted tools
                                 no merge/deploy credentials; pinned policy version
                                 |
                                 +-> deterministic tests and diff/scope checks
                                 |
                              verifier evidence / human review
                                 |
                        separately authorized optional draft PR
```

**Coordinator implementation is not selected:** compare lightweight local state machine with OpenClaw as a dispatch/gateway layer. OpenClaw ACP external harnesses are host-executed and are **not wrapped by its sandbox** [S24]; independent worker isolation is required in either option. See [expanded review](EXPANDED_ECOSYSTEM_REVIEW.md).

The coordinator **owns controls and authoritative task states**. The coding harness owns its internal generation and tool loop only within the worker's externally imposed permissions. The shared [engineering standard](../../../core/standards/ENGINEERING_STANDARD.md) and [contract shapes](../../../core/controls/README.md) remain portable.

## Adapter interface contract (illustrative, not committed API)

```text
AgentAdapter:
  describeCapabilities() -> harness, supported tools/events/resume/auth
  preflight(Task, RuntimePolicy) -> Supported | Blocked(reason)
  start(BoundedJob) -> RunHandle
  collectEvents(RunHandle) -> ordered normalized event stream
  cancel(RunHandle) -> cancellation attempt + confirmed/unknown outcome
  inspect(RunHandle) -> observed state, charges when available
  resumeIfSafe(RunHandle, RecoveryDecision) -> RunHandle | Blocked
```

**Never silently emulate unsupported capabilities**. For example, an API-compatible inference endpoint is not automatically a drop-in replacement for Claude Code permission semantics, skill discovery, or full tool execution. A local model may initially support only read-only summarization or test selection.

## Candidate task/run records

- Task: ID, objective, allowed paths and tools, prohibited effects, baseline commit, required checks, approved provider/data class, time/iteration/dollar ceilings, authorizer, expiry.
- Run: task revision, harness/model/version, policy version, worker identity/isolation configuration, costs and checks actually observed, cancellation/result.
- Event: sequence, UTC time, actor, action type, authorization reference, revision, redacted summary, evidence/hash, outcome.
- Effect ledger: intended external action, idempotency/reconciliation key, before-state/target, authorization, dispatched time, **confirmed / denied / unknown** outcome, safe retry rationale.
- Evaluation: task fixture hash, input/desired output, deterministic checks, human rating, cost, human interventions, regressions, confidence and provenance.

Do not expand M2 schemas prematurely; version an optional extension only when a concrete consumer exists.

## State transitions (candidate)

```text
DRAFT -> VALIDATED -> AUTHORIZED -> QUEUED -> RUNNING -> VERIFYING
       -> AWAITING_HUMAN -> ACCEPTED | REVISE | REJECTED

RUNNING/VERIFYING -> FAILED | CANCELLED | PAUSED
PAUSED -> RECONCILING -> QUEUED | AWAITING_HUMAN | FAILED
```

Rules: no agent self-approval; no automatic promotion from Completed to Accepted; no release as a side effect; no resume without checking repo/worktree revisions and unknown effects. Model selection cannot enlarge authority. Permission changes require a new authorized job.

## Trust boundary tests

| Boundary | How independently exercised | Fail condition |
| --- | --- | --- |
| Repository worktree | Try reading/writing outside allowlisted path | Unauthorized file access succeeds |
| Network | Probe unapproved endpoint from worker and all available tool paths | Network restriction bypass |
| Credentials | Worker starts with no GitHub write/deploy/production secrets | Credential appears in env/log/context |
| Files/tool capability | Attempt denied command and alternate shell/MCP routes | Denied operation actually executes |
| Cost & time | Force max iteration/time/spend before additional invocation | New expensive work proceeds |
| Data/provider | Attempt restricted task with unapproved model target | Data sent to unapproved provider |
| Recovery | Terminate worker after an uncertain effect; resume | Blind duplicate external action |
| Human approval | Have agent emit an 'accepted' artifact | State changes without actual human authorization |

A tool hook by itself is insufficient if the worker can bypass it through shell access. Use OS/process/network and credential constraints appropriate to the platform, and test rather than assume their behavior.

## Evaluation-driven improvement interface

Capture all runs but **do not feed raw private prompts or credentials into model training**. A separate improvement proposer reads sanitized, appropriately authorized evaluation records, creates a candidate prompt/skill/route change, and runs a fixed, held-out comparison. A responsible reviewer approves or rejects. Production policy, role permissions, and enforcement boundaries are immutable to the learning component.

See [learning systems](LEARNING_SYSTEMS.md) and [POC tests](POC_EXECUTION_PLAN.md).
