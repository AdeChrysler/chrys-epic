<img src="assets/icon.svg" width="64" height="64" alt="">

# chrys-epic

Turn a business idea into one focused epic, small ordered tasks, and a clear definition of what “finished” means. Built from [AdeChrysler/chrys-engineering](https://github.com/AdeChrysler/chrys-engineering), narrowed for business owners using Claude or Codex.

Tell the agent the outcome you want. It plans the work, saves it in GitHub Issues or project Markdown, and gives you a short `/goal` instruction. When you start that goal, it works through the epic's children one by one.

## Start here

After installation, open the project you want to improve and say:

> Use chrys-epic to plan a customer intake system. Our team should be able to record a request, assign someone, and see what still needs attention. Make routine decisions for me. Plan it first.

You can invoke it directly as `/chrys-epic` in Claude Code or `$chrys-epic` in Codex. Select Astra or Sol for Codex planning, or Fable or Opus 5.5 for Claude planning. The skill checks the active model and explains any needed switch.

The agent asks only for missing choices:

| Choice | Options |
|---|---|
| Main home for the epic | GitHub Issues, or Markdown in your project. It asks about GitHub first; project files work without a connection. |
| Delivery mode | **Fast:** a demo sooner, with checks in batches. **Hybrid:** fast progress plus security/data checks. **Careful:** prove each change before release. |
| Execution pace | **Sprint:** brief updates, keep moving. **Steady:** keep moving and update after each child. **Checkpoint:** wait for your review after each child. Include a deadline if you have one. |

Hybrid and Steady are the usual recommendations; production/client-data work needs Careful. You can combine Careful with Sprint. Already-recorded choices are reused, and routine technical decisions stay with the agent.

Review the business outcome and exclusions. The agent will save `.epics/<your-epic>/GOAL.md`, even if the main epic is in GitHub, and explicitly tell you which `/goal` line to copy. Open the same project, paste that line, and it reads the full plan from the file. If `/goal` is unavailable, paste the same sentence without the command prefix. No background goal is created merely by planning.

For later work, say “Continue the epic in `.epics/customer-intake/GOAL.md`” or provide its GitHub link. It recovers progress and continues the selected epic. It does not start the rest of your backlog.

## Install or share

Share this repository/folder, or the complete `skills/chrys-epic` folder. Do not copy only `SKILL.md`: the references and templates are part of the skill. No GitHub connection, Grok account, companion Chrys skill, or package install is required. The installer uses Python 3.9+ and its standard library.

Download the public repository:

```bash
git clone https://github.com/AdeChrysler/chrys-epic.git
cd chrys-epic
```

Then install into the project you want to work on:

```bash
python3 scripts/install.py --host claude --project /path/to/project
```

For Codex:

```bash
python3 scripts/install.py --host codex --project /path/to/project
```

Or install for all projects under your account:

```bash
python3 scripts/install.py --host claude --user
python3 scripts/install.py --host codex --user
```

The installer copies the whole skill, leaves application/configuration files alone, and refuses to overwrite a different existing installation. An identical reinstall is harmless. To update a modified/older copy, move that skill directory to a backup outside the skills discovery folder, then rerun the command. Open a new agent session if the skill is not discovered immediately.

Manual installation also works: copy `skills/chrys-epic` into the project's `.claude/skills/` for Claude Code or `.agents/skills/` for Codex. User-wide locations are `~/.claude/skills/` and `~/.agents/skills/`. These follow the hosts' [Claude skills documentation](https://code.claude.com/docs/en/skills) and [Codex local skill documentation](https://learn.chatgpt.com/docs/build-skills). Hosts with different discovery paths can read the complete skill directly.

## Defaults carried into every plan

- Web UI uses **shadcn/ui**; persistent relational data uses **PostgreSQL**.
- Prefer self-hosted product services. No Supabase, including self-hosted Supabase, or new required external SaaS by default. Open-source libraries are allowed.
- **Railway** is the default deployment proposal; another chosen/existing suitable host is supported. Apps stay portable, and deployment needs its own authorization.
- Planning and replanning use **Astra / Sol** or **Fable / Opus 5.5**. Luna/Sonnet can gather evidence, but cannot own planning.
- Implementation defaults to **Luna in Codex** and **Sonnet in Claude**, with one child active at a time. Required checks remain required even in Fast mode.
- Agent-facing tasks are compact contracts with IDs, dependencies, scope, ACs and proof. Human-facing explanations use plain English and business outcomes.

These rules are skill instructions and readiness checks, not host-level model locks. The agent must verify actual model/tool availability and report a missing capability rather than claim it switched models. The saved goal includes a portable runbook so a fresh execution session does not depend on another chat's memory.

## Maintenance

See [UPSTREAM.md](UPSTREAM.md) for the exact upstream revision and deliberate differences. The upstream skill and this focused variant have different names, so they can coexist; invoke `chrys-epic` for this workflow.

Run the installer checks with `python3 -m unittest discover -s tests -v`. The [scenario checklist](tests/scenarios.md) covers the skill's planning and handoff contracts; it is not a claim that every host/model combination has been exercised.
