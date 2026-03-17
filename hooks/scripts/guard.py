#!/usr/bin/env python3
"""PreToolUse guard for the content marketing plugin.

Blocks operations that would corrupt the memory system
or modify the immutable layer at runtime.

Warns on AI-slop patterns in drafted content.
"""

import sys
import json
import os
import re


SLOP_PATTERNS = [
    (r"in today'?s rapidly evolving", "AI cliché opener"),
    (r"\b(leverage|utilize|cutting-edge|game-changing|revolutionary|transformative)\b", "banned word"),
    (r"let'?s dive in", "AI cliché"),
    (r"without further ado", "AI cliché"),
    (r"in this post we'?ll explore", "AI cliché"),
    (r"what do you think\??\s*$", "generic CTA — earn the question or drop it"),
]


def main():
    try:
        input_data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        print(json.dumps({}))
        sys.exit(0)

    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})

    if tool_name not in ("Write", "Edit", "MultiEdit"):
        print(json.dumps({}))
        sys.exit(0)

    file_path = tool_input.get("file_path", "")
    messages = []
    should_block = False

    # --- BLOCK: Append-only file protection ---
    is_append_only = bool(
        re.search(r"(observations|content-ledger)\.md$", file_path)
    )

    if is_append_only:
        if tool_name == "Write":
            if os.path.exists(file_path):
                messages.append(
                    "**BLOCKED: Append-only file protection.**\n\n"
                    f"`{file_path}` is append-only. This is intentional and "
                    "by design — not an error to work around.\n\n"
                    "**Why this exists:** observations.md and content-ledger.md "
                    "accumulate learning over time. The Write tool replaces the "
                    "entire file, which would destroy that history. Every voice "
                    "correction, every rejection reason, every performance note "
                    "compounds into better future output. Losing it resets the "
                    "system's memory.\n\n"
                    "**What to do instead:** Use the Edit tool. Set old_string "
                    "to the last line of the file, and new_string to that same "
                    "line plus your new entries below it. This preserves "
                    "everything and adds your new content at the end.\n\n"
                    "Do not attempt to work around this by copying content to "
                    "a new file or renaming. The constraint protects the user's "
                    "accumulated feedback history."
                )
                should_block = True

        elif tool_name == "Edit":
            old_string = tool_input.get("old_string", "")
            new_string = tool_input.get("new_string", "")
            if old_string and not new_string.startswith(old_string):
                messages.append(
                    "**BLOCKED: Append-only file protection.**\n\n"
                    f"`{file_path}` is append-only. This is intentional.\n\n"
                    "**What happened:** Your edit modifies existing content. "
                    "In append-only files, you can only add new entries after "
                    "existing ones. Your new_string must start with the exact "
                    "old_string and add new content after it.\n\n"
                    "**Why:** Past entries are the system's learning history. "
                    "A voice correction from session 3 is still valuable in "
                    "session 30. Editing or removing old entries destroys "
                    "signal that shapes future output quality.\n\n"
                    "Adjust your edit so new_string begins with old_string "
                    "and appends your new content below."
                )
                should_block = True

    # --- BLOCK: Immutable layer modification ---
    if "/immutable/" in file_path:
        messages.append(
            "**BLOCKED: Immutable layer protection.**\n\n"
            f"`{file_path}` is in the immutable/ directory. This is "
            "intentional and by design.\n\n"
            "**Why this exists:** The immutable layer contains the plugin's "
            "structural rules — anti-fabrication constraints, anti-AI-slop "
            "patterns, and operational guardrails. These are set by the "
            "plugin creator and apply across all sessions. If they could "
            "be modified at runtime, the system could gradually drift from "
            "its own safety constraints.\n\n"
            "**What to do instead:** If you believe a rule needs changing, "
            "tell the user. They can modify immutable files manually outside "
            "of a session. Do not attempt to work around this by writing to "
            "a different path or copying the file elsewhere."
        )
        should_block = True

    # --- WARN: AI-slop detection in queue drafts ---
    if "queue/" in file_path and tool_name == "Write":
        content = tool_input.get("content", "")
        if content:
            slop_warnings = []
            for pattern, label in SLOP_PATTERNS:
                if re.search(pattern, content, re.IGNORECASE):
                    match = re.search(pattern, content, re.IGNORECASE)
                    slop_warnings.append(f"{label}: \"{match.group()}\"")

            # Check em-dash usage (zero tolerance)
            em_dash_count = content.count("\u2014")
            if em_dash_count > 0:
                slop_warnings.append(
                    f"Em-dash used {em_dash_count} time(s). "
                    "Zero em-dashes allowed — use periods, commas, or "
                    "restructure the sentence"
                )

            # Check for unsourced statistics
            pct_matches = re.findall(r"\d{1,3}%", content)
            for match in pct_matches:
                idx = content.find(match)
                surrounding = content[max(0, idx - 200): idx + 200]
                if "(Source:" not in surrounding and "(source:" not in surrounding:
                    slop_warnings.append(
                        f"Statistic '{match}' without inline source citation"
                    )
                    break

            if slop_warnings:
                messages.append(
                    "**Anti-slop warnings:**\n\n"
                    + "\n".join(f"- {w}" for w in slop_warnings)
                    + "\n\nReview before approving. These patterns damage "
                    "credibility with Danish audiences."
                )

    # Build response
    if should_block:
        result = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
            },
            "systemMessage": "\n\n".join(messages),
        }
    elif messages:
        result = {"systemMessage": "\n\n".join(messages)}
    else:
        result = {}

    print(json.dumps(result))
    sys.exit(0)


if __name__ == "__main__":
    main()
