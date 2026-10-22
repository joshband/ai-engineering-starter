# Capability and evidence map

**Snapshot:** 2026-10-22. This is a maintainer-facing status summary, not a new policy or a claim of runtime guarantees. Consult the linked milestone evidence for current disposition.

| Milestone | Delivered capability | Acceptance / evidence boundary |
| --- | --- | --- |
| M1 | [Canonical standard](../core/standards/ENGINEERING_STANDARD.md), taxonomy, workflows and prose contracts | Accepted and merged; only normative STD owner |
| M2 | [Control catalog and optional record schemas](../core/controls/README.md), deterministic checks | Accepted and merged; structural validity does not grant authority |
| M3 | [Claude Code adapter](../adapters/claude-code/README.md) | Accepted and merged; one bounded cloud discovery observation, not universal adherence |
| M4 | [Codex adapter](../adapters/codex/README.md) | Provisionally accepted and merged; [native runtime follow-up](../validation/m4-codex-runtime-followup.md) open |
| M5 | [Five optional skill procedures](../skills/README.md) | Accepted and merged; no automatic invocation |
| M6 | [Copy That documentation pilot](M6_PILOT_PLAN.md) | Partial verification; full target checks and adoption acceptance deferred |
| M7 | [Minimal adoption decision kit](adoption-decision/README.md) | Accepted and merged in [PR #6](https://github.com/joshband/ai-engineering-starter/pull/6); manual guidance, not installer |
| M8 | [Runtime validation proposal](https://github.com/joshband/ai-engineering-starter/blob/m8/runtime-validation-plan/docs/M8_RUNTIME_VALIDATION_PLAN.md) | Planning branch only; runtime tests deferred pending Claude Code / Codex access |
| M9 | [Usability navigation](START_HERE.md) and [candidate plan](M9_USABILITY_PLAN.md) | Accepted and merged in [PR #7](https://github.com/joshband/ai-engineering-starter/pull/7); documentation guidance, not runtime validation |

## Evidence levels

- **Structural:** files, schemas, relative links, and deterministic tests validate documented structure.
- **Discovery:** a specific agent session reports instructions actually loaded. A link that an agent opens on request is not proof of automatic loading.
- **Behavior:** observed response or workflow execution in a named session; cannot be generalized automatically.
- **Enforcement:** permissions, sandbox, approvals, and release controls must be established by actual independent runtime/project controls, not Markdown.

**Unverified is not Failed and not Passed.** A deferred test does not retroactively invalidate an accepted documentation capability. Human acceptance, merge, tag, and release are separate decisions.

For a practical entry path see [Start here](START_HERE.md); for adoption see [ADOPTION](ADOPTION.md).
