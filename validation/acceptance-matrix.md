# M1–M4 Acceptance Matrix

M1 was accepted by the maintainer and merged in PR #1 on 2026-10-22. M2 was accepted following architecture/policy review and squash-merged in PR #2 on 2026-10-22 (commit dcf7e41ce1553dd5ea4138c99c0bae46495a7db2); no release tag was created. M3 was accepted following bounded instruction-discovery smoke testing and squash-merged in PR #3 on 2026-10-22 (commit 291e2d0bff2fb99cee784a599630a9721701d762). Implementation-side editorial assessment is not final acceptance. Status vocabulary is owned by the [completion contract](../core/contracts/COMPLETION_CONTRACT.md).

M4 implementation is Completed per the submitted PR #4 report, provisionally accepted for architecture and structural validation, and squash-merged in PR #4 on 2026-10-22 (commit b460c1dddfe48751eced8f50e3a5bcdc6a086321). Live Codex discovery remains Unverified and is explicitly deferred to [the M4 runtime follow-up](m4-codex-runtime-followup.md). No tag or release is implied.

## M1 structural validation

Run `python3 validation/validate.py` from the distribution root. The original M1 structural checks run before M2 checks. Python standard library only; no packages or services. Adoption does not require Python. Exit 0 means all implemented structural checks Passed; nonzero means Failed.

The M1 portion checks required paths, canonical STD headings and location, recognized policy IDs, inline relative file links and basic ATX heading fragments, task/handoff/exception fields, exact completion status tables, separate classification headings, and narrow project/credential markers. It does not parse arbitrary Markdown, reference-style links or HTML, validate external URLs, detect all secrets, prove policy consistency, or test agent/security behavior. M1 itself had no structural control fixtures or enforcement.

## Requirements

| Requirement | Verification method | Implementation-side assessment and limit |
| --- | --- | --- |
| File completeness | Automated path list | Passed; 19 required documents plus optional checker |
| One canonical definition per STD | Automated heading count/location; editorial ownership review | Passed; semantic duplication needs editorial judgment |
| No contradictory normative definitions | Editorial comparison of all documents to supplied M1 policies | Passed in implementation review; human acceptance completed |
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
| Human acceptance | Maintainer acceptance and merged PR #1 | Passed for M1 and M2; M2 acceptance followed architecture/policy review |

## Editorial review procedure

Read standard, taxonomy, contracts, workflows, templates, adoption, and security guidance. Compare each policy's conditions and strength with the supplied specification. Confirm that examples do not add authority and templates do not duplicate normative requirements. Inspect the final diff for unnecessary files and accidental content. Evaluate both low-risk solo use and consequential work. Passing structural checks and an implementation-side editorial review do not constitute responsible human acceptance.

## Execution evidence

The M1 review recorded commands and results; this file documents M2–M4 checks. Re-run after edits. M3/M4 add instructions only; no enforcement mechanisms, CI/CD, runtime isolation controls, or later-milestone features are supplied or tested.

## M2 structural checks

Run `python3 validation/validate_controls.py` to validate the catalog, schema subset, drift assertions, and all fixtures; run `python3 -m unittest discover -s validation/tests -v` for targeted regression tests. `python3 validation/validate_controls.py --contract task path/to/record.json` validates an individual raw record (or omit `--contract` to supply fixture envelopes). Nonzero errors include the failing JSON path.

| Requirement | Method | Implementation assessment and limit |
| --- | --- | --- |
| M1 remains valid | Original checks at the start of `validation/validate.py` | Passed locally; repository artifact unchanged except entry point and acceptance metadata |
| Sixteen controls and source strength labels | Catalog shape, coverage and heading/label comparison | Passed structurally; clause topics and scope require editorial review |
| No conflicting normative definition | Review catalog descriptions against accepted standard | Implementation review found no intended changes; human M2 review completed |
| Four contract schemas | Schema declaration/keyword audit and instance validation | Passed for documented subset; not a full JSON Schema meta-schema validator |
| Required and conditional semantics | Valid/invalid fixture pairs for material task, approval, exception, and completion | Passed for encoded conditions; applicability and authority are human-assessed |
| Exact status vocabulary | Compare M1 completion tables to completion/handoff schema enums | Passed; cannot establish whether a reported check ran |
| Positive fixtures | Expected manifest and exact zero-error check | Passed; 9 valid fixtures |
| Negative fixtures | Exact expected code and JSON path, with no unrelated errors | Passed; 13 negative fixtures |
| Material Profile H exception trigger only | Positive H/nonmaterial and S/material; negative H/material; unit regression | Passed for structured records; cannot evaluate materiality or authorizer authority |
| Structural drift | Canonical policy IDs/titles/labels, catalog coverage, status enum checks, fixture manifest | Passed; prose-equivalence remains Unverified automatically |
| Minimal Quick/no service | No-record fixture and review of dependencies | Passed; no installation or structured task file required |
| Vendor neutrality and no enforcement claims | Review files and security boundaries | Passed in implementation review; compatibility and controls Unverified |
| Human M2 acceptance | Responsible architecture/policy review of PR | Passed; accepted following architecture/policy review, PR #2 squash-merged |

The [traceability matrix](control-traceability.md) lists every control and what must still be judged by a person. The structural validator does not establish schema correctness under the complete Draft 2020-12 specification, policy semantic equivalence, authorization, data permissions, security isolation, or operational evidence validity.

## M3 candidate checks

Run `python3 validation/validate.py` and `python3 -m unittest discover -s validation/tests -v`. The M3 unit tests check the root CLAUDE imports, M2 task/completion/approval cases, missing/malformed record handling, and the validator's operation without an optional Claude Code executable on PATH. These are deterministic structural tests, not a Claude Code integration test.

| Requirement | Method | Implementation assessment and limit |
| --- | --- | --- |
| M1/M2 regression | Existing combined validator and unit suite | Passed locally before and after M3 changes |
| Instruction discovery paths | Parse root CLAUDE imports and resolve target files | Passed structurally; root and both imports observed in `/context` during bounded cloud-session smoke test |
| Single policy authority | Confirm canonical imports and no STD headings in adapter | Passed structurally; M3 editorial review completed at acceptance |
| Quick without ceremony | M2 no-record fixture and adapter instruction review | Passed in implementation review; actual agent response Unverified |
| Material task reporting | M2 task and completion schemas/fixtures plus guidance review | Passed structurally; quality of reported evidence requires review |
| High-risk escalation | Pending-approval fixture and missing-boundary failure plus instruction review | Passed structurally; actual escalation behavior Unverified |
| Missing/invalid structured records | M2 negative fixture checks; missing/malformed JSON read tests | Passed; optional records are not a universal requirement |
| Optional feature unavailable | Validator subprocess with empty PATH; no settings/hooks shipped | Passed locally; bounded Claude instruction discovery separately observed |
| Incremental adoption and removal | Editorial review of [adapter guide](../adapters/claude-code/README.md) | Passed in implementation review; target repositories vary |
| Runtime integration | `claude` executable discovery; bounded smoke if available | Instruction discovery Passed in cloud session; `/status`, live permissions, prompt adherence, and broader compatibility Unverified |
| M3 human acceptance | Responsible architecture/security review of draft PR | Passed for bounded instruction discovery; M3 accepted and squash-merged in PR #3 |

The adapter's imports are instructions in model context. The static suite does not verify Claude Code permission modes, prompt adherence, actual instruction loading, hooks, sandboxing, or action authorization. No hook or project permission file is installed.

## M4 candidate checks

Run `python3 validation/validate.py`, `python3 -m unittest discover -s validation/tests -v`, and `git diff --check` from the repository root. The M4 tests inspect static paths and semantics, invoke the M2 validator for optional record cases, and confirm the Claude entry point remains intact. They do not run Codex or enforce agent permissions.

| Requirement | Method | Candidate assessment and limit |
| --- | --- | --- |
| M1–M3 regression | Existing combined validator and unit suite | Run and report actual results in PR; accepted source definitions unchanged |
| Codex discovery path | Root `AGENTS.md` presence and no root override; path resolution test | Static path Passed when tests pass; live Codex discovery Unverified until smoke tested |
| Canonical M1/M2 references | Parse links and catalog path, check no STD definition headings | Structural checks only; editorial policy consistency still required |
| Quick no record | Adapter wording and M2 no-record fixture | No universal form; live prompt behavior Unverified |
| Material task and completion | M2 task/completion cases and entry-point references | Shape/status checks; materiality and evidence remain human assessed |
| High-risk escalation | Pending-approval and missing-boundary cases, entry-point guidance | Structural condition only; actual approval boundary Unverified |
| Optional missing/invalid records | Absent/malformed JSON and M2 record errors | Report failures; no record required merely for Quick |
| Claude coexistence | Both native root files and import targets remain present | Static integrity only; cross-runtime loading must be observed |
| Incremental adoption/removal | Editorial review of [Codex guide](../adapters/codex/README.md) | Existing files preserved; target-specific conflicts still require review |
| Permissions and security | Confirm no runtime config, rule, hook, or bypass shipped; review [security boundaries](../docs/SECURITY_BOUNDARIES.md) | Instructions and validators do not enforce authority |
| No later milestone | Final diff inventory | No skills, routing, orchestration, service, or CI added |
| Runtime smoke | `codex` availability and bounded read-only discovery run if available | Report observed output or Unverified explicitly |
| M4 human acceptance | Responsible architecture and security review of draft PR | Pending review; merge and release reserved |

Reviewers should confirm that the two native entry points route to one shared standard, that SHOULD remains conditional, that a risk label or `adapter_candidate` never grants permission, and that no static result is called runtime enforcement. A real Codex discovery check, if later available, should record version, active instruction files, prompt, settings context, and observed output.

## M5 reusable skills candidate checks

M5 adds five opt-in skill procedures under [skills](../skills/README.md). They are reference workflows, not auto-discovered native agent skills, runtime permissions, or new normative requirements. M1 remains the sole STD policy owner.

| Requirement | Verification method | Current evidence / limit |
| --- | --- | --- |
| Skill inventory | Inspect five SKILL.md files and index | Passed by GitHub tree inspection (2026-10-22) |
| Canonical links | Resolve Markdown links within skill library against branch tree | Passed independently: 32 relative links, 0 broken (2026-10-22) |
| No duplicated STD headings | Inspect new skill Markdown | Passed by structural scan; semantic consistency still needs reviewer judgment |
| Quick remains lightweight | Inspect task intake and verification procedures | Passed editorial review; no required Quick form |
| Exception authority and Profile H | Inspect exception procedure against STD-16 | Passed editorial review; conditional trigger preserved; no self-authorization |
| Acceptance vs execution/merge/release | Inspect review and verification procedures | Passed editorial review; states remain distinct |
| M5 regression tests | `python3 -m unittest discover -s validation/tests -v` | **Not run** against complete checkout in this connector-only session; new test_skills.py added |
| M1–M4 regression validator | `python3 validation/validate.py` | **Not run** against complete checkout in this connector-only session |
| Whitespace | `git diff main...HEAD --check` | **Not run** locally; GitHub diff review does not substitute for command |
| Native Claude/Codex skill discovery | Live integration test | **Unverified**; no automatic installation or discovery implemented by M5 |
| Human acceptance | Maintainer review of verified candidate | Pending review until required checks are run and evidence reviewed |

**Current state:** Execution Partial (required Python/whitespace verification pending); Acceptance Pending review. No merge, release, or M6 work.
