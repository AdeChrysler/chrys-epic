# Delivery mode and execution pace

Adapted from upstream Fast / Hybrid / Strict. **Careful is the business-facing name for Strict.** Mode determines the timing of proof; pace determines progress updates and human checkpoints. Neither changes the sequential task order, model rules, scope, required ACs, or publication/deployment authority.

## Delivery mode

| Mode | Business explanation | Required workflow |
|---|---|---|
| Fast | Get a working demo sooner; expect small correction rounds. | Focused checks and independent code review per child. Build verification journeys with the code. Batch real-runtime proof at each useful milestone on the authorized target. Keep unproven tasks open. |
| Hybrid | Move quickly, with extra checks around security and data. | Fast workflow plus independent security review before releasing any change that hits a tripwire below. |
| Careful (Strict) | Prove each change before it is released. | Real-stack self-QA and independent runtime review per child before merge, then deployed verification if deployment is the endpoint. UI changes also need independent interaction/visual checks. |

Recommend Fast only for reversible demos/WIP using synthetic data without shared-data or privilege risk. Recommend Careful for real client data, production/shared production databases, irreversible migrations, money/privacy risk, or go-live. Otherwise recommend Hybrid, including when risks are still unknown. State the one reason in ordinary English. Do not promise “hours” or “days” just from the mode name; estimate only from observed scope and evidence.

Ask once if not already chosen, record the person's words or `assumed`/`delegated choice`, and carry the choice into the epic and goal. Reuse it on resume. A worker never re-asks; it reports newly discovered risk to the coordinator. An execution packet with no mode uses Careful provisionally and records the omission. If risk increases, hold the affected release, explain why stronger checks are needed, and add the required gates. Continue unrelated authorized work within this epic. A request to go faster does not waive proof.

### Hybrid tripwires

Review the diff since the last release for authentication/sessions/tokens; permissions/tenant boundaries; shared-database or destructive migrations; exports/downloads/file access/audit logs; secrets in a client build; money, personal data, retention or deletion. A hit requires independent security review and targeted real-path tests before release. Integration-time migrations or grants also need review in Fast mode. A file-name scan alone cannot establish safety. Test the real request/session/database path, not only a synthetic helper that bypasses it.

### Proof and closure

Fast/Hybrid change when runtime checks happen, not whether outcomes must work. Collect test journeys from the first child and run them as soon as a milestone can be exercised. This is work inside the ordered children, not a parallel implementation lane.

For a write AC, exercise the normal authorized action, reload/read back the durable record, attempt relevant denied or cross-tenant writes, and prove the record remains unchanged after denial. Use isolated synthetic fixtures with a run prefix on the authorized target. UI acceptance needs the UI path when specified. Health checks, screenshots of a login screen, mocks and successful builds do not prove the interior workflow.

Bind evidence to source/candidate revision and environment. For deployed checks, record the deployment/release identity at both ends; discard mixed-release proof. Reviewers open raw responses, logs and captures behind summaries. Visual criteria are judged against the actual agreed reference, separately from functionality. Missing QA dependencies or credentials are a blocked check, not a product defect or a pass.

All required ACs must pass before `done`. Optional improvements may be parked with a reason and owner, but a failed required AC cannot become optional merely to close a task. Upstream's optional core-plus-follow-up closure policy is deliberately not the default here: it would add another business choice and can obscure this simplified acceptance contract. An explicitly requested scope change must preserve the original finding and record the revised contract.

An independent review is a fresh reviewer/session, not the worker rereading its own answer. If unavailable, mark `needs_review` and give a review handoff; do not fabricate independence. “Code reviewed,” “accepted on the test target,” and “verified live” are different gates. A locally scoped goal can finish after its local acceptance; it does not acquire a deployment requirement.

After two related failed correction rounds, stop symptom patching. An eligible planner reviews the root cause and defines one bounded whole-flow correction, including a minimal replacement where justified. Keep required findings visible. Report an owner-only blocker if no authorized route can resolve it; do not loop indefinitely or use a rewrite as permission for unrelated changes.

## Execution pace

| Pace | Behavior |
|---|---|
| Sprint | Continue through ready children automatically, one at a time. Keep narration brief; report milestones, material decisions and blockers. |
| Steady (default) | Continue automatically, one at a time. Give a short business-outcome update after each child. |
| Checkpoint | Finish the current child's recorded gate, report its outcome, and wait for the person's explicit instruction before starting the next. |

Ask about a deadline alongside pace. Under time pressure, propose a smaller useful scope or remove optional polish; do not weaken required acceptance. Careful + Sprint is valid, as is Fast + Checkpoint. Pace does not select a lower planning model, run multiple implementation children, change reasoning effort, or authorize extra spending. Carry the selected pace through resumes and corrections; do not ask again after every child in Sprint/Steady.
