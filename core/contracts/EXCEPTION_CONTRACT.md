# Exception Contract

Owner of exception-record semantics. Authority and limits come from STD-16 in the [standard](../standards/ENGINEERING_STANDARD.md); this form grants no exception.

## Required fields (exceptions to an applicable MUST)

- Requirement ID and reason for the deviation
- Authorized scope (affected actions, work or environment, and relevant boundaries)
- Risk introduced and compensating safeguard, or an explicit explanation if none is available
- Responsible authorizer and authorization evidence/status (pending, granted, denied, or expired)

A concise record may be sufficient for low-risk exceptions. This contract does not grant an exception; STD-16 in the canonical standard governs authorization.

## Conditional fields

- **Material Profile H exceptions:** expiration or review trigger is **required** under STD-16.
- **Other exceptions:** expiration or review trigger is **recommended**, not universally mandatory.
- Where relevant: repository/revision, duration, affected systems, and stronger obligations that may disallow the deviation.

## Invariants

- A proposal or pending request is not authorization. Do not perform the affected action until approval exists.
- An agent cannot authorize its own exception or override applicable law, contracts, or stronger organizational requirements.
- Any approval applies only to its recorded scope; unresolved conflicts require escalation.
- Independent, already-authorized work may continue while the affected operation is paused.

## Example

Requirement: STD-06. Reason: isolated legacy fixture cannot run in the available environment. Scope: proposed deferral of that check for one bounded non-production patch. Risk: missed legacy behavior. Compensating safeguard: inspect fixture and run available regression checks. Responsible authorizer: project maintainer, approval pending. Expiration/review trigger (recommended for this non-production example): before integration, or when the fixture becomes available, whichever occurs first. Stronger governance: confirm no mandatory release check is being waived. Until approved, the exception is not effective and the affected criterion remains unmet.
