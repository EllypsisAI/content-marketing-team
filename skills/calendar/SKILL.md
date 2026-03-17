---
name: content-calendar
description: >
  Content calendar manager that maps queued content to publishing slots, identifies gaps, and suggests fills. Shows this week and next week's schedule against the target cadence (Tue/Thu/Sat + biweekly newsletter). This skill should be used when the user says "show me the calendar", "what's scheduled", "plan next week", "when should I post this", "calendar view", or as part of the /week command.
version: 0.1.0
---

# Calendar

Map queued content to publishing slots. Show what's planned, what's missing, and what to fill gaps with.

## Before Starting

1. Read `${CLAUDE_PLUGIN_ROOT}/references/strategy.md` — target cadence (Tue/Thu/Sat optional + biweekly newsletter)
2. Read workspace `memory/state.md` — current week's plan
3. Read workspace `queue/` — all items and their statuses
4. Read workspace `memory/content-ledger.md` — recent publishing history
5. Read workspace `content-bank.md` — backlog items for suggesting fills

## Process

1. **Map current queue.** List all items in queue/ by status (captured, drafted, in-review, approved). Note scheduled dates from frontmatter.

2. **Build calendar view.** Show this week and next week:

```
## This Week (Mar 10-16)

| Day | Slot | Content | Status |
|-----|------|---------|--------|
| Tue | Post | 2026-03-10-chatrot-post.md (P2, Text, DA) | approved ✓ |
| Thu | Post | — | EMPTY |
| Sat | Post (optional) | — | EMPTY |
| Biweekly? | Newsletter | Not due this week | — |
```

3. **Identify gaps.** Flag empty slots. Check if the gap creates a pillar imbalance (e.g., three P2 posts in a row, no P1).

4. **Suggest fills.** For each empty slot, recommend from:
   - Queue items that are `drafted` or `approved` (ready to go)
   - Content-bank items matching the pillar need
   - If nothing fits, flag that discover-topics should run

5. **Update state.md** with the current week plan after user confirms.

## Output

Calendar view for this week and next week. Empty slots flagged with suggested fills. Pillar balance check.

## Cadence Rules

- Tuesday + Thursday are core. Saturday is optional but recommended during launch phase.
- Minimum 12-hour gap between posts (algorithm penalty otherwise).
- Newsletter is biweekly — check when the last one published and whether this week is a newsletter week.
- Post between 8-10 AM CET for maximum first-90-minute engagement window.
