# Execute {{epic title}}

Readiness: {{ready | draft + blocker}}
Project root: {{actual project root; resolve relative paths from here}}
Canonical epic: {{actual GitHub issue URL or .epics/slug/EPIC.md}}
Ordered children: {{canonical epic table / actual issue links}}
Plan revision: {{revision}}

## Copy to start

Open this project in Claude or Codex, then copy the single line below. The rest of this file is the instruction the agent will read. A draft must have its named blockers resolved before starting.

```text
/goal Read ".epics/{{slug}}/GOAL.md" and complete only the epic it names.
```

If this host has no `/goal`, send the sentence after `/goal` as an ordinary message. This fallback starts authorized session work; it does not promise a persistent background goal. Do not create another goal from inside this file when one is already active.

## Business result and choices

Deliver: {{one business outcome}}
Keep out of scope: {{non-goals / other epics}}
Delivery: {{Fast | Hybrid | Careful; selected or assumed basis}}
Execution pace: {{Sprint | Steady | Checkpoint; selected or assumed basis}}
Deadline: {{if provided; otherwise none}}
Endpoint and authority: {{exact allowed local/review/release endpoint; actions already authorized}}
Owner-only blockers: {{none, or precise blocker + affected task/gate}}

## Model and stack contract

Planner/replanner: {{verified Astra/Sol or Fable/Opus 5.5 route}}
Executor: receiving **Codex → Luna; Claude → Sonnet**. Verify actual identity before edits; no Grok or silent substitution. An eligible planning-model coordinator may delegate one native execution worker at a time. If unavailable, save the handoff and explain the correct session to open.
Independent reviewer: {{native route; a fresh reviewer, not worker self-QA}}
Concrete stack: {{shadcn/ui where UI applies; PostgreSQL where persistence applies; self-hosted components; Railway/existing/chosen deployment proposal}}
Service exceptions: {{none or explicit authorization}}
No Supabase, including self-hosted Supabase, or new required external SaaS service without an explicit recorded user exception. A proposed host does not authorize deployment.

## Execution instructions

Read the epic and the four copied runbook files before acting:

- [Execution protocol](runbook/execution.md)
- [Delivery mode and pace](runbook/delivery.md)
- [Model routing](runbook/models.md)
- [Stack policy](runbook/stack.md)

Recover current state and prior results before dispatch. Read GitHub again if it is canonical; do not silently execute a stale local snapshot. Read each selected child's complete contract. Implement **one child at a time**, in dependency order, and update its AC evidence and the epic's status table before moving on. Never implement two children concurrently or switch to another epic. Fast/Hybrid may defer runtime proof only at a recorded gate; deferred proof is not completion.

Make reversible implementation choices yourself within the accepted plan. Route scope, architecture and acceptance changes to an eligible planner. Ask the human only for a business decision, missing authority/access, or another true owner-only blocker. Preserve findings and scope. Sprint/Steady continue automatically; Checkpoint waits after each child.

Check outcomes, not only builds. Keep required failures open, distinguish self-QA from independent review, and require the selected delivery gates. If stuck, record the child/AC, evidence and next action; do not call the epic complete. Finish only when all required children and the authorized endpoint pass. Stop there.

Tell the human what now works, what was checked, what remains, and what happens next, using plain English and business outcomes. Keep detailed diagnostics in the task evidence.
