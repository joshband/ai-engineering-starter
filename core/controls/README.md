# M2 control interface

The [engineering standard](../standards/ENGINEERING_STANDARD.md) remains the only normative owner of STD-01 through STD-16. This directory contains a versioned representation for future adapters and deterministic review. Catalog summaries and JSON Schema descriptions do not grant authority, waive a MUST, or establish compliance.

## Files and compatibility

- `controls.json`: one control per STD heading. `clauses` preserve each source label (including the separate Profile H MUST under STD-16), strength, and whether it is a requirement, recommendation, or option. `applicability`, `risk_profiles`, `evidence_expectation`, `interpretation_kind`, and `automation_limits` help consumers select appropriate review. A risk label is context, never permission.
- `schema/*.schema.json`: JSON Schema Draft 2020-12 for the catalog and four optional structured contracts. Every record and catalog has `schema_version: "1.0"`. A future incompatible change needs a new version and explicit migration; new optional descriptive fields may be considered only after compatibility review.
- [Traceability](../../validation/control-traceability.md): policy ownership and check coverage.

The schemas define record shape, types, required fields, and conditional fields. The standard-library validator implements the keywords used here: `type`, `required`, `properties`, `additionalProperties`, `enum`, `const`, `minLength`, `minItems`, `items`, `allOf`, `if`, and `then`. It checks known versions and additional catalog/record invariants. This is a focused subset of JSON Schema, not a general Draft 2020-12 implementation or a meta-schema validator. A full JSON Schema consumer may also validate these schemas independently.

Run `python3 validation/validate.py` for M1 and M2 checks, or `python3 validation/validate_controls.py` for the catalog, schemas, and fixture suite. Pass a structured JSON record path to the latter to validate one record. Exit 0 means its supported structural checks passed; nonzero includes paths and causes. No service, dependency installation, or formal record is needed for Quick work. The `none` fixture illustrates this absence of a task file; it does not represent a policy waiver.

## Contract mapping

| Schema | M1 owner | Required when a structured record is used | Conditional/context |
| --- | --- | --- | --- |
| Task | [Task contract](../contracts/TASK_CONTRACT.md) | Objective, scope, constraints, acceptance criteria, authority boundaries for material work | Classification, revision, dependencies, budget, approvals when relevant; nonmaterial records may be concise |
| Handoff | [Handoff contract](../contracts/HANDOFF_CONTRACT.md) | Objective, authorized scope, work, revision, checks, decisions, issues, next action for substantive handoffs | Uncertain effects, approvals, evidence location |
| Completion | [Completion contract](../contracts/COMPLETION_CONTRACT.md) | Delivered scope, separate execution/acceptance states, verification, limitations, next action | Accepted requires review evidence in a structured report; performed merge/release requires distinct evidence |
| Exception | [Exception contract](../contracts/EXCEPTION_CONTRACT.md) | Requirement, reason, scope, risk, safeguard/explanation, authorizer and status | Granted requires authorization evidence; material H requires expiration or review trigger; other exceptions need not have one |

Text and conversational contracts remain valid under M1. A schema cannot determine whether an outcome is genuinely material, a check ran, an authorizer has authority, an acceptance is genuine, or a compensating safeguard is adequate. Verify such claims against the repository and responsible human or platform authority. Structured approval fields only describe evidence; a passing validation result never approves an action.
