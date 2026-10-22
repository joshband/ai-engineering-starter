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

## Candidate verification — 2026-10-22

Executed from the repository root on the M9 candidate tree:

| Check | Result |
| --- | --- |
| `python3 validation/validate.py` | Passed, exit 0: 19 required files, 42 Markdown files, 256 relative links, 16 canonical STD definitions, 16 controls, five schemas, nine valid fixtures, and 13 intentionally invalid fixtures. |
| `python3 -m unittest discover -s validation/tests -v` | Passed, exit 0: 24 tests. |
| `git diff main...HEAD --check` | Passed, exit 0; no whitespace errors. |
| Focused M9 link/anchor review | Passed: 79 relative links and fragments across five changed Markdown files; zero unresolved. |

The capability map now describes M9 as an implemented, verified candidate awaiting human acceptance. Editorial review found no new STD definitions, mandatory Quick form, or runtime enforcement claim. These structural checks do not establish semantic policy equivalence or live agent behavior. The existing validator still prints a stale M5 acceptance note; M5 was accepted and merged, as recorded in the README and capability map. Updating that older validator message is outside this documentation-only candidate.
