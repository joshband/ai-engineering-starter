# M4 Codex runtime instruction-discovery follow-up

**Status:** Open — deferred verification (non-blocking for provisional M4 acceptance)
**Recorded:** 2026-10-22
**Owner:** Maintainer / reviewer with access to a functioning Codex environment
**Milestone:** M4 (Codex adapter)
**Source PR:** #4

## Why deferred

The M4 implementation workspace did not have the Codex CLI on PATH. During acceptance, the Codex mobile cloud interface displayed “Couldn't load environments — Try again to see your cloud environments.” This prevents a controlled live discovery smoke test in that environment; it does not demonstrate an adapter failure. Structural validation and 13 unit tests were reported passing by the implementation team, but do not prove live Codex behavior.

## Required bounded follow-up

In a functioning Codex CLI or cloud environment, check out the accepted repository revision and start a fresh session at the repository root. Use a read-only sandbox and no additional permissions or consequential actions. Record the Codex version/surface and relevant configuration or sandbox/approval state where observable.

1. Distinguish automatically discovered instruction sources from documents explicitly opened during the test.
2. Verify root `AGENTS.md` is loaded and its navigation links resolve; do not assume Markdown links import file text.
3. Identify the canonical source of STD-01–STD-16 and the conditional material Profile H exception trigger in STD-16.
4. Locate M2 `core/controls/controls.json` and confirm `interpretation_kind` values do not grant authority.
5. Explain Quick work's no-record option and the distinction between execution Completed and human acceptance Accepted.
6. Check that Codex instructions are not represented as sandbox or permission enforcement.
7. Report PASS / FAIL / UNVERIFIED per item, including paths, actual observed outputs, and limitations.

## Closure criteria

Close only after a bounded live Codex session confirms native instruction discovery and correct policy routing without contradictory instructions. If it fails, document the exact environment and discrepancy, create a focused fix, and rerun. Keep runtime permission enforcement and cross-environment compatibility Unverified unless separately tested.

**Acceptance note:** M4 is provisionally accepted for architecture and structural validation. This item is deferred runtime verification, not a release-blocking claim of security enforcement.
