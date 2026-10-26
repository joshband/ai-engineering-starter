# Skill: Adoption review

**Use:** When asked to evaluate an established repository against this starter and recommend improvements. Analysis only (A0): do not modify the target repository until the user approves a specific recommendation. A single paste-able version for sessions without this starter installed is in [the adoption review prompt](../../docs/ADOPTION_REVIEW_PROMPT.md).

**Read:** [Adoption decision kit](../../docs/adoption-decision/README.md), [taxonomy](../../core/standards/AUTONOMY_AND_RISK.md), [workflow profiles](../../core/workflows/PROFILES.md), [completion contract](../../core/contracts/COMPLETION_CONTRACT.md), and applicable [M1 standard](../../core/standards/ENGINEERING_STANDARD.md).

## Procedure

1. Inventory the target using the [decision kit inventory](../../docs/adoption-decision/INVENTORY.md): build/test/lint commands (run only cheap read-only ones), CI, review practice, existing agent configuration, secrets and dependency handling, docs, and release path. Preserve uncommitted work and never print secrets.
2. Classify actual consequence risk (L/S/H), autonomy (A0–A4), and complexity (T0–T3); choose the lightest fitting workflow profile.
3. Rate each STD-01–STD-16 as Met, Partial, Gap, or Not applicable, citing a file or command you actually ran; mark unverified items as such. The target's existing conventions stay authoritative.
4. Note what the target does better than this starter.
5. Recommend, ranked and reversible: what, why (STD ID plus evidence), effort, risk, rollback, and whether approval is needed. Use the [decision matrix](../../docs/adoption-decision/DECISION_MATRIX.md) outcome (No adoption, Reference only, or Selective adoption) and the [rollback guide](../../docs/adoption-decision/ROLLBACK.md).

## Output

A concise report with classification, STD ratings, ranked recommendations, a minimal adoption path using imports or pointers rather than copies, and open questions. Then stop. Do not apply changes, and do not treat this skill or a recommendation as authorization.
