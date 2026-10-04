---
name: chrys-epic
description: "Turn a business request or messy backlog into one focused epic, ordered child tasks with acceptance criteria, and a saved /goal handoff. Use for epic planning, task definition, or revising an epic in GitHub Issues or local Markdown. Planning alone does not start implementation."
---

# Chrys Epic

Help a business owner say what they want, understand what will improve, and give an execution agent one unambiguous epic. This is a focused adaptation of AdeChrysler/chrys-engineering, not its general engineering or monitoring workflow.

**Deliver:** one epic → ordered child tasks → observable acceptance criteria → `GOAL.md` → a short copyable `/goal` command. Plan and hand off by default. Do not launch implementation, create an active goal, deploy, or schedule monitoring just because someone requested a plan or installed this skill. When the user explicitly asks to execute an existing epic, recover its goal and follow [execution.md](references/execution.md); do not replan completed work.

## 1. Recover context and use an eligible planner

Read project instructions, the requested epic, existing decisions, relevant source/tests, and dirty work. Identify the business outcome, current gap, preserved behavior, exclusions, repository and revision. Label unknowns; do not invent files, API capabilities, credentials, model availability, or test results.

Read [models.md](references/models.md). Planning, decomposition, acceptance design, architectural decisions, and replanning belong **only to OpenAI Astra or Sol, or Anthropic Fable or Opus 5.5**. Luna and Sonnet may gather bounded evidence; they must not own planning. Verify the actual model before substantive planning. If ineligible or unverifiable, collect facts only and give one concrete instruction for moving the plan to an eligible model.

## 2. Ask once about the business choices

Ask early, in plain English, for the missing choices below. Read [delivery.md](references/delivery.md) before recommending the mode. Bundle the questions; reuse answers already in the conversation or accepted epic. An explicit choice is enough; do not ask the person to confirm it again. Child workers inherit the recorded choices and never repeat intake.

1. **Where should the main epic live?** “Would you prefer GitHub Issues as the main place for this epic, or Markdown files in this project?” Offer GitHub when connected; explain that project files work without a connection. An explicitly supplied issue or local-only request answers this question. A configured connection alone does not answer it. If GitHub is unavailable, still ask the preference, then use local Markdown for preparation. Without a supplied issue/usable connection or after an unanswered preference, local Markdown is the default. Record an unanswered choice as assumed, not approved. If GitHub was requested, local files remain a draft until publication succeeds or the user accepts local as the final home. See [tracking.md](references/tracking.md).
2. **How carefully should we deliver?** Fast: a demo sooner, checks in batches. Hybrid: fast progress with extra checks around security and data. Careful: prove each change before release. Recommend Hybrid unless the risk check indicates Fast or Careful. `Strict` from an upstream plan means `Careful` here.
3. **How should execution move?** Sprint: keep moving with brief updates. Steady: keep moving and report after each child task. Checkpoint: pause after each child for your review. Ask for any deadline in the same question. Recommend Steady. These choices are separate from delivery mode; all execute child tasks one by one.

Continue read-only discovery and local drafting while answers are pending. If the person leaves choices to you, choose and record them. With no answer, use provisional local / risk-recommended mode / Steady; never treat silence as permission to publish or run. Present these defaults in the final handoff so an explicit start can adopt them. Do not invent budgets, time promises, or deployment approval.

## 3. Apply the stack and make routine decisions

Read [stack.md](references/stack.md) and carry its concrete selections into the epic, affected children and goal:

- **shadcn/ui** for web UI; **PostgreSQL** for persistent relational data.
- Prefer self-hosted components. **No Supabase, including self-hosted Supabase, and no new external SaaS runtime dependency by default.** Open-source packages that run inside the project are allowed.
- **Railway** is the default deployment proposal; an existing suitable host or another explicitly chosen option is fine. Keep the application and database portable. Hosting is distinct from outsourcing product features to SaaS. Selecting a host does not deploy anything.

Choose ordinary implementation details yourself from repository evidence. Log the choice, reason, and reversal path briefly. Ask only about missing business outcomes/policy, money, access, incompatible constraints, or consequential scope changes. Do not ask a business owner to choose libraries, table names, code structure, or routine development defaults. Do not turn existing stack differences into an unrequested migration.

## 4. Write the epic and child contracts

Use [epic.md](assets/epic.md) and [child.md](assets/child.md). The local default is `.epics/<slug>/EPIC.md`, with children in `.epics/<slug>/tasks/`. In GitHub mode, issue bodies are canonical; the local epic is a clearly dated snapshot. Keep **one selected epic** in the execution goal. Put unrelated ideas in a short parking list, without creating extra epics unless asked.

Optimize artifacts for the next agent: stable IDs, concise records, explicit dependencies and gates, paths/source evidence, acceptance-to-proof mappings, and state. Keep chat explanations focused on business outcomes. Avoid repeated narratives, ticket boilerplate, unnecessary hierarchy, and a second manifest duplicating the same plan.

Each child must have:

- One useful outcome; bounded included/excluded behavior and files, or a bounded discovery prerequisite when source is not yet known.
- A dependency and the exact gate it needs: `code-reviewed`, `accepted`, or `released`. Order tasks accordingly; never invent a cycle that needs a later task to start an earlier one.
- A concrete implementation direction and inherited stack constraints. Keep contracts and source references accessible to a fresh session.
- Stable AC IDs with input/actor/state → action → observable result. Include meaningful failure, persistence, permission, or recovery cases. “Build passes” and “uses shadcn” alone are insufficient.
- Proof for each AC: command or click path, fixture/expected result, target, and artifact. For writes, include read-back after reload and relevant denied writes that leave data unchanged. For UI, check the actual interaction plus applicable desktop/phone, keyboard, loading/empty/error and visual requirements.
- Completion gate, reviewer, and status. Required acceptance remains required in every delivery mode. A later QA batch means `needs_live`, not `done`.

Start proof work with the first implementation child; do not postpone writing the verification journeys until the end. For a large epic, group tasks under useful business milestones inside the epic, without adding more tracker layers. Trace the connected user journey across tasks. Discovery tasks resolve unknown contracts before their consumers start. Do not impose a fixed task/AC count or hour estimates.

## 5. Check readiness and save the handoff

Check every AC has appropriate proof, every dependency resolves, the task order is executable with one active child, the stack is compliant, the planner is eligible, and the native executor route is explicit. Preserve original findings and completed tasks on revisions. Mark unresolved prerequisites honestly. This review checks the definition; no implementation is being tested.

Use [tracking.md](references/tracking.md) for GitHub publication only when selected/authorized. Read back actual issue bodies and parent/child links. Keep the full contracts in issues, not just links to private files.

Always create `.epics/<slug>/GOAL.md` from [goal.md](assets/goal.md), **even when GitHub is canonical**. Fill in the actual epic URL or local path, project root, ordered task source, mode, pace, model routes, stack, authorized endpoint, evidence and stop conditions. Copy [execution.md](references/execution.md), [delivery.md](references/delivery.md), [models.md](references/models.md), and [stack.md](references/stack.md) into `.epics/<slug>/runbook/` so the next session has the complete instructions without a hidden skill dependency. Do not overwrite a customized runbook on resume without reviewing it.

`GOAL.md` must contain the exact, short `/goal` line the person will copy, plus the detailed execution brief. Replace all template placeholders. Use a quoted, project-relative path; resolve it from the recorded project root. The line points to `GOAL.md`, which points to the real epic. Do not cram the whole plan into the command. Do not start a goal to test the handoff.

End in plain English: what the epic will achieve, where it lives, how many children, chosen/default mode and pace, any owner-only blocker, and the next action. Explicitly say **“Open this project in Claude or Codex, then copy:”** and print the exact `/goal` line. Link `GOAL.md`. If the host has no `/goal` command, tell them to paste the same instruction without `/goal`; do not claim a persistent goal was created. If the plan is blocked, label the goal a draft and say what must be resolved before copying it. A plan is ready only when its actual prerequisites are ready.
