---
name: content-research
description: >
  Deep research skill that enriches content items with real data, statistics, sources, and audience sentiment before drafting. Uses Perplexity for facts and trends, Reddit for real-world sentiment and pain points, and web search for Danish-specific data. This skill should be used when the user says "research this topic", "find data for this post", "enrich this", "what are people saying about", "get me stats on", "dig into this", or when a queue item needs facts before it can be drafted — especially carousels, data posts, and landscape content.
version: 0.1.0
---

# Research

Enrich a content item with real data before drafting. Sits between capture and draft-social. Without this step, data-heavy content either requires manual research or risks fabrication.

## When to Use

- Carousels that need statistics or data visualizations
- Landscape posts (Pillar 3) that reference Danish AI adoption numbers
- Any post making factual claims that need sourcing
- Newsletter deep dives
- Reactions to news or trends
- When discover-topics surfaces an opportunity that needs grounding

NOT needed for: personal stories (Pillar 1 implementation narratives), philosophy pieces based on Sewar's own frameworks, or content bank items marked Ready.

## Before Starting

1. Read `${CLAUDE_PLUGIN_ROOT}/immutable/rules.md` — anti-fabrication constraints are critical here
2. Read `${CLAUDE_PLUGIN_ROOT}/references/pillars.md` — the angle determines what to research
3. Read `${CLAUDE_PLUGIN_ROOT}/skills/research/references/audience.md` — know what the audience already understands vs what confuses them

## Process

### 1. Define the Research Question

From the queue item or user input, identify:
- What specific claims need sourcing?
- What data points would make this post concrete?
- What's the audience's current understanding? (audience.md)

### 2. Fact Layer — ~~research (Perplexity)

Use ~~research for:
- Current statistics (Danish AI adoption, SME numbers, funding programs)
- Recent news and developments (AI Denmark program, EU regulations, Danish company announcements)
- Competitor content analysis (what's already been said about this topic)
- Industry reports and surveys (Implement Economics, Dansk Industri, Statistics Denmark)

Search at least 3 different queries. Cross-reference numbers across sources — if a stat only appears in one place, note the single-source risk.

### 3. Sentiment Layer — Reddit

Use Reddit MCP to understand what real people are saying. Not for posting — for listening.

**Danish-specific subreddits:**
- `r/Denmark` — general Danish sentiment on AI, tech, work
- `r/dkfinance` — business/investment perspective on AI
- `r/copenhagen` — tech community sentiment

**Domain subreddits:**
- `r/smallbusiness` — SME pain points with AI (universal, maps to Danish SMEs)
- `r/artificial` — AI practitioner discussions
- `r/ChatGPT` — consumer AI sentiment, "ChatRot" discussions
- `r/consulting` — consultant perspective on AI implementation
- `r/SaaS` — relevant for KaaS/disposable software angles

**How to search:**
- `mcp__reddit__search_reddit` with topic keywords, filter by `time_filter: "month"` for recent sentiment
- `mcp__reddit__get_top_posts` on relevant subreddits to see what's resonating
- `mcp__reddit__get_post_comments` on high-engagement posts to find the real objections and pain points

**What to extract from Reddit:**
- Direct quotes that capture real sentiment (anonymized — never attribute to usernames)
- Common objections or fears (feeds into Pillar 2 augmentation content)
- Pain points described in the user's own language (not consultant-speak)
- Contrarian views that Sewar could respond to
- "ChatRot" and AI-skepticism threads (Danish-specific gold)

### 4. Compile Research Brief

Append findings to the queue file below the existing content:

```markdown
## Research Notes

### Key Statistics
- [Stat 1] (Source: [name], [URL], [year/date])
- [Stat 2] (Source: [name], [URL], [year/date])

### What People Are Actually Saying
- [Paraphrased sentiment from Reddit/forums — no usernames]
- [Common objection or pain point]

### Competitor Coverage
- [Who has written about this, what angle they took, what they missed]

### Angle Recommendation
Based on research: [specific angle that fills a gap or offers a contrarian take]

### Sources (with URLs)
- [Source name] — [URL] — [date accessed] — [what it provides]
```

### 5. Flag Gaps

If the research reveals:
- A statistic everyone cites but nobody can source → flag it, don't use it
- A topic that's been covered exhaustively → recommend a different angle or skip
- A claim Sewar makes in the content bank that can't be verified → flag for his input

## Output

The queue file is enriched with research notes. Status stays at `captured` — draft-social will use the research when drafting. The user can review the research brief before drafting or go straight to draft.

## Quality Rules

- Every number must have a named source. No "studies show" without the study.
- Reddit sentiment is paraphrased, never quoted with usernames. Respect anonymity.
- If two sources contradict, note both — let Sewar decide which to use.
- Prefer Danish sources for Danish-market claims (Statistics Denmark, Dansk Industri, Implement Economics over generic global surveys).
- If the research changes the angle, say so. "The content bank suggests X, but current data suggests Y would be stronger."
