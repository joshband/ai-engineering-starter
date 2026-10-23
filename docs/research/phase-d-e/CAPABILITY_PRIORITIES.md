# Phase D/E capability backlog and prioritization

**Status:** Proposed evaluation, not implementation approval. Scores are planning judgments, not empirical performance.

## Selection method

Each capability receives a 1–5 assessment across risk reduction (30%), cross-project reusability (25%), feasibility (20%), portability (15%), and measurability (10%). Higher numbers mean more desirable *for the first bounded prototype*. Dependencies and risk gates override numerical scores.

| ID | Capability | Risk | Reuse | Feasibility | Portability | Measurable | Weighted | Selection |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| D01 | Task authority and state machine | 5 | 5 | 4 | 5 | 5 | **4.80** | **P0** |
| D02 | Restricted execution identity/tools | 5 | 5 | 3 | 5 | 5 | **4.60** | **P0** |
| D03 | Verification and audit evidence | 5 | 5 | 4 | 5 | 5 | **4.80** | **P0** |
| D04 | Time/iteration/cost stops | 5 | 4 | 4 | 5 | 5 | **4.55** | **P0** |
| D05 | Resume/reconcile effect ledger | 5 | 4 | 3 | 5 | 5 | **4.35** | **P0, narrow** |
| D06 | **Claude Agent SDK** harness adapter | 4 | 5 | 4 | 4 | 5 | **4.35** | **P0, first** |
| D07 | Codex adapter parity smoke test | 4 | 5 | 3 | 5 | 5 | **4.30** | **P1, portability gate** |
| D08 | Static explainable model routing | 3 | 5 | 5 | 5 | 5 | **4.35** | **P1** |
| D09 | Sequential implementation→verification | 4 | 4 | 4 | 4 | 5 | **4.10** | **P1** |
| D10 | Learning/evaluation dataset | 4 | 5 | 4 | 5 | 5 | **4.55** | **P0 capture, P1 analysis** |
| D11 | GitHub draft-PR handoff | 3 | 4 | 4 | 4 | 5 | **3.80** | **P1 only if separately authorized** |
| D12 | Local-model integration | 3 | 4 | 3 | 4 | 5 | **3.55** | P2 |
| D13 | Reviewed self-improvement suggestions | 4 | 5 | 3 | 4 | 4 | **4.05** | P2 after eval baseline |
| D14 | LangGraph/Temporal migration | 4 | 3 | 2 | 3 | 4 | **3.20** | P2 demand-triggered |
| D15 | Learned contextual routing/bandits | 2 | 4 | 2 | 3 | 3 | **2.65** | P3 until adequate data |
| D16 | Parallel multi-agent writes | 2 | 3 | 2 | 2 | 3 | **2.35** | P3 |
| D17 | Policy/model reinforcement learning | 2 | 3 | 1 | 2 | 2 | **2.05** | Research-only, Phase E |
| D18 | Autonomous merge/deploy | 1 | 2 | 2 | 2 | 3 | **1.80** | **Exclude from POC** |
| E01 | Cross-repo retrieval with ACL/provenance | 3 | 4 | 2 | 3 | 4 | **3.15** | Phase E |
| E02 | Hybrid local/cloud policy | 4 | 4 | 3 | 4 | 4 | **3.85** | After P2 local comparisons |
| E03 | Organization-wide policy distribution | 4 | 2 | 2 | 3 | 3 | **2.85** | Demand-triggered |

## Priority bundles

**P0 — Foundation and measurement.** D01/02/03/04/05/06 and outcome instrumentation for D10. One approved, local, reversible fixture; Claude-first; no production secrets or external writes. Fail-closed boundaries.

**P1 — Portability and usefulness.** D07/08/09; dataset analysis D10; optional draft PR handoff D11 subject to additional authority. Codex parity and transparent model/harness identity.

**P2 — Selective productivity improvements.** D12/13, optional durable-framework spike D14; begin eval-gated self-improvement proposals and local/cloud tests.

**P3 — Experimental learning and concurrency.** D15/16 after proper benchmarks, governance and resource isolation. D17 in a separate research/training program; D18 remains excluded from the described v2.0 proof of concept.

## Top five decisions recommended now

1. Claude Agent SDK first, but the first coordinator interface is **provider-independent**.
2. Independent task authority and worker constraints, not prompt-only policies.
3. A local event/effect journal with **reconciliation before retries**.
4. Evaluation records from the very first run, with human-calibrated outcomes.
5. Sequential agent handoff and manual approval before any publication.

## Reprioritization gates

Re-score after **10–20 varied, paired, reversible tasks** and at least one deliberate crash/restart, invalid authorization, denied tool, and exceeded-budget test. Do not treat an initial success as evidence for general agent or model quality. Track quality and cost separately; stop optimizing if safeguards regress.
