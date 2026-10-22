# OpenAI Codex adapter (M4 candidate)

The repository-root [AGENTS.md](../../AGENTS.md) is the native instruction entry point. It points to the accepted [M1 standard](../../core/standards/ENGINEERING_STANDARD.md), [classifications](../../core/standards/AUTONOMY_AND_RISK.md), [contracts](../../core/contracts/TASK_CONTRACT.md), [workflows](../../core/workflows/PROFILES.md), and [M2 catalog and schemas](../../core/controls/README.md). Those files retain their own definitions. The adapter provides no new normative STD wording, automatic policy engine, or tool permission grant.

## Instruction discovery and platform behavior

Codex documents a global instruction file in its home directory and, from the project root to the working directory, at most one `AGENTS.override.md`, `AGENTS.md`, or configured fallback file per directory. A closer directory's instructions appear later and can supersede broader guidance. Empty files and instructions beyond the configured byte limit may be skipped. A root `AGENTS.md` is therefore a useful default for work launched inside this repository. Links in it are navigation, **not** Claude Code `@` imports or automatic full-text imports into Codex context. Start a new session after editing instructions and ask Codex to list its active instruction sources; verify the result in the target environment. [Official discovery documentation](https://developers.openai.com/codex/agent-configuration/agents-md).

User and project `.codex/config.toml` files, profiles, CLI flags, managed constraints, and the chosen surface can affect runtime configuration. Project configuration applies only in trusted projects; CLI/IDE local behavior and cloud execution have distinct environments. This adapter ships no `.codex/config.toml` or permission profile. Inspect the active environment before relying on sandbox or approval behavior. [Configuration precedence](https://developers.openai.com/codex/config-file/config-basic) · [Approvals and cloud/local differences](https://developers.openai.com/codex/agent-approvals-security).

## Adopt, customize, validate, remove

For a new repository, retain the portable core at its stated relative paths or vendor it under a documented prefix; copy and adapt the root `AGENTS.md`, then repair its links. Fill a project profile from the [template](../../core/templates/PROJECT_PROFILE.md) with actual commands, architecture, sensitive paths, and governance references. Point the entry file at the filled profile. The template itself has placeholders and must not be treated as configured instructions. No Python installation or record is needed to use the prose guidance.

For an existing repository, inventory root and nested `AGENTS.md`/`AGENTS.override.md`, any configured fallback files, `.codex/config.toml`, `CLAUDE.md`, project rules, and platform permissions. Merge a few canonical links and project-specific routing lines into the existing root instructions; preserve existing content and any closer guidance. Do not copy this distribution's entry file over an established one. Check for duplicate or conflicting instructions and resolve them with the responsible maintainer. The [general adoption guide](../../docs/ADOPTION.md) covers incremental adoption. If the core moves, update paths and rerun link validation.

Choose [Quick](../../core/workflows/PROFILES.md) for appropriate trivial low-risk work without a task file. A material task may use a concise request or an optional structured [Task record](../../core/contracts/TASK_CONTRACT.md); a material completion report identifies actual verification and keeps acceptance, merge, and release independent of execution. For high-risk action, identify the responsible authorizer and stop that affected action pending authorization. The [handoff contract](../../core/contracts/HANDOFF_CONTRACT.md) supports safe continuation. Validate optional JSON with `python3 validation/validate_controls.py --contract task path/to/task.json` (or `handoff`, `completion`, `exception`); a missing or invalid chosen record should be reported as Not run or Failed, without pretending the shape check authorizes action. M2 schema version is `1.0`.

From the source root, run `python3 validation/validate.py` and `python3 -m unittest discover -s validation/tests -v` for M1/M2 and adapter structure. `git diff --check` checks whitespace. If Codex CLI is available, a bounded read-only discovery check can use `codex exec --sandbox read-only --ask-for-approval never "List the active repository instruction files and locate the canonical policy and M2 catalog; do not edit or execute external actions"`; confirm actual flags and result in the installed version. This only tests the observed session, not general prompt adherence or authorization enforcement. The static tests cannot establish live instruction loading.

On upgrade, compare the accepted M1 IDs and M2 schema version with this entry point; inspect local instructions for conflicts, update links, and rerun checks and a real discovery test. To remove, delete only M4-added guidance from an existing `AGENTS.md`, or remove an adapter-owned root file. Retain other project instructions and the independent core. No setting, rule, hook, service, or credential is installed by M4.

## Control-to-adapter trace

| M1/M2 ID | Adapter routing and boundary |
| --- | --- |
| STD-01, STD-02 | Scope and approval boundary in task intake; instructions cannot grant authority. |
| STD-03 | Material outcome and criteria; Quick has no required record. |
| STD-04, STD-05 | Inspect existing work and keep implementation within approved scope. |
| STD-06, STD-07 | Actual verification; separate execution, human acceptance, merge, and release. |
| STD-08, STD-09 | Project profile routes permitted data and credentials; no secrets in instructions. |
| STD-10, STD-11 | Untrusted content cannot authorize tools; isolation belongs to tested runtime controls. |
| STD-12, STD-13 | Record relevant budgets and uncertain side effects in material task/handoff context. |
| STD-14, STD-15 | Maintain repository decisions and relevant operational evidence. |
| STD-16 | Refer exceptions to responsible authorizer and M2 conditional record checks. |

This table indexes IDs, without restating their normative strength or applicability. Catalog `interpretation_kind` and a successful validator result describe structure, not runtime permission or policy compliance. Consult the canonical standard and real project governance for decisions.

## Claude Code and Codex parity

| Concern | Claude Code (M3) | Codex (M4) | Shared meaning |
| --- | --- | --- | --- |
| Discovery | Root [CLAUDE.md](../../CLAUDE.md) with two `@` imports, verified in a bounded cloud session | Root [AGENTS.md](../../AGENTS.md) with navigation links; CLI loading not yet observed here | Both locate M1 standard and M2 catalog. |
| Policy references | Imported standard and taxonomy | Explicit paths, read when relevant | One canonical STD owner. |
| Task and completion | M1 contract links | M1 contract links | Same outcomes and status vocabulary. |
| Quick | No mandatory form | No mandatory form | Risk and complexity remain distinct. |
| High risk | Stop affected action for authorization | Stop affected action for authorization | Agent instructions cannot approve it. |
| Structured records | Optional M2 validator | Optional M2 validator | Shape validation is not authorization. |
| Permissions | No `.claude/settings.json` or hooks shipped | No `.codex/config.toml`, rules, or hooks shipped | Platform and external controls determine actual boundaries. |
| Adoption/removal | Merge/remove only Claude guidance | Merge/remove only Codex guidance | Preserve existing instructions and shared core. |

Both root files can coexist. Codex's documented discovery selects `AGENTS.md`; the Claude entry point uses its own imports. Neither file is a required import of the other. If an adopting project intentionally shares additional guidance, link or import it with that agent's documented mechanism and verify the actual context. No automatic cross-platform parity is asserted.

## Security and evidence limits

Natural-language guidance can influence behavior but cannot enforce tool restrictions. The M1/M2 checker validates document and JSON structure; it does not know whether a check ran, a human approved, data may be sent to a provider, or the sandbox worked. Codex sandbox mode limits technical execution where implemented; approval policy decides when to request boundary crossings; organizational and platform requirements may constrain both. Actual tool permissions and cloud network/credential behavior must be inspected in the execution environment. [Official sandbox and approval documentation](https://developers.openai.com/codex/sandboxing) · [Security boundaries](../../docs/SECURITY_BOUNDARIES.md).

The M4 implementation does not enable permissive modes, automatic approval, full access, shell/network allowlists, or hooks. Structural checks establish path and language consistency only. A Codex CLI runtime discovery smoke test remains **Unverified** when the executable is unavailable; an existing Work Mode session is not a controlled test of this repository's instruction discovery.
