# M1 and M2 Acceptance Matrix

M1 was accepted by the maintainer and merged in PR #1 on 2026-10-22. M2 implementation is a v0.2.0 candidate; responsible human acceptance: Pending review. Implementation-side editorial assessment is not final acceptance. Status vocabulary is owned by the [completion contract](../core/contracts/COMPLETION_CONTRACT.md).

## M1 structural validation

Run `python3 validation/validate.py` from the distribution root. The original M1 structural checks run before M2 checks. Python standard library only; no packages or services. Adoption does not require Python. Exit 0 means all implemented structural checks Passed; nonzero means Failed.

The M1 portion checks required paths, canonical STD headings and location, recognized policy IDs, inline relative file links and basic ATX heading fragments, task/handoff/exception fields, exact completion status tables, separate classification headings, and narrow project/credential markers. It does not parse arbitrary Markdown, reference-style links or HTML, validate external URLs, detect all secrets, prove policy consistency, or test agent/security behavior. M1 itself had no structural control fixtures or enforcement.

## Requirements

| Requirement | Verification method | Implementation-side assessment and limit |
| --- | --- | --- |
| File completeness | Automated path list | Passed; 19 required documents plus optional checker |
| One canonical definition per STD | Automated heading count/location; editorial ownership review | Passed; semantic duplication needs editorial judgment |
| No contradictory normative definitions | Editorial comparison of all documents to supplied M1 policies | Passed in implementation review; human acceptance pending |
| Documentation links | Automated inline links and supported fragments | Passed in source layout; relocate template links during adoption |
| Task contract completeness | Automated fields; editorial meaning | Passed; required and conditional semantics distinguished |
| Workflow and classification consistency | Automated taxonomy headings; editorial scenario/profile/lifecycle review | Passed; four dimensions and eight checkpoints remain distinct |
| Small change with high operational risk | Editorial taxonomy example | Passed; production-triggering one-line edit included |
| Completion and acceptance separation | Automated vocabulary; editorial state transitions | Passed; merge and release independent |
| Consistent verification status | Automated exact status tables; editorial reporting | Passed; actual evidence required |
| No mandatory vendor lock-in or service | Editorial requirements and adoption review | Passed; no mandatory agent, provider, gateway, or infrastructure |
| No unnecessary solo ceremony | Editorial Quick, adoption, and policy review | Passed; no universal branch, PR, task form, separate reviewer, or container |
| No unimplemented enforcement claims | Editorial README and security review | Passed; instructions, settings, hooks, CI, protections, isolation, authorization distinguished |
| No private project content | Narrow automated marker scan; editorial provenance review | Passed for newly authored content; no private source accessed; not comprehensive secret detection |
| Incremental existing-repository adoption | Editorial adoption review | Passed; inventory then merge; no automatic replacement |
| Architecture fidelity | Editorial ADR-001–ADR-006 and ownership review | Passed; portable policy, project context, adapters, external governance distinct |
| Normative strength | Editorial STD comparison | Passed; conditional MUST, recommended SHOULD, optional MAY preserved |
| No scope expansion | File inventory and final diff review | Passed in implementation review; no later milestones |
| Whitespace | `git diff --cached --check` in local review repository | See execution evidence in accompanying report |
| Runtime controls and specific agent compatibility | Outside M1 | Not applicable to M1 implementation; guarantees Unverified |
| Human acceptance | Maintainer acceptance and merged PR #1 | Passed for M1; M2 remains Pending review |

## Editorial review procedure

Read standard, taxonomy, contracts, workflows, templates, adoption, and security guidance. Compare each policy's conditions and strength with the supplied specification. Confirm that examples do not add authority and templates do not duplicate normative requirements. Inspect the final diff for unnecessary files and accidental content. Evaluate both low-risk solo use and consequential work. Passing structural checks and an implementation-side editorial review do not constitute responsible human acceptance.

## Execution evidence

The M1 review recorded commands and results; this file now documents M2 checks. Re-run after edits. No adapters, enforcement mechanisms, CI/CD, runtime isolation controls, or later-milestone features are supplied or tested.

## M2 candidate checks

Run `python3 validation/validate_controls.py` to validate the catalog, schema subset, drift assertions, and all fixtures; run `python3 -m unittest discover -s validation/tests -v` for targeted regression tests. `python3 validation/validate_controls.py --contract task path/to/record.json` validates an individual raw record (or omit `--contract` to supply fixture envelopes). Nonzero errors include the failing JSON path.

| Requirement | Method | Implementation assessment and limit |
| --- | --- | --- |
| M1 remains valid | Original checks at the start of `validation/validate.py` | Passed locally; repository artifact unchanged except entry point and acceptance metadata |
| Sixteen controls and source strength labels | Catalog shape, coverage and heading/label comparison | Passed structurally; clause topics and scope require editorial review |
| No conflicting normative definition | Review catalog descriptions against accepted standard | Implementation review found no intended changes; human M2 review pending |
| Four contract schemas | Schema declaration/keyword audit and instance validation | Passed for documented subset; not a full JSON Schema meta-schema validator |
| Required and conditional semantics | Valid/invalid fixture pairs for material task, approval, exception, and completion | Passed for encoded conditions; applicability and authority are human-assessed |
| Exact status vocabulary | Compare M1 completion tables to completion/handoff schema enums | Passed; cannot establish whether a reported check ran |
| Positive fixtures | Expected manifest and exact zero-error check | Passed; 9 valid fixtures |
| Negative fixtures | Exact expected code and JSON path, with no unrelated errors | Passed; 13 negative fixtures |
| Material Profile H exception trigger only | Positive H/nonmaterial and S/material; negative H/material; unit regression | Passed for structured records; cannot evaluate materiality or authorizer authority |
| Structural drift | Canonical policy IDs/titles/labels, catalog coverage, status enum checks, fixture manifest | Passed; prose-equivalence remains Unverified automatically |
| Minimal Quick/no service | No-record fixture and review of dependencies | Passed; no installation or structured task file required |
| Vendor neutrality and no enforcement claims | Review files and security boundaries | Passed in implementation review; compatibility and controls Unverified |
| Human M2 acceptance | Responsible architecture/policy review of PR | Not run; Pending review |

The [traceability matrix](control-traceability.md) lists every control and what must still be judged by a person. The structural validator does not establish schema correctness under the complete Draft 2020-12 specification, policy semantic equivalence, authorization, data permissions, security isolation, or operational evidence validity.
