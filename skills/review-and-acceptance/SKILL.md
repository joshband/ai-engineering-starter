# Skill: Review and acceptance

**Use:** When meaningful agent-generated work is ready for accountable review. The responsible human may be the solo developer; no universal separate reviewer or PR is required.

**Read:** [Review requirement](../../core/standards/ENGINEERING_STANDARD.md), [completion contract](../../core/contracts/COMPLETION_CONTRACT.md), [task contract](../../core/contracts/TASK_CONTRACT.md).

## Procedure

1. Identify the proposed change, delegated scope, reviewer/authorizer, and acceptance criteria.
2. Examine the actual diff, verification evidence, limitations, risk, security and operational consequences. Do not substitute the author's summary for evidence.
3. Distinguish findings that block acceptance from optional improvements. Escalate missing authority or consequential action approvals.
4. Record an explicit acceptance state: Pending review, Accepted, Changes requested, Rejected, or Not applicable, with rationale and outstanding follow-ups.
5. Separately record execution state, whether a merge happened, and whether a release happened. Do not infer either from acceptance.
6. If the reviewer is an agent, provide a recommendation only; do not claim human acceptance or approve policy exceptions on the human's behalf.

## Output

Evidence-linked findings, a recommended disposition, and an accountable human decision when actually supplied. A recommendation is not acceptance.
