# Sewar's Voice — Reference File

For use by `draft-social` and `refine` skills. This file teaches Claude to write in Sewar's actual voice — not a generic "professional but approachable" approximation.

---

## 1. The Signature Cadence

Sewar's rhythm is **short declarative pairs**. Two sentences. Period. Period. The second sentence flips, extends, or reframes the first.

**Examples from his actual writing:**

> "Automation is loud. Augmentation is profitable."

> "Software is a commodity now. Knowledge is power."

> "De løj for dig. Systemet gjorde dig til specialist fordi de havde brug for tandhjul."

This is his most recognizable pattern. When drafting for him, the hook and key turns should use this rhythm. Not every sentence — just the moments that matter.

**Anti-pattern:** Long compound sentences with multiple clauses. Sewar doesn't hedge within sentences. If it needs a qualifier, it gets its own sentence.

---

## 2. How He Opens

### Scene entry, not context setup

His strongest openings drop the reader into a specific moment. No preamble. No "In my work as an AI consultant..."

**His actual opening lines (ranked by strength):**

| Line | Why it works |
|------|-------------|
| "I sat with a woman who was opening 10 windows to answer a single email about rust on a ship hull." | Scene. Specific details. Visual. The reader is there. |
| "De løj for dig." | Three words. Provocative. The reader has to keep going. |
| "Most AI projects fail at the translation layer, not the technology." | Contrarian claim. Immediate tension with common belief. |
| "The better I get at my job, the harder it is to get paid fairly for it." | Personal contradiction. Honest. Relatable to every consultant. |
| "Your CEO read an article about AI. Now you need AI." | Scenario. The reader recognizes their own life. |

**Pattern:** His best openings are either (a) a scene with a specific detail, or (b) a contrarian claim stated flatly. He never opens with a question (except rhetorical), and never opens with a definition or explanation.

**The test:** If the opening could be written by anyone on any topic, it's wrong. If it contains a detail that only someone inside the work would know, it's right.

---

## 3. The Contrarian Flip

Almost every strong Sewar piece takes a common assumption and inverts it. This isn't him being controversial for attention — it's him describing what he actually sees vs. what people expect.

**Structure:** `[Common belief] is wrong/backwards/not the real issue. [What actually happens] is.`

| Common belief | His flip |
|--------------|----------|
| AI is a technology problem | "Most AI projects fail at the translation layer, not the technology." |
| AI replaces humans | "You don't remove the pilot. You build a cockpit that deserves them." |
| Software is the product | "Software is a commodity. Knowledge is power." |
| AI makes everything easier | "I felt dumber after my first client than before. That meant I was learning." |
| More AI tools = more value | "Is there at least one detail in this post that only I could have written? If no, it's automation. If yes, it's augmentation." |
| Specialism is the path | "De løj for dig. Systemet gjorde dig til specialist fordi de havde brug for tandhjul." |
| The future = what becomes unnecessary | "The question is always 'what becomes possible?' not 'what becomes unnecessary?'" |

**Instruction to Claude:** When drafting a Sewar post, identify the assumption the audience holds about the topic. State it. Then show what Sewar has actually observed. The flip should feel like a revelation, not an argument.

---

## 4. Metaphor as Argument

Sewar doesn't use metaphor decoratively. He uses it as the argument itself. The metaphor IS the insight — remove it and the point collapses.

| Metaphor | What it argues |
|----------|---------------|
| "You don't remove the pilot. You build a cockpit that deserves them." | AI augmentation isn't about removing humans — it's about building better systems around human judgment |
| "Organizational scar tissue" | The informal workarounds in a company aren't dysfunction — they're evolved responses to real complexity. Automating past them destroys information |
| "Excel on steroids" | AI tools aren't enterprise software projects. They're the modern equivalent of the Excel sheet Bente from accounting built. Reframes perceived cost from 200K to quick internal tool |
| "Tandhjul" (cogs) | The specialization narrative wasn't about your growth — it was about the system's need for interchangeable parts |
| "SaaS is the hammer, AI is the carpenter" | Technology layers don't replace each other — they change who uses them and how |

**Anti-pattern:** Generic metaphors that could apply to anything. "AI is a journey" / "building blocks" / "the tip of the iceberg." Sewar's metaphors are specific to the situation and can't be transplanted to another context.

**Instruction to Claude:** Use metaphor only when it reframes the argument. If the metaphor is removable without losing the point, it's decoration — delete it.

---

## 5. Danish vs English Voice

Sewar is bilingual, but he's not the same writer in both languages.

| Dimension | Danish | English |
|-----------|--------|---------|
| **Emotional register** | Higher. More provocative, more intimate | More analytical, more measured |
| **Sentence length** | Shorter. Punchier. | Slightly longer. More structured |
| **Opening style** | Provocative ("De løj for dig") | Scene-setting or contrarian claim |
| **Humor** | Dry, cultural, implicit | Occasional, usually through absurd specificity |
| **Tone** | Speaking to an equal. "Du" (informal you). Direct | Slight authority voice. Still direct, but more considered |
| **Cultural layer** | Uses Danish concepts natively (janteloven, implied but never named) | Translates for international reader |
| **Best for** | Implementation stories, trust-building, opinion pieces, CEO scenarios | Named frameworks, data analysis, "signature pieces" for broader reach |

**The split rule:** If the post is about a feeling, a client relationship, or a Danish-market observation → Danish. If it's about a framework, data analysis, or concept intended for broader reach → English.

**Critical:** Never translate directly between languages. The Danish version should feel like it was born in Danish. The English version should feel like it was born in English. Different rhythms, different cultural shortcuts.

---

## 6. What He Avoids (Voice Guardrails)

These are things Sewar never does. If a draft contains them, it's not his voice.

| Avoid | Why | Instead |
|-------|-----|---------|
| Jargon dumping (RBV, appropriability, NLP pipeline) | His audience is non-technical business leaders | Use the concept, explain it through example, never name the academic term |
| Hedging language ("perhaps," "it could be argued," "in some cases") | He states what he observes. If it's uncertain, he says "I don't know yet" | Direct statements. "This works." "This doesn't." "I haven't tested this enough to say." |
| Exclamation marks and emoji | Not his tone. Danish professional communication is understated | Period. The weight comes from the word choice, not the punctuation |
| "5 tips" / "7 ways" / listicle framing | His frameworks are rooted in specific experience, not generic advice | One insight, fully developed. Or a named framework with a story behind it |
| "I'm excited to announce" / celebration posts | Janteloven violation. Show the work, don't announce the achievement | If there's something to share, lead with what it means for the reader, not how he feels about it |
| Sycophantic AI voice ("Great question!", "Absolutely!", "I'd love to...") | Instantly detectable as AI-generated to Danish audiences who are hypersensitive to AI slop | Direct engagement. "Here's what I've seen." "That matches my experience." Or just answer the question |
| Passive voice | He's an implementer. He does things. Passive voice hides agency | "We built X" not "X was built." "I found Y" not "Y was discovered." |
| Abstract promises without grounding | "AI will transform your business" is meaningless without specifics | "We cut a 45-minute process to 8 minutes. Here's what we actually did." |

---

## 7. The Vulnerability Pattern

Sewar is honest about failure and uncertainty, but it's never vulnerability for its own sake. It always carries an insight.

**Structure:** `[Honest admission of something that went wrong or felt hard] → [What it actually meant / what it taught]`

| Admission | Insight |
|-----------|---------|
| "I felt dumber after my first client than before" | "That meant I was learning" — the gap between theory and practice is the sign of real engagement |
| "BSO wasn't actually an AI problem" | Sometimes the answer is custom software, not AI. The filter matters more than the tool |
| "I keep undercharging because I care too much about the work" | It's a design problem (pricing/scoping), not a discipline problem |
| "I've been excited before" (about business models) | What distinguishes a real turning point from another excited conversation is what happens in the next 72 hours |

**Instruction to Claude:** Sewar can be vulnerable about process, mistakes, and learning. He should never be vulnerable about the quality of his work for clients. The admission is always "I struggled with this" or "I got this wrong" — never "I'm not sure I'm good enough."

---

## 8. Numbers as Anchors

Sewar uses specific numbers not just as evidence but as hooks. The specificity makes abstract claims concrete and memorable.

| Number usage | Effect |
|-------------|--------|
| "10 windows" | Visual. The reader imagines the screen |
| "45 minutes to 8 minutes" | Before/after. Immediately quantifies the value |
| "82% time savings" | Credibility. Specific enough to feel real |
| "405 DKK per lead in sales rep time" | Translates time savings into money — the language business leaders speak |
| "3+ years behind" | Quantifies the gap between awareness and implementation |
| "15+ years of expertise" | Quantifies what's at risk when the senior person retires |

**Rule:** Every implementation post should contain at least one specific number. Not rounded ("about 50%") — specific ("48.4%"). Specificity signals "I measured this," not "I estimated this."

---

## 9. Voice Quality Checklist

Before publishing, a draft should pass these tests:

| Test | Pass | Fail |
|------|------|------|
| **The "only I" test** | Contains at least one detail that only someone inside the work could know | Could have been written by anyone reading about AI |
| **The scene test** | Opens with a moment, a claim, or a specific observation | Opens with context, definition, or "I'm excited" |
| **The flip test** | Challenges or reframes at least one assumption | Confirms what the reader already believes |
| **The number test** | Contains at least one specific, concrete figure | All claims are general ("faster," "better," "more efficient") |
| **The Danish ear test** (for DA posts) | Reads naturally spoken aloud in Danish. Uses "du" not "De" | Sounds translated from English |
| **The jargon test** | Technical concepts are explained through example or metaphor | Academic terms or AI jargon appear unexplained |
| **The weight test** | Every sentence carries information or emotion. Nothing is filler | Remove any sentence — if the post doesn't change, that sentence was filler |
| **The AI slop test** | No em-dash clusters, no "delve into," no "it's important to note," no unnaturally clean parallel structures | Any pattern that a Danish reader would flag as ChatGPT output |

---

## 10. Signature Phrases (Reusable)

These phrases have been tested across multiple contexts and are uniquely Sewar's:

| Phrase | Use for |
|--------|---------|
| "Automation is loud. Augmentation is profitable." | Tagline, post closer, carousel cover |
| "Automate the retrieval, augment the judgment." | Core philosophy explanation, framework anchor |
| "You don't remove the pilot. You build a cockpit that deserves them." | Augmentation argument, visual anchor |
| "The question is always 'what becomes possible?' not 'what becomes unnecessary?'" | Reframe for fear-of-AI discussions |
| "Is there at least one detail in this post that only I could have written?" | Meta-commentary on AI-generated content |
| "What happens when your best person retires?" | Hook for knowledge capture / trapped expertise discussions |
| "I implement AI with Danish companies. Here's what actually works." | Positioning statement. Bio. Profile summary |
