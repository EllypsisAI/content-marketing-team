---
name: discover-topics
description: >
  Strategic topic discovery that finds high-value content opportunities by cross-referencing pillar distribution targets, content-bank backlog, published history, and current trends in the Danish AI landscape. Ranks opportunities by pillar need, timeliness, and content-bank match. This skill should be used when the user says "what should I post about", "find topics", "content ideas", "topic research", "what's trending", "suggest topics", or when /week reveals a thin queue.
version: 0.1.0
---

# Discover Topics

Find the highest-value topics to post about next. Balance pillar distribution targets, what's already in the content bank, what's been published, and what's timely.

## Before Starting

1. Read `${CLAUDE_PLUGIN_ROOT}/references/pillars.md` — current distribution targets
2. Read `${CLAUDE_PLUGIN_ROOT}/references/strategy.md` — what's timely per the 90-day plan
3. Read workspace `memory/content-ledger.md` — what's been published (avoid repeats, check pillar balance)
4. Read workspace `content-bank.md` — what's in the backlog

## Process

### 1. Check Pillar Distribution

Count published posts per pillar in content-ledger.md. Compare against targets (P1: 40%, P2: 35%, P3: 25%). If a pillar is underrepresented, weight discovery toward it.

Use code to count, not reasoning. Accuracy matters.

### 2. Scan Content Bank

Check content-bank.md for items matching the pillar need. Priority 1-2 items that haven't been drafted are the first candidates — they require the least prep.

### 3. Scan for Timely Signals

Use ~~research to search for:
- Danish AI news (policy, research, company announcements)
- LinkedIn trending topics in the AI/business space
- Competitor posts from target accounts (Anders Baek, Dennis Uhrskov Raagaard, Julian Bent Singh)
- Anything Sewar could react to through the implementation lens

### 4. Score and Rank

For each topic candidate, evaluate:

| Factor | Weight |
|--------|--------|
| Pillar need (fills distribution gap) | High |
| Content-bank match (less prep) | High |
| Timeliness (trending or newsworthy) | Medium |
| "Only I" potential (Sewar has unique angle) | Medium |
| Format variety (different from recent posts) | Low |

### 5. Output

Ranked list of 3-5 topic opportunities:

```
## Topic Opportunities

### 1. [Topic]
- **Pillar:** P1/P2/P3
- **Format:** text/carousel/poll/newsletter
- **Content-bank item:** [ref if exists] or "New"
- **Why now:** [timeliness signal or pillar gap]
- **Angle:** [the specific take Sewar would have]
```

#1 is the recommendation. Sewar overrides if needed.

## What NOT to Discover

- Generic "Top 10 Tools" topics
- Topics outside the implementation lane
- Topics already well-covered in content-ledger.md
- Anything that positions Ellypsis as a tool vendor
