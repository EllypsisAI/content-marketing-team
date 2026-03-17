---
description: Pipeline view — shows all content items by status
allowed-tools: Read, Glob, Grep, Bash
---

# Queue

Read all files in `queue/` and present a pipeline view grouped by status.

## Process

1. Read all markdown files in `queue/`
2. Parse frontmatter from each (title, pillar, format, language, status, date_created, date_scheduled)
3. Group by status: approved → in-review → drafted → captured
4. Sort within each group by date_created (newest first)

## Output

```
## Content Queue

### Approved ([count])
- YYYY-MM-DD-slug.md — Pillar [X], [Format], [Lang] — scheduled [date or "unscheduled"]

### In Review ([count])
- YYYY-MM-DD-slug.md — Pillar [X], [Format], [Lang] — review requested

### Drafted ([count])
- YYYY-MM-DD-slug.md — Pillar [X], [Format], [Lang] — drafted [X] days ago

### Captured ([count])
- YYYY-MM-DD-slug.md — Pillar [X], [Format], [Lang] — captured [X] days ago

### Published This Week ([count])
[from content-ledger.md, last 7 days]
```

If queue is empty, say so and suggest `/capture` or running discover-topics.
