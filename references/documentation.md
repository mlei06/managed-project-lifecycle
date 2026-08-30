# Documentation standard

Maintain one authoritative home for each kind of project truth.

| Document | Owns |
|---|---|
| `README.md` | What the project is, current status, quick start, and links inward |
| `docs/product.md` | Problem, users, value, goals, non-goals, scope, and open questions |
| `docs/system.md` | Implemented and planned architecture, components, boundaries, data, flows, interfaces, configuration, operation, and deployment |
| `docs/quality.md` | Tests, evaluation, dated measurements with conditions, limitations, gaps, and technical debt |
| `docs/decisions/*.md` | Why a significant choice won over live alternatives |

## Rules

- Documentation changes in the same branch and PR as the behavior they describe.
- Mark planned architecture and behavior explicitly.
- Record measurements with date, corpus or sample size, configuration, and conditions.
- Do not edit an accepted ADR to rewrite history; supersede it.
- Add an ADR only when alternatives were real and the reasoning would otherwise be invisible.
- Do not create additional product-documentation Markdown by default. Propose a taxonomy change if information genuinely does not fit.

Operational files such as `AGENTS.md`, `CONTRIBUTING.md`, `.agents/project.json`, PR templates, hooks, and skill files are not product documentation and are outside the product-document allowlist.

## Update routing

- Changed purpose, audience, goal, non-goal, scope, or open question: product.
- Changed component, boundary, field, schema, flow, interface, configuration, runtime, or deployment: system.
- Changed tests, evaluation method, measurement, known gap, or debt: quality.
- Changed setup or basic usage: README and system, plus configuration examples when relevant.
- Chose among live alternatives: new ADR and a reference from the affected documentation or work item.

