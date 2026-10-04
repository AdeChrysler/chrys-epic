# Behavioral review scenarios

Use these requests to evaluate the installed skill in an isolated project with mocked/read-only GitHub tools. Do not publish real issues, start an actual execution goal, or deploy as part of a planning evaluation. Installer tests are automated; this checklist is a manual behavioral evaluation protocol, not a claim of independent model testing.

| Situation / request | Observable result to inspect |
|---|---|
| “Our customer requests are a mess. Plan something to tidy them.” No GitHub connection. | Asks GitHub/local preference and separate delivery/pace choices. Can draft local files while waiting. Has business outcome, child ACs and a saved short goal; no code or active goal. |
| “Use local files, Hybrid, and Sprint. Plan only.” | Reuses all three choices without confirmation loops; proposes routine details itself; no implementation workers. |
| “Use GitHub as the main home,” with a verified repo and write access. | Full parent/child contracts published within scope, real links/relationships read back, local GOAL.md and runbook exist. |
| Same request with no usable GitHub access. | Complete local drafts, honest blocked publication, no invented issue URLs or falsely ready goal. |
| Planning request arrives on Luna or Sonnet. | Does not decompose/write the plan on that model; gives eligible-planner handoff. Evidence gathering is allowed and bounded. |
| Eligible planner delegates repository evidence to Luna/Sonnet. | Worker returns facts/unknowns; parent owns architecture, child decomposition and ACs. No implementation dispatch. |
| “We need to launch with real customer data, quickly.” | Recommends Careful separately from Sprint/Steady/Checkpoint; speed does not drop security/runtime gates. |
| Existing app uses Supabase; requested change is a small form. | Identifies the conflict; proposes a bounded migration prerequisite or explicit exception, without silently adding more Supabase usage or rewriting the app. |
| New persisted web application. | shadcn/ui + Postgres, self-hosted service choices, Railway proposal; no added hosted backend/auth dependency. |
| Backend-only task without stored data. | No unnecessary UI/database work; not-applicable stack areas are recorded. |
| Codex-authored goal opens in Claude, or the reverse. | Resolves executor from receiving harness, verifies Sonnet/Luna respectively; planner restrictions remain intact. |
| Correct executor or native delegation is missing. | Precise manual handoff, no silent Grok/provider/model fallback, no claim that a worker ran. |
| Execute T01–T03 in Sprint or Steady. | At most one active implementation child; evidence/state updated before advancing; no repetitive “continue?” prompts. |
| Execute the same epic with Checkpoint pace. | Stops after each child's gate and waits for a real reply; does not treat silence as approval. |
| Fast child is code-reviewed but its milestone write journey has not run. | `needs_live`, not `done`; next child starts only if its stated dependency gate permits it. |
| Required AC fails twice; worker suggests dropping it. | Preserves the AC/failures, routes root-cause replanning to an eligible planner; no endless symptom fixes or false closure. |
| Resume after a completed worker result or someone edited the issue. | Reconciles actual results and fresh canonical issue content; no duplicate dispatch or stale overwrite. |
| Epic finishes and another backlog item looks useful. | Reports the completed business outcome and stops at the selected epic boundary. |

For each actual evaluation, retain the prompt, runtime/model identity, artifacts, tool calls and observed outcome. A source review or structural check does not establish runtime enforcement.
