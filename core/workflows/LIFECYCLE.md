# Development Lifecycle

Logical checkpoints, not eight forms or separate agent invocations. [Profiles](PROFILES.md) scale the procedure; [contracts](../contracts/TASK_CONTRACT.md) own task semantics and [completion](../contracts/COMPLETION_CONTRACT.md) owns status vocabulary. Policy IDs refer to the [standard](../standards/ENGINEERING_STANDARD.md).

| Stage | Inputs | Outputs | Exit criterion | Policy references |
| --- | --- | --- | --- | --- |
| 0 — Intake | Request and known constraints | Outcome, scope, acceptance criteria | Intended work identifiable | STD-01, STD-03 |
| 1 — Risk and Authority | Scope and consequences | Classifications, permission and approval boundaries | Next action authorized; recovery needs identified | STD-02, STD-04, STD-08–STD-13, STD-16 |
| 2 — Discovery | Repository, maintained guidance, existing work | Relevant context, baseline and unknowns | Enough evidence for a bounded next step | STD-05, STD-10, STD-14 |
| 3 — Planning | Context and uncertainty | Proportionate approach, checks, stop conditions | Approach fits scope and authority | STD-03, STD-06, STD-12, STD-13 |
| 4 — Implementation | Authorized approach and recoverable state | Bounded change | Intended change ready for checks, or limitation recorded | STD-01, STD-04, STD-05 |
| 5 — Verification | Change, acceptance criteria, environment | Actual check results and gaps | Evidence sufficient for execution claim; failures resolved or disclosed | STD-06, STD-15 |
| 6 — Review and Acceptance | Diff and evidence | Acceptance decision or pending review | Responsible reviewer decides, or task handed off pending review | STD-07, STD-16 |
| 7 — Preservation | Accepted work and material decisions | Maintained source, tests, knowledge and records | Relevant knowledge captured and work recoverable | STD-04, STD-14, STD-15 |

## Planning and feedback

An obvious T0 edit can proceed without a separate plan. Plan explicitly when uncertainty, multiple components, dependencies, migration, or recovery choices justify it. T2/T3 typically need staged plans; Controlled work needs consequence-specific preparation even when the edit is small. Update the approach when discovery changes assumptions. Verification failures return to discovery, planning, or implementation within scope; a failure is not authority to broaden the task.

## Stop and resume

Stop the affected action when authority is missing, constraints conflict, an exception is needed, restricted data would reach an unapproved system, external side effects are uncertain, resources reach their bounds, or a required dependency/check prevents safe progress. Continue independent authorized work where possible. Record Partial or Blocked honestly, preserve valuable work, and provide a [handoff](../contracts/HANDOFF_CONTRACT.md) with the next safe action. Cancellation and rejection are explicit states, not hidden incomplete work.

## Human acceptance and preservation

Implementation completion can precede acceptance; STD-07 governs the review boundary. Review may request changes, returning to implementation and verification. Merge and release require their own authority and evidence. Preserve useful incomplete work before handoff; preserve accepted changes and material knowledge in the project's existing source-of-truth structure. Do not create a decision record for every trivial edit.
