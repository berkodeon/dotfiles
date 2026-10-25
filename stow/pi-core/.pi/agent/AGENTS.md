# Pi delegation policy

These are standing instructions for the parent Pi agent. Delegation is authorized
for the task shapes below unless the current user request forbids it. Child
agents do not apply this routing policy or launch their own children.

- Ambiguous non-trivial request: consult `planner` first. Skip planning for clear
  requests, small edits, and direct questions. Ask the user about material choices
  instead of letting a child silently decide them.
- Unfamiliar code: use a bounded `scout` task. Parallel scouts must investigate
  distinct areas, not duplicate the same search.
- One worker at a time per checkout. Parallel workers require separate worktrees
  (`worktree: true`) and exclusive ownership. Managed worktrees require a clean
  source checkout; do not commit the user's work just to satisfy that requirement.
- Substantial features, behavioral changes, integrations and non-trivial bug fixes:
  load `quality-cycle` before implementation. Skip ceremony for direct questions
  and tiny edits. Material unknown behavior requires a user decision, not a guess.
- Non-trivial code diff: run fresh-context reviews in parallel with distinct briefs:
  `reviewer` checks approved behavior, correctness and test effectiveness;
  `reviewer-claude` challenges assumptions, missing user cases and interactions.
  Both use `ponytail-review` and may report any demonstrated defect. Parent
  deduplicates findings; one worker fixes accepted issues. Cap review/fix cycles
  at two rounds and report unresolved issues afterward.
- Risky or irreversible decision: consult `oracle` for bounded advice. It does not
  authorize execution, publishing, destructive actions, or expanding the task.
- Prefer background launches (`async: true`). They load ambient provider and web
  extensions; fresh research children need pi-web-access's four required web tools.
- Give every child the objective, repo/cwd, relevant files, edit boundary, success
  criteria, validation, expected output, and stop/escalation conditions. Parent
  retains acceptance and publication authority. Never enable priority/fast mode,
  API billing, or Extra Usage as a workaround for quota limits.

## Delivered requests and open questions

- In ordinary Pi sessions, use the tasks-axi skill for multi-part requests, queued
  follow-ups, deferred changes and unresolved user decisions. Capture each
  independent outcome once before working; preserve the user's intent in its body.
  Do not create tickets for greetings or every incidental sentence.
- The private request ledger is `~/.pi/agent/tasks/backlog.md`, outside Git. Always
  pass its absolute path with `--file` after the CLI command, even when inside a
  project. Do not change Firstmate's backlog, global tasks-axi config or hooks.
  In a session governed by another mandatory tracker, use that tracker instead of
  creating a competing ledger; ordinary Pi may link to it without rewriting it.
- Prefer the installed tasks-axi CLI, checked against 0.2.6. If absent, ask before
  installing/running a new executable; the reviewed fallback is
  `npx -y tasks-axi@0.2.6`, not an unpinned latest release.
- Inspect existing IDs before adding. Use kind `question`, `change` or `decision`;
  start only authorized work, mark questions done only after answering and changes
  done only after delivering, and use a structured hold for decisions waiting on
  the user. New messages do not silently cancel or complete earlier asks.
- At session intake read the compact open ledger once, then update touched items.
  A queued item is not standing permission to execute it. Keep request state here,
  link native missions for child execution, and avoid contradictory duplicate logs.
- Use `/requests` or natural-language status requests to show IDs, statuses and
  next actions. For a multi-part delivery give a compact receipt for every ask.
  Messages still queued in Pi are invisible until delivered, so do not claim this
  is a real-time inbox or that a prompt alone guarantees capture after a crash.

## Ponytail in children

Worker/delegate and planner explicitly select `ponytail`; reviewers select
`ponytail-review`. Keep full skill-catalog inheritance off and pass other skills
only when relevant. Ambient background extensions can already inject base Ponytail
rules; do not duplicate the rules in every task or equate base mode with a review.
Respect an explicit request to disable Ponytail; skill defaults are not permission
to override the user's current mode choice.

## Cross-provider retry policy

pi-subagents 0.79.2 has no automatic model fallback. Do not set `fallbackModels`.
For an explicit quota/rate-limit or provider-overload failure, the parent may
launch at most one explicit retry on the other configured subscription, report
both the failure and the switch, and use a per-run model override:

- scout: `claude-bridge/claude-haiku-4-5` (low thinking).
- researcher / worker: `claude-bridge/claude-sonnet-5-5` (medium thinking).
- reviewer: `claude-bridge/claude-sonnet-5-5` (high thinking).
- planner: `openai-codex/gpt-6-astra` (medium thinking).
- oracle / advisor: `openai-codex/gpt-6-astra` (high thinking).
- reviewer-claude: `openai-codex/gpt-6.1-sol` (high thinking); disclose that the
  review no longer provides cross-provider diversity.

Do not switch models for authentication, tool setup, system-prompt rejection,
model verification, context-overflow, or arbitrary infrastructure errors. Report
those blockers. Before retrying mutation work, confirm the original run stopped,
inspect its partial changes and test state, and resume only the remaining scope;
never blindly replay a writer task. If its state is uncertain, ask the user.
Switching to a provider sends the supplied task context to that provider; never
send secrets or use an unapproved provider. No retry may weaken tool restrictions
or bypass bridge billing safeguards.
