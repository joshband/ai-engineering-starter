# M1 Acceptance Matrix

Candidate implementation; responsible human architecture/policy acceptance: Pending review. Implementation-side editorial assessment is not final acceptance. Status vocabulary is owned by the [completion contract](../core/contracts/COMPLETION_CONTRACT.md).

## Structural validation

Run `python3 validation/validate.py` from the distribution root. Python standard library only; no packages or services. Adoption does not require Python. Exit 0 means the structural checks Passed; exit 1 means Failed.

The script checks required paths, canonical STD headings and location, recognized policy IDs, inline relative file links and basic ATX heading fragments, task/handoff/exception fields, exact completion status tables, separate classification headings, and narrow project/credential markers. It does not parse arbitrary Markdown, reference-style links or HTML, validate external URLs, detect all secrets, prove policy consistency, or test agent/security behavior. No structural control fixtures or enforcement are implemented.

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
| Human acceptance | Responsible reviewer assessment | Not run; Pending review |

## Editorial review procedure

Read standard, taxonomy, contracts, workflows, templates, adoption, and security guidance. Compare each policy's conditions and strength with the supplied specification. Confirm that examples do not add authority and templates do not duplicate normative requirements. Inspect the final diff for unnecessary files and accidental content. Evaluate both low-risk solo use and consequential work. Passing structural checks and an implementation-side editorial review do not constitute responsible human acceptance.

## Execution evidence

The accompanying implementation report records commands and actual results. Re-run checks after edits. No adapters, enforcement mechanisms, CI/CD, runtime isolation controls, or later-milestone features are supplied or tested.
