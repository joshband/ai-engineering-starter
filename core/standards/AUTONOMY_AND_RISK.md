# Autonomy and Risk

This file owns four independent classifications. [Policy](ENGINEERING_STANDARD.md) determines obligations, not a label alone. Record the dimensions separately and reassess when scope or consequences change.

## Risk profiles

| Code | Profile | Examples |
| --- | --- | --- |
| L | Low-risk local | Isolated reversible fixes, prototypes, documentation, synthetic data |
| S | Shared or consequential | Shared repositories, user-facing changes, APIs, significant dependencies, customer deliverables |
| H | High-risk | Production access, restricted information, destruction, security-sensitive operations, financial effects, unattended consequential execution |

Classify actual consequences, including downstream automation. Team size is irrelevant. Classify local editing and later release separately when their consequences differ; use the stronger profile for any workflow that includes the consequential action.

## Autonomy levels

| Code | Authority |
| --- | --- |
| A0 — Advisory | Analyze and recommend without modification |
| A1 — Bounded execution | Modify authorized local working state |
| A2 — Supervised workflow | Execute multiple stages subject to approval boundaries |
| A3 — Delegated routine operation | Explicitly preauthorized recurring or unattended tasks |
| A4 — High-consequence autonomy | Exceptional sensitive operations under stronger controls |

A1/A2 are the design center. A4 is excluded from the default starter profile. A level describes delegated authority; it never grants authority by itself. A3 requires explicit preauthorization; it is not permission to create recurring operations.

## Task complexity

| Code | Scope |
| --- | --- |
| T0 — Trivial | Small, obvious, reversible work |
| T1 — Bounded | Limited defect, feature, localized refactor |
| T2 — Complex | Multiple components, uncertainty, architecture choices, important dependencies |
| T3 — Extended | Long-running migrations, multi-system or operational complexity |

## Workflow profiles

Quick minimizes process for trivial L work; Standard covers bounded work; Structured adds explicit discovery and staged plans; Controlled adds consequence-specific approvals, isolation, operational evidence, and recovery. The [workflow guide](../workflows/PROFILES.md) owns selection and procedures.

## Independent dimensions in practice

| Scenario | Risk | Autonomy | Complexity | Workflow |
| --- | --- | --- | --- | --- |
| Correct a local draft typo | L | A1 | T0 | Quick |
| Fix shared API behavior locally | S | A1 | T1 | Standard |
| Investigate a broad local architecture alternative | L | A0 | T2 | Structured |
| One-line documentation merge that automatically deploys production | H for merge/release; editing can be L | A1 for edit; merge not authorized by that | T0 editing | Controlled for consequential action |
| Approved recurring financial operation | H | A3 only within explicit authorization | T1 or higher | Controlled; operation not supplied by M1 |

Select the workflow using risk and complexity, then constrain it by actual authority. Complexity cannot lower approval needs; risk does not force elaborate planning for a simple action. Fast/Standard/Deep/Local model workload labels are optional selection vocabulary, separate from all four dimensions and from workflow names. No model class changes permissions.
