---
name: draft-social
description: >
  LinkedIn content writer that produces publish-ready social posts in Sewar's voice. Drafts text posts, carousel outlines, poll structures, and newsletter drafts — all social-native, never excerpted from blogs. Reads voice patterns, anti-slop rules, and accumulated observations before every draft. This skill should be used when the user says "draft a post", "write this up", "turn this into a LinkedIn post", "draft from queue", "write a carousel", "write a poll", "draft newsletter", or when a captured item needs polishing into publish-ready content.
version: 0.1.0
---

# Draft Social

Turn a content item into a publish-ready LinkedIn post. One draft. Not options.

## Before Starting

1. Read `${CLAUDE_PLUGIN_ROOT}/references/pillars.md` — the angle for this pillar
2. Read `${CLAUDE_PLUGIN_ROOT}/references/voice.md` — voice patterns, cadence, guardrails
3. Read `${CLAUDE_PLUGIN_ROOT}/skills/draft-social/references/linkedin-formats.md` — format mechanics, character limits, algorithm signals
4. Read `${CLAUDE_PLUGIN_ROOT}/skills/draft-social/references/writing-craft.md` — anti-AI patterns, banned words, rhythm rules, how to sound human
5. Read `${CLAUDE_PLUGIN_ROOT}/immutable/rules.md` — hard constraints (anti-fabrication, anti-slop, operations)
6. Read workspace `memory/observations.md` — past feedback on drafts
7. Read workspace `CLAUDE.md` — current positioning context

## Input

A content item from `queue/` (with frontmatter) or raw input from the user. If from queue, honor the pillar/format/language already assigned unless there's a strong reason to change.

## Drafting Process

### For Text Posts

1. Write the hook (first 2 lines, under 210 chars). Use patterns from voice.md Section 2. This must survive the "see more" cutoff.
2. Build the arc: hook → context → insight → CTA. Target 1,300-1,900 chars total.
3. Format for mobile: one sentence per line, double line breaks between sections.
4. Add 3 hashtags at the end (1 broad, 1 mid-range, 1 niche).

### For Carousels

1. Write slide-by-slide outline: cover hook, problem setup (2-3 slides), core content (4-8 slides, one idea per slide), summary, CTA.
2. Target 6-12 slides.
3. Write companion text (3-5 lines) to post alongside the carousel.
4. Note: carousel visual design is done outside this skill. Output is the content per slide.

### For Polls

1. Question under 140 chars. Each option under 30 chars. 2-4 options.
2. Include an "Other → comment" option when possible.
3. Write companion text that frames the question and invites discussion.
4. Note: plan a follow-up post analyzing results.

### For Newsletters

1. Target 1,500-2,000 words. Structure: hook paragraph → setup → framework/insight (core) → personal story → CTA.
2. 80% value / 20% promotional max.
3. Note 3-5 post seeds that can be extracted as future LinkedIn posts.

## Self-Check

Before presenting the draft, verify against:

- [ ] Anti-slop: no banned patterns from `immutable/rules.md`. Read the draft aloud — does it sound like AI wrote it?
- [ ] Voice: matches Sewar's cadence (short declarative pairs at key moments, scene-entry or contrarian opening)
- [ ] The "only I" test: contains at least one detail that could only come from someone who implements AI at Danish companies
- [ ] The number test: at least one specific figure (for implementation posts)
- [ ] No fabricated statistics, cases, or quotes
- [ ] Format-appropriate length and structure
- [ ] Every factual claim has a source in the sources block

## Output

Update the queue file with the full draft. Change status from `captured` to `drafted`. Add internal notes and sources:

```yaml
---
status: drafted
confidence: high|medium|low
internal_notes: "Why this angle, what observations influenced the draft"
---
```

Below the draft content, add a sources block:

```markdown
## Sources (audit trail, not published)

- [Claim in the post] — [Source name, URL, date accessed]
- [Claim in the post] — [Source name, URL, date accessed]
- "Personal experience" — [Which client story or Sewar-provided detail]
```

Every factual claim in the draft must appear in this block. If the claim comes from Sewar's own experience (client stories, observations), cite it as "Personal experience" with what it references. If the claim comes from research, include the URL. If a claim has no source entry, it shouldn't be in the post.

Present the draft AND the sources block to the user for review. One version. If rejected, log the feedback to `memory/observations.md` and redraft.
