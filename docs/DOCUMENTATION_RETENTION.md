# Research, decision, and evidence retention

**Status:** Proposed documentation practice in draft PR #10; descriptive, not a new STD requirement.\
**Scope:** Materials supporting the AI-Native Software Engineering Starter Kit.

## Principles

1. **Preserve originals, not reconstructed substitutes.** Keep the complete original research or source artifact where authorized. A summary, excerpt, or recreated narrative must be labeled as such.
2. **Keep one normative owner.** [STD-01–STD-16](../core/standards/ENGINEERING_STANDARD.md) remain authoritative in the M1 standard. Research, decisions, evaluations, and roadmap files do not create additional MUST requirements or override organizational policy.
3. **Preserve historical context.** Keep dated findings, unsuccessful experiments, rejected alternatives, and limitations. Mark supersession with a link instead of silently rewriting history.
4. **Use links before copies.** Index existing repository artifacts at their current paths. Move them only with a separate reviewed migration that fixes links and preserves history.
5. **Protect restricted material.** Before importing external documents, inspect for secrets, personal data, client information, proprietary text, contractual restrictions, and third-party licensing. Do not commit disallowed material or paste secrets into Git history.
6. **Distinguish evidence levels.** Label structural checks, observed instruction discovery, behavior, and independent enforcement separately. Missing or deferred evidence is Unverified, not Passed.
7. **Preserve provenance.** Record origin, author/owner if known, original date or date unknown, retrieval/import date, original URL or revision where appropriate, and relationship to later decisions.
8. **Make changes reviewable.** New or imported source material should be a separate bounded change when substantial. Human acceptance, merge, and release remain distinct.

## Locations and ownership

| Location | Contents | Rule |
| --- | --- | --- |
| [research/](research/README.md) | Original studies, source material, comparisons, notes, and an index | Source evidence; not policy |
| [decisions/](decisions/README.md) | Recorded trade-offs, decision status, and links to ADRs | Decisions; no competing STD definitions |
| [evaluations/](evaluations/README.md) | Test protocols, experiments, results, pilot evidence | Report actual conditions and outcomes |
| [roadmap/](roadmap/README.md) | Prioritized proposals and links to plans | Proposed does not mean approved |
| `archive/` (only if needed) | Superseded historical copies that cannot remain at their existing location | Preserve date, reason, successor, and provenance |
| `core/`, `validation/`, `adapters/`, `skills/` | Existing implementation and validation sources | Remain in place; index by link |
| Root README / CHANGELOG / PR history | Navigation, version history, review record | Retain source-of-truth location |

## Minimal metadata for imported research

Use a short header or companion index entry with:

- **Title and subject**
- **Document type:** original, excerpt, summary, reconstruction, or external reference
- **Origin / source URL or revision**
- **Original date:** actual date or unknown; do not infer
- **Imported / reviewed date**
- **Owner or attribution:** if known and appropriate
- **Status:** current, historical, superseded, disputed, incomplete, or unverified
- **Related decisions, implementation, and tests**
- **Restrictions:** license, confidentiality, redistribution, or retention concerns when relevant

Do not add formal metadata to every trivial document retroactively. This is a lightweight practice for substantive research and external imports.

## Import workflow

1. Inventory candidate sources and avoid duplicates.
2. Retrieve the original and verify what it contains.
3. Check whether Git is an appropriate destination. For restricted or large material, retain it in an authorized external location and index a non-sensitive reference instead.
4. Preserve original wording and attach attribution; add a clearly separate summary only when helpful.
5. Identify superseding research and related accepted decisions without rewriting the original.
6. Review links, relative paths, security exposure, and provenance.
7. Update the [research index](research/README.md) and request separate human acceptance for the import.

## Change and removal

Do not delete historical evidence merely because a conclusion changed. Correct errors with dated amendments or replacement links. Remove or restrict material when legally, contractually, or security-required; assess Git history exposure and follow appropriate containment procedures rather than assuming deletion from the working tree removes exposure.

## Scope of this PR

This PR adds **organization and inventory only**. It does not claim to recover external research, alter accepted policies, move existing files, configure automation, or authorize a release.
