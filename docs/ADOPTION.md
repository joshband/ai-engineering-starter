# Adoption

Start with [README](../README.md), [classifications](../core/standards/AUTONOMY_AND_RISK.md), and [workflow selection](../core/workflows/PROFILES.md). No installation service, generator, agent adapter, or mandatory external infrastructure is needed.

## New repository

1. Keep the core and supporting docs at their existing relative locations, or vendor this distribution under a clearly identified directory such as `engineering/`. Record the version adopted and local modifications.
2. Copy the [AGENTS template](../core/templates/AGENTS.md) into the repository's instruction entry point, fill its actual paths and permission boundaries, and complete a project profile. Keep copied template links valid: if moving a template outside its original directory, rewrite relative links to the retained core. Do not leave placeholders presented as configured controls.
3. Use Quick for an appropriate local trivial task. Use the task-contract semantics for material work, verify results, and review before acceptance as applicable.

Copying the complete small distribution preserves navigation. If adopting fewer files, retain the dependency closure of their relative links and validate it. No separate forms are needed for every task.

## Existing repository

Inventory current AGENTS/instruction files, architecture docs, project commands, policy, hooks, CI, protections, and release triggers before adding scaffolding. Identify each source of truth, owner, actual enforcement, and tested behavior. Preserve uncommitted work. Assess conflicts and gaps with the maintainer before replacing anything.

Merge a short entry point into existing instructions rather than overwriting them. Reuse the project's established architecture, task, review, and decision locations. Pilot on one bounded task, then adjust references and remove only explicitly agreed duplication. A new branch, PR, or container is not universally required by adoption; project governance may require them.

## Ownership and conflicts

Portable policy belongs in the canonical standard; technical commands, domain invariants, sensitive paths, and release behavior belong in the project profile. Organizational governance stays externally authoritative. Adapters expose applicable guidance without redefining policy. Avoid parallel full policy copies in agent-specific files. When sources conflict, identify the stronger applicable obligation and ask the responsible owner to resolve remaining ambiguity; an agent cannot grant itself an exception (STD-16).

Different agents may discover instructions differently. Point each agent to the same maintained entry point using its supported mechanism and confirm it can locate relevant context. The M3 Claude Code entry point provides one concrete example; actual runtime loading still needs confirmation in each target environment. Permission configuration remains separate from reading instructions.

## Optional M2 records

For projects that exchange structured records, use the [M2 control interface](../core/controls/README.md) and preserve its version. The catalog indexes the same policy IDs and the four schemas validate optional record shapes; neither changes when a task needs a formal record. An agent or developer may use M1's brief Quick workflow with no structured task file. Validate a record locally with the documented standard-library command, and still review its meaning, permissions, and evidence with the responsible owner.

## Optional M3 Claude Code adapter

Follow the [Claude Code adoption guide](../adapters/claude-code/README.md) after inventorying existing instructions and settings. The root [CLAUDE.md](../CLAUDE.md) demonstrates native instruction discovery and canonical imports in this source distribution. For an existing project, merge links and imports into its maintained instructions, repair moved relative paths, and preserve any existing AGENTS guidance explicitly when a CLAUDE file takes precedence. The adapter installs no permissions or hooks; validate actual runtime behavior in the target environment.

## Deferred work

M2 introduces shared control definitions and structural validation fixtures. M3 adds only the Claude Code instruction adapter. Other tool adapters and later capabilities require separate milestones and authorization. This repository still provides no hooks, skills package, routing, durable operations, orchestration, CI/CD, generator, or deployment.

[Security interpretation](SECURITY_BOUNDARIES.md) · [Acceptance matrix](../validation/acceptance-matrix.md)
