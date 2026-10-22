# Reversal and follow-up

The adoption kit is **manual and optional**. An adopting repository must know which files it changed before it can safely undo them.

## Before editing

Record the baseline revision, owner, authorized file list, whether files are copied or linked, and any existing uncommitted changes. Prefer the smallest reversible diff. Never overwrite an existing `AGENTS.md`, `CLAUDE.md`, scoped rule, hook, CI configuration, or project policy.

## Remove only pilot-introduced material

1. Identify the exact references, example, or optional skill copies introduced by the pilot.
2. Confirm that no project-owned instructions or links now depend on them.
3. Remove only those additions; restore original links if they were changed.
4. Inspect the diff and run the adopting repository's applicable checks.
5. Record whether the pilot was **Adopted**, **Revised**, or **Rejected**; keep verification, acceptance, merge, and release states separate.

Do not assume a `git reset`, deletion of a whole directory, or reverting an unrelated commit is safe when other work exists. Obtain required approvals for any commit, push, PR, merge, or deployment.

If a project adopted only external references, removing those links may be sufficient. If a copied skill's relative links no longer resolve, repair or remove the copy rather than leaving broken guidance. Removing text does not revoke actual tool credentials or permissions; those controls require their own owners and actions.

See [decision matrix](DECISION_MATRIX.md), [existing-repository guidance](../ADOPTION.md#existing-repository), and [security boundaries](../SECURITY_BOUNDARIES.md).
