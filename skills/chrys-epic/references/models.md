# Model routing

Read before planning and again when a new execution or review session starts. These are workflow rules, not model-switching machinery. A Markdown skill cannot enable a model, change an account, or guarantee a host's routing. Use the current host's exposed model picker, runtime identity, or supported agent tool; never pretend a prompt changed the model.

| Responsibility | OpenAI / Codex harness | Anthropic / Claude harness |
|---|---|---|
| Plan, decompose, choose architecture, write ACs, replan | Astra or Sol | Fable or **Opus 5.5** |
| Gather evidence for an eligible planner | Luna | Sonnet |
| Implement a bounded accepted child, fix it, self-check | **Luna** | **Sonnet** |
| Independent implementation review | A fresh Luna reviewer; eligible planner for difficult security/design judgment | A fresh Opus 5.5 reviewer; Fable if available and selected |

Keep an already eligible planning model. Do not choose Luna or Sonnet for planning, even in Fast mode or under deadline pressure. A low-cost evidence worker returns observations, source paths, commands/results, and unknowns; the eligible planner interprets them and owns the plan. An independent *planning* review also needs an eligible planner, not the implementation-review defaults above.

Resolve available native model IDs at runtime. Examples, when actually exposed, include `gpt-6-astra`, `gpt-6.1-sol`, `gpt-6-sol`, `gpt-6-luna`, and `claude-opus-5-5`; resolve Fable and Sonnet to their supported host IDs. Do not guess availability from these examples or use an unverified `opus` alias that could resolve to another version. Preserve a requested eligible version. Use supported reasoning defaults unless the user has chosen an effort; pace is not an invented CLI speed flag.

Record `role / harness / requested model / observed model / verification source` in the plan and each worker result. Verify the planner now; label future worker identities `verify at dispatch` until observed. “Use Luna” in a packet is not proof Luna ran.

At execution, the receiving harness determines the native executor, even if the original plan was made in the other harness. Record the resolved route before edits: Codex → Luna, Claude → Sonnet. No Grok dependency, cross-provider relay, or silent model substitution. A planning-model coordinator may dispatch **one** native implementation worker at a time; it must not silently do implementation itself on the expensive planning model. Pass the child, epic, goal, and runbook to the worker, not an unbounded “build everything” assignment.

If native delegation or the required model is unavailable, prepare the bounded handoff and give the user one concrete step to open it on the correct native model. If the current session already runs that executor, it may implement directly. Unknown/other harnesses require a verified supported route before implementation. Do not claim a worker or review ran if it did not.

New architecture, changed ACs, conflicting business rules, or an enlarged scope go back to an eligible planner. An executor can choose routine code details inside the accepted contract and gather more facts; that is not permission to rewrite the plan. For planning during execution, use an eligible native planning subagent if supported, or save the question and hand it back to an eligible session.

Evidence and independent review helpers may run when authorized and useful. Their assignment must exclude implementation of another child. Model selection never authorizes extra paid services, credential changes, or a different provider.

For host configuration details, consult the actual available tools and current official [Codex subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents), [OpenAI model catalog](https://developers.openai.com/api/docs/models), and [Claude model configuration](https://code.claude.com/docs/en/model-config). These document capabilities; the restricted role choices above are this workflow's policy.
