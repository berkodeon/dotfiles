---
description: Show tracked questions, requested changes and decisions without starting work
---

Use the tasks-axi skill and the private Pi request ledger specified in Pi AGENTS.md.
Read it with the installed `tasks-axi` CLI, always passing
`--file "$HOME/.pi/agent/tasks/backlog.md"` after the command.
Show a concise table with ID, request, status and next action. Read the queued
and in-flight groups with `--fields held,hold_reason`; a held item remains in one
of those states internally, so display it as waiting with its reason, not as
ready to execute, and do not count it twice. Include at most five recent done
items in a separate section. Read full bodies only for unclear items. If the file is absent, say no requests
have been tracked yet; do not create a file just to answer this command.

This is a read-only status request, not permission to dispatch, change statuses,
install hooks or edit project backlogs. Explain that messages still queued in Pi
cannot be recorded until delivered to the agent. Extra requested focus: $ARGUMENTS
