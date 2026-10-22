# Claude Code entry point

@core/standards/ENGINEERING_STANDARD.md
@core/standards/AUTONOMY_AND_RISK.md

The imported standard owns policy. This file only points Claude Code to applicable project guidance; it does not grant tool access or create new requirements.

- Start with the objective, boundaries, actual consequences, and delegated authority. Use [workflow profiles](core/workflows/PROFILES.md) to choose proportionate steps. Quick local work needs no formal task record.
- For material work, use the [task contract](core/contracts/TASK_CONTRACT.md) and report actual checks and independent execution, acceptance, merge, and release states using the [completion contract](core/contracts/COMPLETION_CONTRACT.md). A structured record is optional; if one is used, validate it with the [M2 interface](core/controls/README.md).
- Consult the [control catalog](core/controls/controls.json) by relevant STD ID for structured indexing. The catalog's `interpretation_kind` value `adapter_candidate`, risk labels, and a passing validator do not authorize execution.
- For high-risk or consequential actions, identify the applicable approval boundary and stop the affected action until authorized. Continue independent authorized work where possible. Use the [handoff contract](core/contracts/HANDOFF_CONTRACT.md) to preserve safe continuation.
- This source distribution has no filled project profile. When adopted in another repository, point to its maintained project profile and real build/test commands; do not treat [the template](core/templates/PROJECT_PROFILE.md) as configured guidance.

No project permission settings, hooks, allowlists, model choice, or runtime isolation are installed by this entry point. The actual Claude Code settings and platform permissions remain independently authoritative.
