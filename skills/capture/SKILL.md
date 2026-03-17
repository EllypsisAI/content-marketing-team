---
name: content-capture
description: >
  Frictionless idea capture that turns messy input into structured content items. Accepts anything — a story dump, a reaction to a LinkedIn post, a one-line idea, a URL — and determines pillar, format, and language without asking. Queues a structured draft. This skill should be used when the user says "I have an idea", "capture this", "I saw something", "client meeting story", "queue this", "save this idea", "content idea", or uses the /capture command.
version: 0.1.0
---

# Capture

Turn raw input into a structured content item. No clarifying questions unless intent is genuinely ambiguous. Decide pillar, format, and language. Queue it.

## Before Starting

1. Read `${CLAUDE_PLUGIN_ROOT}/references/pillars.md` — determine which pillar fits
2. Read `${CLAUDE_PLUGIN_ROOT}/references/voice.md` — understand voice for the hook
3. Read workspace `memory/observations.md` — check for relevant past feedback

## Input

Anything. A messy text dump, a URL, a reaction, a story from a client meeting, a one-liner. The skill's job is to make sense of it, not to ask for structure.

## Process

1. **Determine pillar.** Map input to P1 (implementation story/lesson), P2 (philosophy/framework/augmentation), or P3 (Danish landscape/data/news). If it spans two, pick the stronger angle.

2. **Determine format.** Use the content type → format mapping from `${CLAUDE_PLUGIN_ROOT}/skills/draft-social/references/linkedin-formats.md` Section 6. Implementation stories → text post. Frameworks → carousel. Data breakdowns → carousel. Opinions → text post. Audience questions → poll.

3. **Determine language.** Danish by default. English only if the topic is inherently English-domain or the user specifies.

4. **Write the hook.** One strong opening line using patterns from `${CLAUDE_PLUGIN_ROOT}/references/voice.md` Section 2 (scene entry or contrarian claim). This is a starting point, not final copy.

5. **Structure the item.** Create a queue file with frontmatter and a content skeleton: hook, core message (2-3 sentences), and suggested angle.

## Output

Save to workspace `queue/YYYY-MM-DD-slug.md`:

```yaml
---
title: "Hook line or working title"
pillar: 1|2|3
format: text|carousel|poll|newsletter
language: da|en
status: captured
date_created: YYYY-MM-DD
sources: []
---
```

Below the frontmatter: the hook line, core message, and angle notes. Enough for draft-social to work from, not a finished post. The sources array starts empty and gets populated by the research skill or during drafting.

## Key Behavior

Do NOT ask "what pillar?" or "what format?" — decide. If the decision is wrong, Sewar redirects. Log every redirect to `memory/observations.md` as a learning signal.
