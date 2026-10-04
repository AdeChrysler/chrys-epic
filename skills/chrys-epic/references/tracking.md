# Epic home and GitHub publication

One canonical home per epic: local Markdown or GitHub Issues. Ask the business owner which they prefer before choosing for them; a usable GitHub connection is an option, not implicit permission to publish. Reuse an explicit issue URL/local choice. If no answer or connection is available, prepare the local default and identify any assumed choice. If GitHub was explicitly requested, local preparation does not satisfy publication.

## Local default

```text
.epics/<slug>/
  EPIC.md
  GOAL.md
  tasks/T01-<slug>.md
  tasks/T02-<slug>.md
  runbook/execution.md
  runbook/delivery.md
  runbook/models.md
  runbook/stack.md
```

Use stable task IDs and relative links. `EPIC.md` owns the ordered status table, choices, decisions and any owner-only blockers. Each child owns its scope, ACs and evidence. `GOAL.md` points to those contracts; it does not duplicate their entire content. The runbook is a copy of the four relevant skill references so it travels with the plan. Evidence can go in a subdirectory when execution actually produces it. Do not create empty reports or fabricate future results.

Keep files inside the user's project. A same-machine handoff can use these files directly. For another machine, ensure they are actually available in that checkout or transferred through the user's chosen authorized channel; a private absolute path is not a portable artifact. Do not commit or push solely to make a link unless that action is authorized.

## GitHub mode

Read the chosen issue and relevant existing issues before drafting. Verify account, repository, and available issue-write capabilities. Search for matching task IDs/outcomes before creating anything. Selecting GitHub as the home authorizes scoped issue creation/update when the destination is clear; do not ask for the same permission again. A connection alone or an upstream repository used as reference does not authorize issue writes there.

Prepare the full epic and child bodies locally, review them, then publish the parent and each child with their ACs. Use native sub-issue relationships where supported and explicit dependency links. If unavailable, use a linked child checklist and state the limitation. Do not create milestone/programme tracker layers for this single-epic workflow.

Use structured body arguments or `gh ... --body-file`; never interpolate Markdown into shell code. Preserve newlines. Save each returned URL immediately in the local epic table, resolve dependencies to real URLs, and read back every body and relationship. A numeric GitHub issue ID used by a relationship API is not necessarily its issue number; follow the available tool/API schema. Do not move someone else's child from another parent.

Use a stable marker such as `<!-- chrys-epic:customer-intake:T01 -->` in published bodies. On timeout, search/read back the marker before retrying so ambiguous writes do not create duplicates. Before updating, fetch the current body and preserve intervening edits/comments. Stop writes on unresolved auth, rate-limit or concurrent-edit conflicts; keep completed URLs and remaining local bodies.

GitHub issue bodies become the source of truth. Mark local files `snapshot`, with source URL and retrieval/revision time. At execution/resume, read GitHub again rather than silently trusting the snapshot. If GitHub is inaccessible, report that synchronization is blocked; use cached contracts only under an explicitly recorded offline policy. Do not change the canonical home without a recorded decision.

Keep `GOAL.md` local even in GitHub mode, containing the actual epic URL and the runbook paths. In an issue, identify the local goal by its project-relative path as text, or use an actual accessible repository permalink; a relative `[GOAL.md](GOAL.md)` link inside an issue does not point into the user's project. Never use placeholder issue numbers in a ready handoff. If publication was requested but failed, mark the goal `draft`, explain the missing step, and do not claim issues exist.

Issue planning authority does not imply merge, production-data access, deployment, unrelated issue closure, or messages to other people. At execution, use the already-authorized status owner to update only this epic's children. Do not close a child for code completion while required runtime/review evidence is pending.
