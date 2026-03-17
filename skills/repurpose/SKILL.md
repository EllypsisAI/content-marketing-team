---
name: content-repurpose
description: >
  Creates standalone LinkedIn posts from existing long-form content. Takes a blog post, newsletter edition, or article and extracts 3-5 social-native posts — not excerpts, but original posts inspired by the source. This skill should be used when the user says "repurpose this blog post", "create social posts from this", "derivatives from this article", "turn this newsletter into posts", "extract posts from", or when long-form content needs social distribution.
version: 0.1.0
---

# Repurpose

Extract 3-5 standalone LinkedIn posts from a long-form source. Each post must stand alone — native social content, not a truncated blog excerpt.

## Before Starting

1. Read `${CLAUDE_PLUGIN_ROOT}/references/pillars.md` — determine angles per derivative
2. Read `${CLAUDE_PLUGIN_ROOT}/references/voice.md` — voice patterns
3. Read `${CLAUDE_PLUGIN_ROOT}/skills/draft-social/references/linkedin-formats.md` — format mechanics
4. Read `${CLAUDE_PLUGIN_ROOT}/immutable/rules.md` — anti-fabrication, anti-slop constraints
5. Read workspace `memory/observations.md` — past voice feedback

## Input

A published blog post, newsletter edition, or article. Either a URL (use ~~research to fetch) or pasted text.

## Process

1. Read the source content fully. Identify the core insights, not the structure.

2. Find 3-5 standalone angles. Each must work as an independent LinkedIn post for someone who hasn't read the source. Look for:
   - A contrarian claim buried in the body
   - A specific data point or result
   - A framework or mental model
   - A story or anecdote
   - A question the article answers that could be a hook

3. For each derivative, determine format (text post, carousel, poll) using the format selection matrix in linkedin-formats.md Section 6.

4. Draft each as a complete post following the draft-social skill's process. Apply voice patterns and anti-slop checks.

## Output

3-5 queue items saved to `queue/YYYY-MM-DD-slug.md`, each with frontmatter:

```yaml
---
title: "Hook line"
pillar: 1|2|3
format: text|carousel|poll
language: da|en
status: drafted
date_created: YYYY-MM-DD
source: "Title or URL of original content"
---
```

Present the set to the user with a one-line summary per post explaining the angle.
