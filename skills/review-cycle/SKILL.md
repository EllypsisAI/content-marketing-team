---
name: review-cycle
description: >
  Monthly performance review that analyzes publishing history, engagement patterns, pillar distribution, and accumulated observations to propose concrete strategy adjustments. Not "consider adjusting" — specific changes with reasoning. This skill should be used when the user says "monthly review", "what's working", "review performance", "content review", "how did this month go", or uses the /month command.
version: 0.1.0
---

# Review Cycle

Analyze the past month's content performance. Propose concrete changes to strategy, voice, and pillar distribution based on data and observations.

## Before Starting

1. Read workspace `memory/content-ledger.md` — all published content with performance data
2. Read workspace `memory/observations.md` — accumulated feedback, voice corrections, what resonated
3. Read `${CLAUDE_PLUGIN_ROOT}/references/pillars.md` — current pillar targets
4. Read `${CLAUDE_PLUGIN_ROOT}/references/strategy.md` — current strategy and KPIs

## Process

### 1. Publishing Stats

Count using code, not reasoning:
- Total posts published this month
- Posts per pillar (actual vs target: P1 40%, P2 35%, P3 25%)
- Cadence adherence (how many Tue/Thu slots were filled?)
- Newsletter editions published vs target (biweekly)
- Formats used (text/carousel/poll/newsletter distribution)

### 2. Performance Analysis

From content-ledger.md performance data (manually entered):
- Highest engagement posts — what pillar, format, topic, language?
- Lowest engagement posts — pattern?
- Comment rate trend (the metric that matters most)
- Any posts with 50+ or 100+ engagements (breakout content)?

### 3. Observations Synthesis

From observations.md:
- Voice corrections — is there a pattern? (e.g., "too formal", "needs more Danish")
- Feedback themes — what do redirects and rejections have in common?
- What resonated — topics, formats, angles that got positive feedback

### 4. Propose Changes

Be concrete. Not "consider posting more carousels." Instead:

- "Change pillar 3 from 25% to 20% because landscape posts consistently underperform. Redistribute 5% to pillar 1."
- "Switch Thursday format from carousel to text post — text posts got 2x more comments this month."
- "The 'CEO scenario' format (Danish, P2) generated the most engagement. Write 2 more next month."

### 5. Output

Monthly review document:

```
## Month [X] Review

### Publishing Stats
[Table: posts published, pillar distribution actual vs target, cadence adherence]

### What Worked
[2-3 specific highlights with why they worked]

### What Didn't
[1-2 specific lowlights with diagnosis]

### Strategy Adjustments (Proposed)
[Numbered list of concrete changes, each with reasoning]

### Voice Observations
[Any patterns from accumulated feedback]

### Next Month Focus
[1-2 sentence recommendation]
```

Present to user. If they agree with proposed changes, update `memory/state.md` with the new priorities and note the adjustments in `memory/observations.md`.
