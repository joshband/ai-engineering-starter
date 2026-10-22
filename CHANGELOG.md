# Changelog

## 0.2.0 candidate — 2026-10-22

- Added versioned structured controls for STD-01 through STD-16 and optional Task, Handoff, Completion, and Exception record schemas.
- Extended the original M1 validation entry point with standard-library catalog, schema-subset, drift, and fixture checks.
- Added 9 positive and 13 negative fixtures, traceability, and conditional boundary regression tests.
- M2 accepted following architecture/policy review and squash-merged in PR #2 (commit dcf7e41ce1553dd5ea4138c99c0bae46495a7db2). No runtime authorization, adapter, service, release, or tag implemented.

## 0.1.0 candidate — 2026-10-22

- Implemented M1 portable engineering policy, classifications, contracts, lifecycle, workflows, and minimal templates.
- Added incremental adoption and security-boundary guidance.
- Added a dependency-free structural checker and acceptance matrix.
- Clarified mandatory review/expiration triggers for material Profile H exceptions (STD-16); made required, conditional, and invariant contract semantics explicit without adding process for low-risk work.
- At candidate creation, human architecture/policy acceptance was pending. M1 was later accepted by the maintainer and merged in PR #1 (merge commit b21ef5e86f41d5715bd1eb727be58076e45a1e56). No release tag was created.
