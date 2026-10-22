# Completion Contract

Canonical owner of execution, acceptance, and verification status vocabulary. References STD-06, STD-07, STD-14, STD-15 in the [standard](../standards/ENGINEERING_STANDARD.md).

## Execution state

| State | Meaning |
| --- | --- |
| Completed | Authorized implementation scope and essential execution criteria fulfilled; acceptance can remain pending |
| Partial | Useful work exists but scope or an essential criterion remains unmet |
| Blocked | Progress requires missing authority, input, capability, or dependency |
| Rejected | Proposed execution result was declined and will not proceed in its current form |
| Canceled | Work intentionally stopped without a completion claim |

## Acceptance state

| State | Meaning |
| --- | --- |
| Pending review | Responsible reviewer has not accepted the result |
| Accepted | Responsible human or explicitly approved bounded automation policy accepted the result |
| Changes requested | Review requires revision |
| Rejected | Reviewer declined the proposed result |
| Not applicable | No acceptance decision applies; explain why, such as an abandoned exploration |

Completed does not mean Accepted. Accepted does not mean Merged. Merged does not mean Released. Record merge and release independently using actual repository/platform evidence, or state “not performed” or “unknown.” Local completion never implies authorization for those actions. Rejected has separate meanings in the two state dimensions; label each explicitly.

## Verification status

| Status | Meaning |
| --- | --- |
| Passed | Executed check met its stated criteria |
| Failed | Executed check did not meet its stated criteria |
| Not run | Known check was not executed; state why |
| Not applicable | Check does not apply; explain why |
| Unverified | A relevant claim has insufficient or uncertain evidence |

## Required fields (material completion reports)

- Objective and scope delivered
- Execution state and separate acceptance state
- Verification checks, their actual status, and supporting evidence or method
- Remaining material limitations or outstanding criteria
- Next safe action or disposition

For each check, record the command or review method, revision/context, actual result, and material limitations. A concise interactive report is sufficient for low-risk work.

## Conditional fields

Include deferred work, recovery/continuation information when unfinished, and merge or release evidence when either action is relevant. State **not performed** or **unknown** rather than inferring external actions. Include approval, cost, or operational evidence only when material to the task or risk profile.

## Invariants

- Completed does not imply Accepted; Accepted does not imply Merged; Merged does not imply Released.
- Tool output and editorial review are different evidence types; structural validation does not prove policy correctness.
- If an essential execution criterion is unverified, report Partial or Blocked rather than Completed.
- Do not conceal failed or unrun checks in an otherwise positive completion summary.
- Human acceptance may remain Pending review after implementation is complete.

## Example

Execution: Completed (parser fix and regression test implemented). Acceptance: Pending review. Verification: `python3 -m unittest tests.test_parser` — Passed on the recorded working revision; broader suite Not run due to unavailable service. Limitation: service integration behavior Unverified, outside the agreed local task criteria. Merge: not performed. Release: not performed. Next: maintainer reviews the diff and decides whether broader checks are needed before integration.

The [optional structured Completion schema](../controls/schema/completion.schema.json) uses these exact status values and keeps merge and release independent of acceptance.
