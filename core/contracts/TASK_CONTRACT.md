# Task Contract

Owner of task semantics; implements references to STD-01, STD-03, STD-05, STD-06 in the [standard](../standards/ENGINEERING_STANDARD.md). A contract may be a short request or repository record. Formal documents are unnecessary for trivial work.

## Required fields (material tasks)

These are required *semantics*, not mandatory form fields: a short interactive request may express them in prose.

| Field | Meaning |
| --- | --- |
| Objective | Observable intended outcome |
| Scope | Included and excluded work |
| Constraints | Technical, data, dependency, compatibility, and process limits |
| Acceptance criteria | Observable conditions that a reviewer can assess |
| Authority boundaries | Permitted modifications and actions; actions reserved for authorization |

For material work, make these semantics identifiable even when expressed in prose.

## Conditional fields

Use risk and autonomy when permissions or consequences need clarification; project revision when reproducibility or concurrent changes matter; dependencies when work relies on systems, people, or prerequisites; budget when time, cost, or resource limits matter; approval and escalation when a decision, blocked check, exception, or consequential action needs an authorizer. Complexity and workflow can be recorded to explain process choice. A missing conditional field does not authorize an action.

## Invariants

- The task does not authorize changes outside its stated scope or boundaries.
- Material scope expansion and consequential actions require applicable authorization.
- Acceptance criteria remain distinguishable from implementation steps.
- Conditional-field omission never creates permission or overrides higher-priority obligations.

## Example

Objective: Correct parser handling of empty input. Scope: parser and focused tests only; no API redesign. Constraints: retain existing dependency set. Acceptance criteria: empty input produces the documented result and focused regression checks pass. Authority boundaries: local edits and tests only; no merge or release. Context: S/A1/T1, Standard; record the actual starting revision before editing. Escalate incompatible API behavior to the maintainer.

Use the [task template](../templates/TASK.md) and [completion contract](COMPLETION_CONTRACT.md) for results.

The [optional structured Task schema](../controls/schema/task.schema.json) represents these semantics when a JSON record is used; it does not make the template mandatory.
