# M9 — Usability and documentation consolidation

**Status:** Documentation-only implementation candidate for human review. No human acceptance, merge, tag, or release authorized.

## Why

The repository has a canonical standard, optional structured controls, two agent adapters, five optional skills, and a manual adoption kit. New readers need a concise decision path and accurate status reporting without another policy layer. The root README still described M7 as a pending candidate after PR #6 merged; this candidate corrects that stale navigation.

## In scope

- One [reader-first entry guide](START_HERE.md) mapping common situations to existing authoritative files.
- One [capability/evidence map](CAPABILITY_STATUS.md) distinguishing accepted, provisional, deferred, and candidate states.
- Update root README navigation and stale M7 status.
- A small link from the existing adoption guide to the new navigation.
- Read-only deterministic link/anchor and whitespace checks where available; human review for clarity, duplication, and policy semantics.

## Out of scope

No edits to STD-01–STD-16, taxonomy, contracts, agent instruction entry points, schemas, permission files, hooks, CI, installers, target repositories, M8 runtime testing, release or tag. No new mandatory forms or policies.

## Acceptance criteria

1. A new reader can choose Quick, Standard, existing-repo adoption, or an adapter in two navigation steps or fewer from README.
2. M1 remains sole normative STD owner; M2/M5/M7 are optional where specified.
3. The capability matrix correctly separates observed structural, discovery, behavioral, and enforcement evidence and labels M4/M6/M8 limitations.
4. M7 is accurately marked accepted/merged; M9 remains a candidate until explicit human decision.
5. All new relative paths and anchors resolve, and existing deterministic tests and diff whitespace check pass when executed.
6. Human review confirms the pages are useful navigation rather than duplicated policy; no merge or release without authorization.

## Review gate

Review this documentation candidate and actual verification evidence; decide Accept, Revise, or Reject. Do not infer runtime behavior from documentation checks.
