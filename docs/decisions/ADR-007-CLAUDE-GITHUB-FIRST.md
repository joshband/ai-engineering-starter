# ADR-007 — Claude + GitHub first; preserve portable architecture

**Status:** Proposed for maintainer review (implementation direction documented 2026-10-23); **not merged or ratified**.  
**Supersedes:** No canonical M1 standards or original ADR summaries.  
**Related:** [Approved-tooling profile](../roadmap/APPROVED_TOOLING_PROFILE.md), [M10 execution plan](../roadmap/M10_EXECUTION_PLAN.md), [Phase D/E research](../research/phase-d-e/README.md).

## Context

M1–M9 established a portable engineering foundation, including native Claude and Codex entry points, shared standards/contracts and optional skills. M6 target verification and M8 runtime testing are unfinished; M4 Codex-native instruction discovery is deferred. Follow-on research compared Claude Agent SDK, Pi, OpenCode, OpenClaw and independent orchestration systems but no comparative runtime experiment has selected a winner.

For the **current** working environment only Claude and GitHub are approved tools. Future private, open, or unconstrained environments may permit Codex, local inference or other harnesses. Building a custom coordinator now would add dependencies, credentials, maintenance and uncertain benefit before native Claude/GitHub effectiveness is measured.

## Decision proposed

1. **One architecture; two horizons:** M1–M9 core and Phase D/E research remain available. Use Claude + GitHub for the first reference implementation; provider-specific adapters remain optional, not destroyed.
2. **Native-first, evaluation-led:** before adding Claude Agent SDK, Pi, another harness or custom orchestration, compare native Claude Code with and without minimal portable workflow guidance.
3. **GitHub as project record/control plane:** issue/PR/review/Actions where independently approved, not as a guaranteed execution sandbox; maintain completion, verification, acceptance, merge and release as distinct states.
4. **Thin by default:** no new coordinator, provider gateway, queue, policy engine or hosted agent infrastructure in M10 unless a documented, repeatable requirement fails existing capabilities and risk/cost tradeoffs justify it.
5. **Reviewed improvements:** use observed task outcomes and deterministic tests to propose skill/standard improvements through human-reviewed PRs, never autonomous approval/promotion.
6. **Retain dormant alternatives:** do not delete Codex adapter or Phase D/E evaluations; refresh alternatives only when new authorization or a demonstrated unmet requirement creates decision value.

## Alternatives and why not selected now

| Option | Judgment now | When to revisit |
| --- | --- | --- |
| Claude-only bespoke coordinator | Unnecessary complexity without observed gap | Repeatable failed native recovery/approval need |
| Claude Agent SDK from day one | Useful for embedding but extra SDK auth/runtime and observability burden | Need a programmatic session-control contract native Code cannot satisfy |
| Pi or OpenCode primary harness | May increase multi-provider flexibility, but not currently approved | Second provider permitted + equal-task comparison |
| OpenClaw gateway | Valuable for always-on remote dispatch; larger security/operations footprint | Approved remote/recurring workflow plus independent host isolation tests |
| LangGraph/Temporal/DBOS/Mastra/Pydantic AI | Durable orchestration should be demand-driven | Evidence of resumability/reconciliation gap |
| Discard multi-provider architecture | Rejected: destroys optionality and prior investment | Not appropriate |
| **No custom harness or coordinator** | **Acceptable outcome** | If native Claude + GitHub meets measured requirements |

## Consequences

**Positive:** Faster useful pilot; smaller trusted computing base; better integration with existing GitHub review; less risk of maintaining duplicated Claude features.  
**Trade-offs:** Initial executable path is Claude-specific. Cross-provider compatibility remains a design and fixture claim until verified, not an achieved runtime claim. GitHub does not enforce host/network policy by itself.  
**Obligations:** Record model/tool versions, data/credentials limits, acceptance evidence and actual failures; maintain a future activation checklist for provider adapters and coordinator alternatives.

## Reconsideration and deletion gate

Trigger a bounded comparison when (a) a second provider is explicitly approved, (b) native Claude cannot safely recover a reproducible interrupted task, (c) cross-session/recurring orchestration is needed in more than one case, (d) review/evaluation data show another harness materially improves accepted-task quality/effort/cost, or (e) governance needs cannot be met by independently scoped GitHub permissions and existing controls.

A custom coordinator is **not** approved by this ADR; if a future POC does not improve outcomes, remove the experimental component and retain the fixture and evidence. Evaluate alternatives against security, total cost and maintenance, not just features.

## Source and evidence limits

This is an **architecture proposal**, not a claim that current Claude versions, GitHub policy settings, or the pilot are verified. Validate [native feature map](../research/phase-d-e/CLAUDE_NATIVE_CAPABILITIES.md) and actual host/runner constraints before promotion to Accepted.
