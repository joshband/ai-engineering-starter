# Skill: Task intake

**Use:** When work is material, uncertain, consequential, or needs explicit boundaries. For trivial low-risk Quick work, a short objective and boundary suffice; do not require a form.

**Read:** [Task contract](../../core/contracts/TASK_CONTRACT.md), [taxonomy](../../core/standards/AUTONOMY_AND_RISK.md), [workflow profiles](../../core/workflows/PROFILES.md), and applicable [M1 standard](../../core/standards/ENGINEERING_STANDARD.md).

## Procedure

1. State the observable outcome, in-scope and out-of-scope work, constraints, acceptance criteria, and delegated authority for material work. Keep the request concise.
2. Distinguish actual consequence risk (L/S/H), autonomy (A0–A4), and complexity (T0–T3). Choose a proportionate workflow; classification is not authorization.
3. Identify project instructions, existing work, dependencies, sensitive data, and recovery needs. Ask only for material missing information.
4. Identify destructive, irreversible, sensitive, or externally consequential actions and the responsible authorizer. Do not infer approval from tool availability or from a skill.
5. If helpful, write an optional record conforming to [M2 Task schema](../../core/controls/schema/task.schema.json); validate its shape with `python3 validation/validate_controls.py --contract task <path>` if a file exists.

## Output

A bounded task description with a clear next authorized action, or **Blocked** for the affected action when authority is missing. Never self-authorize scope expansion or claim schema validation is policy approval.
