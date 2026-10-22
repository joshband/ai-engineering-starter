# Claude Code adapter (M3 candidate)

This adapter is the repository-root [CLAUDE.md](../../CLAUDE.md) plus adoption and validation guidance. It reads the accepted [M1 standard](../../core/standards/ENGINEERING_STANDARD.md) and [taxonomy](../../core/standards/AUTONOMY_AND_RISK.md), then points to the [M2 catalog](../../core/controls/controls.json) and optional record schemas. The standard remains normative. There is no separate Claude policy, executable agent framework, permission configuration, or hook.

## Discovery and installation

Claude Code's project instructions can live in a root `CLAUDE.md`; its `@path` imports resolve relative to that file. The two imports in the entry point load the standard and taxonomy when the file is loaded. Its other Markdown links are navigation for the agent and developer, not automatic imports. Run Claude Code from the repository or its subdirectory; inspect `/context` under Memory files to confirm discovery in the actual environment. This has not been smoke-tested here because the `claude` executable was unavailable. Official documentation: [project memory and imports](https://code.claude.com/docs/en/memory).

For a new repository, retain the small portable core in the target repository and place an adapted `CLAUDE.md` at its root. If the core is vendored under `engineering/`, rewrite imports and links to begin with `engineering/`. Fill an actual project profile from the [template](../../core/templates/PROJECT_PROFILE.md), add its maintained path to the entry point, and record real commands and sensitive paths. Run the validation commands below after moving files. Do not import the unfilled template as project policy.

For an existing repository, inventory root and nested `CLAUDE.md`, `CLAUDE.local.md`, `AGENTS.md`, `.claude/rules/`, shared/local/managed settings, and current release behavior first. Merge the two canonical imports and a short link to the project profile into the existing instruction entry point. Do not overwrite local work or duplicate existing normative prose. Claude Code can read root `AGENTS.md` directly in supported sessions when no project `CLAUDE.md` applies; once you add `CLAUDE.md`, explicitly import `@AGENTS.md` if those instructions must remain in context. Verify the actual instruction mode and file list in `/context`. Direct AGENTS.md reading requires Claude Code v2.1.277 or later; using an explicit import is the compatibility route for sessions that cannot read it directly. Official documentation: [AGENTS.md discovery](https://code.claude.com/docs/en/memory#agentsmd).

The default experience is light: classify the work, use [Quick](../../core/workflows/PROFILES.md) for appropriate trivial local work, and verify/report the result. No form, branch, PR, container, or structured JSON record is installed as a universal requirement. For material work, use the [task](../../core/contracts/TASK_CONTRACT.md), [completion](../../core/contracts/COMPLETION_CONTRACT.md), and, when interrupted, [handoff](../../core/contracts/HANDOFF_CONTRACT.md) semantics. If you choose a structured record, check its M2 schema version (`1.0`) and run the validator; if the structured-record facility is unavailable, use the M1 prose contract and report that the structured check was Not run.

## Control-to-adapter map

| Control | Adapter use (instruction or record shape only) |
| --- | --- |
| STD-01 | Intake identifies delegated scope; no authority inferred from tools. |
| STD-02 | Consequential action is escalated to its responsible authorizer. |
| STD-03 | Material task points to observable criteria; Quick has no form. |
| STD-04 | Discovery checks important work and a reasonable recovery path. |
| STD-05 | Implementation stays within scope; dependency review remains project-specific. |
| STD-06 | Completion links actual checks to the exact M1 verification vocabulary. |
| STD-07 | Acceptance is separate from execution, merge, and release. |
| STD-08 | Project profile identifies authorized data/provider boundaries. |
| STD-09 | Project profile identifies credential boundaries without embedding secrets. |
| STD-10 | Tools and retrieved content cannot grant authority. |
| STD-11 | High-risk isolation is assessed externally; this adapter configures none. |
| STD-12 | Relevant unattended/billed limits belong to the bounded task context. |
| STD-13 | Handoff records uncertain external effects; safe retries need real reconciliation. |
| STD-14 | Decisions and accepted changes remain in maintained repository artifacts. |
| STD-15 | High-risk evidence needs actual operational records, not prompt assertions. |
| STD-16 | Exception records point to responsible authorization; material Profile H trigger is validated structurally. |

The table indexes the [canonical STD definitions](../../core/standards/ENGINEERING_STANDARD.md); it is not another statement of normative strength or applicability. The M2 `adapter_candidate` value describes potential future use, not an enabled enforcement capability.

## Permissions and evidence

The entry point is natural-language context. No `.claude/settings.json`, hook, shell/network allowlist, model override, or bypass mode is shipped. Claude Code has configurable permission modes and rules; the active user, project-local, managed, command-line, and platform settings determine actual tool behavior. A repository instruction cannot force a permission prompt, independently isolate execution, or verify an approver. Inspect `/status` and `/permissions` in the actual Claude Code session before relying on permissions, and use independent controls for high-risk work. Official documentation: [permission system](https://code.claude.com/docs/en/permissions), [settings precedence](https://code.claude.com/docs/en/settings), [hooks reference](https://code.claude.com/docs/en/hooks).

Static tests confirm paths, source ownership, and schema examples; they do not prove that Claude Code obeys instructions or that a permission setting took effect. Runtime compatibility is **Unverified** in this implementation environment. A reviewer with Claude Code should start in a clean checkout, inspect `/context` for root imports, inspect `/status` for settings sources, and try bounded advisory/Quick and material-task prompts without consequential actions. Record actual version, settings context, prompts, observed outputs, and limits before claiming runtime behavior.

## Validate, upgrade, or remove

From the distribution root, run `python3 validation/validate.py` and `python3 -m unittest discover -s validation/tests -v`. The tests require Python's standard library; using the instructions does not. For an optional structured record, run `python3 validation/validate_controls.py --contract task path/to/task.json` (or select another contract). Validation checks shape and structural drift only.

The adapter targets accepted M1 policy IDs STD-01–STD-16 and accepted M2 catalog/schema version `1.0`. Before upgrading the vendored core, review changed policy references, status vocabulary, schema compatibility, and project-specific instructions. Re-run validation and the real Claude Code discovery check. To remove the adapter, delete only its added imports and guidance from an existing `CLAUDE.md`, or remove an adapter-owned `CLAUDE.md`; preserve unrelated project instructions and the independent portable core. No hook, settings entry, or service needs uninstalling.
