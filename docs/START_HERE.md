# Start here — choose a small, safe path

This page is **navigation**, not a new standard or mandatory process. The [M1 engineering standard](../core/standards/ENGINEERING_STANDARD.md) owns STD-01–STD-16; [classification](../core/standards/AUTONOMY_AND_RISK.md) and [workflow profiles](../core/workflows/PROFILES.md) own their respective definitions. Existing project and organizational authority still applies.

## What are you trying to do?

| Situation | Smallest useful path | You do **not** need by default |
| --- | --- | --- |
| Understand the kit | Read [README](../README.md), [M1 standard](../core/standards/ENGINEERING_STANDARD.md), and [profiles](../core/workflows/PROFILES.md) | Agent runtime or installation |
| Make a trivial, low-risk local edit | [Quick profile](../core/workflows/PROFILES.md#quick): state outcome/boundary, inspect diff or cheap check, report result | Task file, branch, PR, structured JSON |
| Implement a material change | [Standard profile](../core/workflows/PROFILES.md#standard) and [task semantics](../core/contracts/TASK_CONTRACT.md); report actual [completion evidence](../core/contracts/COMPLETION_CONTRACT.md) | Mandatory form or automation |
| Handle high uncertainty or consequences | [Structured or Controlled profiles](../core/workflows/PROFILES.md#structured); obtain actual action authority where required | Assumed tool permissions |
| Start a new repository | [Adoption guide](ADOPTION.md#new-repository) and [project profile](../core/templates/PROJECT_PROFILE.md) | Installer |
| Evaluate an established repository | [M7 adoption decision kit](adoption-decision/README.md): inventory, then No adoption / Reference only / Selective adoption; to delegate the evaluation to a separate session, paste the [adoption review prompt](ADOPTION_REVIEW_PROMPT.md) | Overwriting existing instructions |
| Use Claude Code or Codex | Read [Claude adapter](../adapters/claude-code/README.md) or [Codex adapter](../adapters/codex/README.md); verify real discovery separately | Assumed runtime enforcement |
| Need optional procedural assistance | Browse [M5 skills](../skills/README.md) | Automatic skill invocation |
| Need optional machine-readable records | [M2 controls](../core/controls/README.md) | JSON for Quick tasks |

## Minimum useful sequence

1. Identify the requested outcome, scope, existing instructions, and authority.
2. Select a proportionate [profile](../core/workflows/PROFILES.md); Quick is deliberately lightweight.
3. Perform only authorized work, then record checks actually run and important limitations.
4. Keep **Completed** implementation, **Passed** verification, **Accepted** human review, merge, and release separate.

The [security boundaries](SECURITY_BOUNDARIES.md) explain why text instructions and passing validators are not runtime permission controls.

## What has actually been verified?

Use the [capability and evidence map](CAPABILITY_STATUS.md). Runtime-dependent M8 testing is deferred, not a reason to treat documentation-only work as blocked. No adapter is represented as a universal security guarantee.
