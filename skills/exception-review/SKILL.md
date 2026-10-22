# Skill: Exception review

**Use:** When someone proposes not following an applicable M1 MUST. This skill drafts and checks an exception request; it never grants one.

**Read:** [STD-16](../../core/standards/ENGINEERING_STANDARD.md), [exception contract](../../core/contracts/EXCEPTION_CONTRACT.md), [taxonomy](../../core/standards/AUTONOMY_AND_RISK.md).

## Procedure

1. Identify the exact applicable MUST, context, requested deviation, reason, scope, risk, and proposed compensating safeguards.
2. Identify the responsible authorizer and any stronger law, contract, or organizational requirement that cannot be overridden.
3. For a **material Profile H exception**, require an explicit expiration or review trigger. For other exceptions, recommend one without misrepresenting SHOULD as MUST.
4. Record authorization evidence only when actually supplied by the responsible authorizer; an agent cannot self-authorize.
5. If an optional JSON exception record is used, check its supported shape with [M2 Exception schema](../../core/controls/schema/exception.schema.json). Validation does not grant the exception.
6. Until authorization is confirmed, mark the affected action pending/blocked and continue only independently authorized work.

## Output

Scoped exception proposal, authorization status, conditional review trigger, and next safe decision. Do not present a draft as a granted exception.
