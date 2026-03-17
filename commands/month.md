---
description: Monthly performance review — analyzes what worked, proposes strategy changes
allowed-tools: Read, Edit, Write, Bash, Grep
---

# Monthly Review

Trigger the review-cycle skill. Present the analysis. If Sewar agrees with proposed changes, apply them.

## Process

1. Invoke the review-cycle skill
2. Present the full review document
3. Wait for Sewar's response

## After Review

If Sewar agrees with proposed strategy adjustments:

1. Update `memory/state.md` with new priorities, cadence changes, or pillar rebalancing
2. Append to `memory/observations.md`:
   ```
   ### [DATE] — Monthly review: strategy adjustments applied
   - Changes: [list what changed]
   - Reasoning: [from review-cycle output]
   ```

If Sewar disagrees or wants modifications:

1. Discuss. Adjust the proposals.
2. Apply only the agreed changes.
3. Log what was rejected and why to observations.md — this is signal for future reviews.

## Performance Data Entry

If Sewar hasn't entered performance data for published posts, prompt:

"Before running the review, we need engagement data for published posts. For each post in the content ledger, can you share: engagement count (reactions + comments) and any notable comments?"

Update content-ledger.md entries with the performance data before running the analysis.
