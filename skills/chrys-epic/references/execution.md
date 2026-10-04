# Execute one accepted epic

This protocol is copied into the epic's runbook during planning. It applies only when the user starts execution, including by sending the prepared `/goal` instruction. Reading or writing the goal file during planning does not start work. Installing or editing this skill also does not start a goal.

## Recover before acting

Read `GOAL.md`, its canonical epic, the ordered child list, and sibling [models.md](models.md), [delivery.md](delivery.md), and [stack.md](stack.md). Confirm project root, source revision/dirty work, current permissions and the authorized endpoint. Read the current issue bodies in GitHub mode. A restart first reconciles saved task state, work already present, and finished worker results; do not dispatch a duplicate worker or overwrite unfinished edits.

Keep the selected epic as the scope boundary. Record unrelated ideas in its parking list and continue the epic. Do not clean up the whole backlog, start a different epic, add a new framework or migrate infrastructure because it seems useful.

Resolve the receiving harness and verify the actual executor: Codex → Luna; Claude → Sonnet. An eligible planning model can remain the coordinator and delegate each child to that native executor. A Luna/Sonnet root can execute the accepted contract directly, but must route substantive replanning to an eligible Astra/Sol/Fable/Opus 5.5 planner. If the correct route is unavailable, save the precise handoff rather than silently substituting a model.

## One child at a time

1. Select the first unfinished, unblocked child in the recorded order whose required dependency gates are satisfied. Read its full scope and ACs. Keep **at most one implementation child active** across the root and workers. Never dispatch the rest of the epic as a swarm. Evidence gathering and independent review helpers do not get permission to implement other children.
2. Mark the child `active` and record the actual worker/model and starting revision. Implement only its accepted contract. Choose reversible details yourself, keeping shadcn/ui, PostgreSQL and the self-hosting rules. Check dependencies/service calls against the stack policy.
3. Run its focused checks and user journeys. For writes, prove persistence and relevant denied writes. Record results per AC as `pass`, `fail`, `not_tested`, or `blocked`, with raw evidence and candidate/environment. A successful build does not turn an untested AC into a pass.
4. Obtain the review/proof gate required by the delivery mode. Self-QA is distinct from independent review. Return failures to the same worker where supported and retest the affected behavior. Preserve original failures and clearing evidence. After two related failed correction rounds, use the planner escalation in `delivery.md`.
5. Update the canonical child and epic table. `done` requires all required ACs and its closure gate to pass. Fast/Hybrid can record `needs_live` after successful code review when a later milestone owns the runtime batch; later children may depend explicitly on `code-reviewed`. Never mark it `done` early. A `needs_review` child has not met `code-reviewed`. Missing independent review holds acceptance but need not block a later *independent* child after implementation has stopped. Record the pending gate.
6. In Sprint/Steady, continue automatically to the next eligible child. In Checkpoint, report and wait for the user's instruction. Respect dependencies even if a different child seems easier. If one child is blocked, document why and move to the next ready child **within this epic only**, without running both at once.

Allowed states: `ready`, `active`, `needs_review`, `needs_live`, `blocked`, `done`. Record dependency gates separately from state. A code review can pass without live acceptance; a release can exist without passing live verification. Do not equate these.

At each milestone, run its pending verification journeys against the combined candidate, obtain fresh independent judgment, and clear only criteria actually proven. If deployment is authorized, follow the selected mode's release gates, check the actual target/rollback, and bind live evidence to one unchanged release. Do not make a live release merely because Railway appears in the stack proposal.

## Make progress without unnecessary questions

Carry forward the recorded mode, pace and decisions. Decide ordinary implementation details and reversible development defaults; log material choices briefly. Ask the human only for owner-only blockers such as access, spending, missing business policy, a conflicting requirement, or expanded scope. Use an eligible planner for architecture/acceptance changes. Keep old and new plan revisions and the reason; affected workers acknowledge the change before continuing.

Do not end a continuous run after each child with “shall I continue?” Do stop at a chosen Checkpoint, a real blocker with no ready authorized work, the authorized endpoint, or a user stop. Report incomplete work honestly. Never create cron jobs, `/loop`, recurring monitors or cross-session promises to keep this workflow alive. Resume from durable files and actual available host tools.

## Communicate and finish

Talk in plain English: what the person can now do, what was checked, what is next, and any decision only they can make. Keep implementation diagnostics in the evidence unless needed to explain a blocker. Use the selected pace for updates.

Finish only when this epic's required outcomes, all child ACs, independent review and the authorized endpoint are satisfied. A goal completion tool, when available, is called only then; use its documented status rules. Otherwise leave the goal incomplete and report exact remaining child/AC IDs and the next action. Do not call planning, code completion or local testing a live release. Do not start another epic after completion.
