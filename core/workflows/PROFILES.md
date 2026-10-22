# Workflow Profiles

Procedures implement the [lifecycle](LIFECYCLE.md); [taxonomy](../standards/AUTONOMY_AND_RISK.md) owns classifications and the [standard](../standards/ENGINEERING_STANDARD.md) owns obligations. Selection depends on complexity and actual consequences, not team size. Profiles do not grant permissions.

## Decision table

| Context | Starting profile | Adjustments |
| --- | --- | --- |
| L, T0, bounded local authority | Quick | Escalate process if consequences or uncertainty increase |
| L/S, T1 | Standard | Add checks relevant to shared behavior |
| L/S, T2/T3 | Structured | Stage work and reassess dependencies |
| H, any complexity | Controlled | Apply independently enforced controls appropriate to consequences |
| A0 analysis | Scale discovery to complexity | No modification authority implied |
| A3/A4 proposed operation | Controlled when consequences warrant | Explicit authorization and operational controls; M1 supplies no operation runtime |

## Quick

State the intended outcome and boundary in the request, make the small edit, inspect the diff or run the relevant inexpensive check, and report the result for the developer's review. No task file, branch, PR, container, service, telemetry stack, or separate planning document is required just to use this profile. Applicable STD requirements still apply; a trivial edit does not authorize consequential publication.

## Standard

Identify task-contract semantics (a short request can suffice), inspect relevant guidance and baseline, implement within scope, run targeted checks, and report evidence and limitations. Obtain applicable review and preserve material knowledge. Use templates only when they help.

## Structured

Add explicit discovery, a staged plan, dependencies, revision context, check strategy, and meaningful decision records to Standard. Verify increments, update the plan as evidence changes, and hand off resumable context when interrupted. Scale records to uncertainty rather than document count.

## Controlled

Add explicit action authority, approvals at actual consequence boundaries, appropriate isolation and credential restrictions, operational evidence, spending/stopping controls where applicable, and recovery planning. For consequential retries, reconcile prior outcomes. For high-consequence recurring operations, identify cancellation and escalation. Assess real control guarantees before execution; unresolved controls block the affected action. No specific platform is mandated or implemented by M1.

A higher complexity profile need not create release authority. A higher-risk action may use a short plan with strong permissions and evidence. Record why an atypical profile is appropriate rather than treating the table as an authorization rule.
