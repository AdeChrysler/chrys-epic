# E01 — {{business outcome}}

Home: {{local | github}} · Canonical: {{actual path or issue URL}}
Record: {{canonical | snapshot + source URL + fetched UTC}}
Project: {{root/repository}} · Baseline: {{revision or no source yet}}
Plan revision: {{revision}} · Readiness: {{draft | ready | blocked + reason}}

## Outcome and boundary

Outcome: {{who can do what, and why it matters}}
Current evidence: {{observed gap; source path/link; unknowns explicitly labeled}}
Connected journey: {{actor → ordinary action → durable result → next step}}
Included: {{bounded result}}
Preserve: {{existing behavior/accepted directions}}
Excluded: {{non-goals}}
Endpoint: {{locally accepted | reviewed change | authorized deployment target}}
Authority: {{issue writes/code edits/reviews/merge/deploy actually authorized}}

## Choices

Epic home: {{choice; user words or assumed; connection/publication status}}
Delivery: {{Fast | Hybrid | Careful}} · Basis: {{user words/delegated/assumed, UTC}}
Risk: {{real client data; auth/privileges; shared/production DB; audience; unknowns}}
Pace: {{Sprint | Steady | Checkpoint}} · Basis: {{user words/delegated/assumed}}
Deadline: {{user-provided or none}} · Scope tradeoff: {{if needed}}
Planner: {{harness/model + observed verification source}}
Executor: {{Codex → Luna; Claude → Sonnet; resolve/verify at dispatch}}
Reviewer: {{native independent reviewer route + verification status}}
Stack: {{shadcn/ui or UI not applicable; PostgreSQL or persistence not applicable; self-hosted components; Railway/existing/chosen host proposal}}
Service exceptions: {{none, or explicit user choice + reason}}
Status owner: {{coordinator; permitted tracker transitions}}

## Ordered children

| ID | Business outcome | Contract | Depends on / gate | Status | Evidence / pending gate |
|---|---|---|---|---|---|
| T01 | {{outcome}} | {{relative task path or real issue URL}} | {{none or task ID + code-reviewed/accepted/released}} | ready | {{not run}} |

Add only useful children. Group by business milestone here if needed. Identify the child/gate owning each Fast/Hybrid runtime batch; include verification work with implementation from the first task.

## Epic acceptance

| ID | Observable connected outcome | Child ACs | Proof target / method |
|---|---|---|---|
| E01-AC01 | {{actor, action, visible/durable result}} | {{T01-AC01}} | {{combined journey + endpoint}} |

## Decisions and blockers

Decisions: {{choice → evidence/reason → reversal path; include revisions}}
Owner-only blockers: {{none, or question + owner + affected task/gate}}
Discovery prerequisites: {{unknown + bounded task/owner + required gate}}
Parked ideas: {{unrelated work; no implicit authorization}}

## Start

Execution brief: {{project-relative GOAL.md path; use a Markdown link only when it resolves from this document's actual home}}. One active implementation child; required ACs remain required in every mode. Do not mark the epic complete while any required child/gate is incomplete.
