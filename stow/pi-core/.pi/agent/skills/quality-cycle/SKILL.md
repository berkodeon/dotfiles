---
name: quality-cycle
description: Evidence-led work cycle for substantial features, behavioral changes, ambiguous requirements, integrations and non-trivial bug fixes. Challenge assumptions, expose product decisions, build meaningful tests, run distinct reviews and deliver a concise QA/decision handoff. Skip ceremony for direct questions and tiny edits.
---

# Quality cycle

The parent owns intent, decisions, request tracking and final acceptance. Children
supply bounded evidence, implementation or review. Use the smallest sufficient
cycle, not every role on every task. Existing project rules and explicit user
instructions win. Investigation is not permission to implement or publish.

## 1. Intake and evidence

- Read the actual request, supplied ticket, artifacts and relevant prior decisions.
  Reconcile delivered follow-ups with the private request ledger in Pi AGENTS.md;
  do not lose an earlier ask when a new message arrives. State the target repo.
- Inspect current code, callers, tests, real data and existing helpers. Use scout
  only when a bounded independent investigation earns its overhead. Research
  external facts only when local evidence cannot answer them; fetch primary sources.
- For bugs, reproduce the user's experience end to end as closely as feasible
  before editing. Record the exact failure and any simulated services or missing
  environment. Then add a focused regression check.
- Keep discovery bounded. Read existing evidence before repeating searches or
  launching children. Never infer performance or quality from model names.

## 2. Challenge the contract before coding

- Identify what the user wants to achieve, not just the requested mechanism. Name
  meaningful simpler alternatives and downstream effects; do not widen the task.
- For behavioral changes, draft a compact case matrix: case ID, input/condition,
  expected result, justification/source, approval state, test level and observation.
  Start with material boundaries, missing/invalid inputs, collisions/ambiguity,
  preservation/export behavior, failures and existing callers. Add combinations
  that exercise actual interaction risks, not a Cartesian product of everything.
- Classify expectations as specified, established by evidence, or requiring a user
  decision. A test asserting the current implementation is not independent evidence
  that its business rule is correct. Unknown behavior stays a question.
- Parent or planner proposes options, consequences and a recommendation. Ask only
  material product/authority choices; look up facts yourself. Put dependent
  questions in later rounds. Wait for the answer before implementing that choice;
  continue unrelated approved work when safe. Do not interrogate settled decisions.
- A new finding is not automatically new scope. Separate regressions, existing
  limitations, optional improvements and proposed extensions. Keep historical,
  rejected or already-closed findings closed unless new evidence changes them.

## 3. Implement the approved slice

- Use one writer per checkout, with explicit ownership and success criteria.
  Separate concurrent writers into approved isolated worktrees. Never commit the
  user's work merely to make isolation possible.
- Worker/delegate use the selected ponytail skill: reuse existing code, prefer the
  smallest complete change, preserve validation and error handling. If Ponytail's
  active rules are already injected, do not repeat their body in each handoff.
- Pass the relevant named testing skill when useful, such as pytest-patterns or
  playwright-best-practices. Fresh children do not receive the entire skill catalog
  by default. Include applicable personal/project constraints in the handoff.
- Test approved expectations independently of the implementation. Prefer a check
  that fails before the fix or without the feature. Include important negative
  cases and preservation invariants. Use targeted mutation checks only in a safe
  disposable environment; never leave deliberately broken code behind.
- Run the cheapest checks that prove the behavior, then relevant integration/E2E
  checks. Report actual commands and results. Do not call mocks a hosted UI test.
- For requested QA packs, create reusable inputs, independently justified expected
  outputs and a clear runbook. Use representative real data when appropriate and
  safe; avoid secrets. Do not generate a large pack when it adds no value.

## 4. Review distinct risks, not duplicate summaries

For non-trivial code diffs, use fresh-context independent reviews as authorized by
Pi AGENTS.md. Both see the same request, approved decisions, exact ref/diff and
validation evidence, with different primary questions:

- reviewer: Does the implementation satisfy the approved contract? Check callers,
  boundary/negative cases, security, test effectiveness, simplicity and readability.
  Use ponytail-review; inspect connected code, not just the changed lines.
- reviewer-claude: Is the contract complete for the user's goal? Challenge hidden
  assumptions, realistic missed cases, data/API/UI/export interactions and scope.
  Use ponytail-review as a quality baseline, not as a replacement for this question.

Both may flag any demonstrated defect; risk ownership is not blindness. Ask for
concrete examples and file/line or contract evidence. Keep hypotheses and optional
readability changes separate from proven bugs. Read-only reviewers do not edit.
The current builtin reviewer cannot run shell tests; parent/worker runs the checks
it requests. Never pretend inspection is execution or read-only prompts are an OS
sandbox. If a required provider/tool fails, stop that lane and disclose the blocker;
use only the explicit retry policy, not a hidden execution-mode fallback.

Parent deduplicates and judges findings. One worker fixes accepted in-scope issues;
rerun affected checks and review only the changed blast radius. At most two
review/fix rounds, then report remaining issues. Do not repeat for taste-only polish.
Use oracle only for a bounded hard tradeoff, contradictory evidence or decision drift.
If delegation tools are unavailable, disclose the missing independent review and
perform only the authorized direct work; do not claim a child reviewed it.

## 5. Deliver and reconcile

Give one concise, self-contained handoff, scaled to the task:

1. Outcome and changed files/artifacts.
2. Decisions: what was approved, what still needs the user, and any implementation
   assumptions worth exposing. Do not present a retrospective choice as approval.
3. Tests: relevant case IDs, exact checks/results and unverified environments.
4. Findings: fixed bugs, remaining risks, optional readability improvements and
   out-of-scope follow-ups with consequences and recommended disposition.
5. Request receipt: account for each delivered ask; mark answered/completed, in
   progress, queued or waiting. A report about work is not proof it was implemented.

Use a Kanagawa Wave Lavish surface when decisions or comparisons benefit from it,
not for every tiny reply. Treat submitted feedback as new input, record unresolved
choices and respect ended sessions. No commit, push, merge, deployment, destructive
cleanup, paid tier or billing change without applicable explicit authority.

Use tasks-axi for user-request truth and native missions for child run/decision
records. Link them rather than maintaining conflicting copies. On resume inspect
these records and partial work before relaunching; never blindly replay a writer.
