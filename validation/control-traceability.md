# M2 control traceability

Each row maps a stable catalog ID to its sole normative definition in the [M1 standard](../core/standards/ENGINEERING_STANDARD.md). The [catalog](../core/controls/controls.json) carries the same source labels and concise indexing topics. Its descriptions do not restate or replace policy. The [contract schemas](../core/controls/README.md) validate records only when records are used.

| Control | M1 source | Deterministic check | Editorial/operational review still needed |
| --- | --- | --- | --- |
| STD-01 | [Defined task authority](../core/standards/ENGINEERING_STANDARD.md#std-01--defined-task-authority) | ID, clause labels; material task fields | Real delegation and scope |
| STD-02 | [Consequential action approval](../core/standards/ENGINEERING_STANDARD.md#std-02--consequential-action-approval) | ID, clause labels; explicit approval boundary shape | Consequences, permission source, actual authorization |
| STD-03 | [Task boundaries and acceptance](../core/standards/ENGINEERING_STANDARD.md#std-03--task-boundaries-and-acceptance) | ID, clause labels; material task criteria | Adequacy of outcome and criteria |
| STD-04 | [Recoverability](../core/standards/ENGINEERING_STANDARD.md#std-04--recoverability) | ID and clause labels | Important work and tested recovery |
| STD-05 | [Change scope and dependencies](../core/standards/ENGINEERING_STANDARD.md#std-05--change-scope-and-dependencies) | ID and clause labels | Actual diff, licenses, organizational requirements |
| STD-06 | [Verification evidence](../core/standards/ENGINEERING_STANDARD.md#std-06--verification-evidence) | ID, clause labels; status/evidence field shape | Whether checks ran and suit behavior/risk |
| STD-07 | [Review and acceptance](../core/standards/ENGINEERING_STANDARD.md#std-07--review-and-acceptance) | ID, clause labels; separate acceptance field | Genuine reviewer or approved bounded automation |
| STD-08 | [Data and provider authorization](../core/standards/ENGINEERING_STANDARD.md#std-08--data-and-provider-authorization) | ID and clause labels | Actual destinations and data agreements |
| STD-09 | [Secrets and credentials](../core/standards/ENGINEERING_STANDARD.md#std-09--secrets-and-credentials) | ID and clause labels | Secret exposure and containment |
| STD-10 | [Tool, MCP, and skill trust](../core/standards/ENGINEERING_STANDARD.md#std-10--tool-mcp-and-skill-trust) | ID and clause labels | Capabilities, permission boundaries, injection resistance |
| STD-11 | [Execution isolation](../core/standards/ENGINEERING_STANDARD.md#std-11--execution-isolation) | ID and clause labels | Actual runtime guarantees |
| STD-12 | [Cost and resource controls](../core/standards/ENGINEERING_STANDARD.md#std-12--cost-and-resource-controls) | ID and clause labels | Effective bounds and stopping conditions |
| STD-13 | [Durable operations and side effects](../core/standards/ENGINEERING_STANDARD.md#std-13--durable-operations-and-side-effects) | ID and clause labels | Prior effects, idempotency, cancellation, recovery |
| STD-14 | [Authoritative engineering knowledge](../core/standards/ENGINEERING_STANDARD.md#std-14--authoritative-engineering-knowledge) | ID and clause labels | Maintained source-of-truth artifacts |
| STD-15 | [Execution evidence](../core/standards/ENGINEERING_STANDARD.md#std-15--execution-evidence) | ID and clause labels | Sufficiency, retention, sensitive data handling |
| STD-16 | [Exceptions](../core/standards/ENGINEERING_STANDARD.md#std-16--exceptions) | ID and three source labels; granted evidence; material H trigger | Authorizer's authority, risk, scope, safeguard, legal/governance constraints |

The validator compares canonical headings, titles, and source strength labels with catalog entries; exact completion status tables with schema enums; schema-supported shapes and conditionals with 9 valid and 13 negative fixtures. It identifies structural drift, not semantic equivalence. Reviewers must compare catalog topics, applicability, risk boundaries, and schema requirements to the accepted Markdown and verify that no narrower or stronger interpretation slipped in. In particular, absent structured records for Quick work and the optional trigger for nonmaterial or non-H exceptions are deliberate.
