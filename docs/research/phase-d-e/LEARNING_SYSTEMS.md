# Self-improving agents, adaptive policies, and reinforcement learning

**Status:** Phase D/E research track; not an implemented learner.  
**Recommendation:** Evaluation-driven improvement now; controlled adaptation later; RL/model training only when justified by a strong evaluation and safety foundation.

## Important distinction: what is actually improving?

| Layer | Example of change | Required feedback | Risk/priority |
| --- | --- | --- | --- |
| **L0 — Observation and evaluation** | Record which task types failed, what checks passed, cost and review effort | Deterministic tests, human review, runtime telemetry | **P0: capture from day one** |
| **L1 — Offline workflow improvement** | Propose shorter task prompts, better handoff, added checks, scoped skill revisions | Replay/held-out evals and human acceptance | **P2: first self-improvement** |
| **L2 — Adaptive selection** | Contextual-bandit selection among approved model/workflow options | Many comparable, well-attributed task outcomes; exploration limits | **P3: controlled experiment** |
| **L3 — Training a policy/model** | Fine-tune a routing policy or a model with preference/reward data, potentially RL | High-quality rewards, reproducible training/evals, held-out shifts, rollback | **Phase E research only** |
| **L4 — Open-ended recursive self-modification** | Agent changes its own tools, governance, test standards and execution policy | Extremely difficult to verify meaningful safety/quality | **Not recommended** |

*Self-improvement* is not synonymous with *reinforcement learning*. Changing prompts or skill procedures in response to measured errors is an easier-to-review type of scaffolding optimization; updating model weights requires substantially more research and engineering.

## Recommended improvement loop

```text
Approved task run
   -> immutable, redacted outcome/evidence record
   -> failure taxonomy and benchmark dataset
   -> proposal agent produces a candidate configuration diff
   -> offline replay + held-out capability/regression evaluations
   -> deterministic security/authorization constraints
   -> calibrated human review and approval
   -> limited canary with rollback
   -> promotion OR rejection with provenance
```

The learner must **not** change STD policy, control enforcement, ACLs, tool allowlists, credentials, or approval boundaries. Treat all suggestions as untrusted until reviewed and tested. Improvements should be stored as versioned, reversible project artifacts.

## Reward design

A single proxy reward such as "tests passed" is insufficient. Candidates should be evaluated by a **vector of outcomes**:

- Correctness: hidden tests, behavior checks, regressions.
- Adherence: changed-path bounds, forbidden effects, permission attempts, data handling.
- Human utility: acceptance, reviewer effort, perceived clarity, rework.
- Cost and performance: API spend when observable, latency, local compute, token/tool usage.
- Robustness: held-out repositories, changed task wording, restarts and timeouts.

**Hard constraints** are never compensated for by higher task-quality reward. A scope violation or secret leak disqualifies a candidate irrespective of pass rate. Carefully label noise, missing-cost telemetry, confounding from differing models/runtimes, and failures caused by fixture environment.

## Evaluation design

Anthropic's evaluation research emphasizes **code-based, model-based, and human graders**, and separates capability tests from regressions [S11]. Apply that approach to real coding tasks:

1. Create **versioned, fixed** train/development and held-out evaluation splits.
2. Track model/harness version, input fixture and repository SHA; separate task types, risk profiles and difficulty.
3. Use programmatic pass/fail checks for observable behavior; calibrate subjective LLM graders with humans.
4. Log paired A/B tests under the same allowed tools and budgets; randomize order when practical.
5. Watch for test contamination, reward hacking, selection bias, benchmark overfitting and shifted provider capabilities.
6. Require no safety regression and material utility gain before promoting a change.
7. Preserve prior passing baseline and rollback path.

A 10–20-task initial pilot can test feasibility and reveal obvious issues, **not justify statistical claims or learned routing policies**.

## Contextual bandits / online routing

Once a suitably large dataset exists, experiment with a **constrained contextual bandit** where actions are only already-approved model/harness configurations. Context could include task size, language, observed repository checks, risk/data classification and latency budget. The model recommends an arm; a hard policy filter can block disallowed arms.

- Start offline from logged routing data, then a very small controlled canary.
- Never explore high-risk tasks, production write permissions or disallowed providers.
- Estimate the risk of biased logged decisions and missing counterfactual outcomes; use randomized comparisons only where authorized.
- Roll back on increased scope violations, quality drop or spend.
- Avoid promising optimal token use or elimination of commercial subscription limits.

## Reinforcement learning proper

Actual RL policy/model training can be valuable where repeated simulation supplies **reliable, cheap, objective rewards**, such as constrained tool choice in a synthetic environment. However, coding-agent production trajectories have sparse/delayed rewards, variable tooling, potential reward hacking, and sensitive data concerns.

Research questions before any RL build:
- What trainable policy is owned: lightweight *route/task-decomposition policy*, or foundation-model weights?
- Does the intended model/provider offer authorized tuning/training access? Proprietary Claude/Codex weights should not be assumed trainable.
- Can safely sandboxed simulators produce thousands of meaningful trajectories with low data leakage?
- Can we demonstrate out-of-distribution gains, not merely improvements on a memorized test suite?
- How do we prove training does not modify authorization, bypass limits or incentivize gaming tests?
- What is the total cost of data curation, rewards, training compute and regression testing versus simple reviewed workflow changes?

**Provisional sequence:** versioned evaluations → reviewed scaffolding changes → controlled bandit policy → offline training experiments → only then consideration of larger RL. **Do not build an RL training system in the Phase D POC.**

## Research provenance

- [S11] Anthropic, *Demystifying evals for AI agents* (2026): supports multi-grader evaluations and capability/regression distinction.
- [S12] *Self-Improvements in Modern Agentic Systems* survey (2026): taxonomy of foundation-model vs scaffolding improvement; research survey, not implementation validation.
- [S14] Anthropic automated researcher report (2026): a specialized research example, not evidence that unrestricted autonomous coding improvement is safe.
- Framework and provider capability claims: [source register](SOURCE_REGISTER.md).

## Acceptance milestones for the learning track

**L0:** run and human outcome provenance captured; no sensitive contents logged by default.  
**L1:** candidate skill/prompt revision demonstrably improves held-out outcomes without regression; manually promoted.  
**L2:** constrained routing wins against fixed baseline with adequate sample/uncertainty reporting and bounded exploration.  
**L3:** training experiment is separately approved, repeatable, secure, and provides measurable OOD gains with safe rollback.
