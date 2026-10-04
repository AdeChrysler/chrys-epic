# Default stack and dependency boundary

Apply this policy during definition and check it again before accepting each child. Record the concrete stack in the epic and goal; affected child contracts inherit it.

| Area | Default | How to apply |
|---|---|---|
| Web UI | shadcn/ui | Reuse existing compatible primitives and compose shadcn components. Inspect current repository setup before adding packages. A backend-only task does not gain a UI. |
| Persistent relational data | PostgreSQL | Use normal Postgres connections and repository-managed migrations. Prove persistence on real Postgres when required; mocks or SQLite do not establish Postgres behavior. A task without persistent data does not need a database. |
| Product services | Self-hosted where possible | Prefer in-process or self-managed authentication, storage, queues and scheduled jobs. Add only what the business outcome needs. |
| Deployment proposal | Railway | Use an existing suitable deployment setup or another user-selected host when appropriate. Keep app/configuration/migrations portable to another container host or VPS. Specify persistent storage and backup/restore when relevant. |

**Do not introduce Supabase, including its self-hosted distribution. Do not introduce required external SaaS for core application behavior by default.** This also rules out casually replacing it with another hosted backend, authentication, data, search, analytics, or storage service. An open-source package executed in the application or a component deployed in the team's own environment is allowed; “no third-party dependency” here means no required third-party *service*, not a ban on shadcn, Postgres, package registries or open-source code.

Railway or another chosen infrastructure host is an intentional hosting allowance, not an allowance for unrelated SaaS. GitHub is an optional planning store, and the person's existing Claude/Codex harness is an execution tool; neither should become a new dependency of the product being built. Avoid introducing mandatory research plugins or companion skills.

For genuinely unavoidable external functions, such as an explicitly requested payment processor or email delivery provider, describe the business need and propose an isolated integration with a recorded exception. Do not silently subscribe, add credentials, or treat “easier” as necessity. Record an exception only when the user explicitly chooses it. Keep secrets out of artifacts.

If the existing application uses a conflicting stack, report it and propose a bounded path. Do not pretend it already meets this policy, destructively migrate it, or introduce a second UI/database system for an unrelated change. Plan the requested outcome under the defaults, with a migration prerequisite or a clearly recorded user exception where needed. Let unrelated discovery continue.

Before plan readiness and each task's acceptance, inspect the proposed/actual packages, environment-variable names, imports, service calls, migrations and deployment configuration. Confirm shadcn/Postgres use where applicable and list any service exception with its authorization. A prose claim of compliance is not sufficient if the implementation introduces a hidden hosted dependency.
