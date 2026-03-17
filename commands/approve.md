---
description: Review and approve a content draft
allowed-tools: Read, Edit, Write, Glob
args: filename
---

# Approve

Open a specific queue item for review. Present the draft. Accept approval, rejection with feedback, or redirect.

## Process

1. If a filename is provided, read that file from `queue/`. If not, list drafted items and ask which to review.
2. Present the full draft to the user.
3. Wait for response.

## Response Handling

### "approve" / "publish it" / "go"

- Update the queue file frontmatter: `status: approved`
- Optionally set `date_scheduled` if the user specifies when to post
- Confirm: "Approved. [Scheduled for X / Ready to post when you choose.]"

### Rejection with feedback

Any response that indicates the draft isn't right. Capture the feedback:

1. Update queue file frontmatter: add feedback to the `feedback` array
2. Append to `memory/observations.md`:
   ```
   ### [DATE] — Draft rejected: [slug]
   - Pillar: [X], Format: [format]
   - Feedback: [user's exact words]
   - Pattern: [if this matches a previous rejection, note it]
   ```
3. Set `status: drafted` (back to drafting pool)
4. Offer to redraft now or leave for later

### Redirect

"Make it shorter", "change to carousel", "wrong pillar", "try Danish instead":

1. Log the redirect to `memory/observations.md` (same format as rejection)
2. Update queue file frontmatter with the new direction
3. Redraft using the draft-social skill with the redirect applied

## Important

- ONLY accept explicit approval words: "approve", "approved", "publish it", "go", "post it"
- "ok", "sure", "looks good" → ask: "Ready to approve for publishing, or do you want changes?"
- Never change status to `published` — that happens manually after actual posting, logged via content-ledger.md
