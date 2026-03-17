#!/usr/bin/env python3
"""PostToolUse telemetry logger for the content marketing team.

Appends a JSONL entry for every tool call. Provides audit trail
and observability.

Reads JSON from stdin. Writes to telemetry.jsonl in the workspace.
Workspace is detected by scanning for a .content-marketing-team marker file.
"""

import sys
import json
import os
from datetime import datetime, timezone

MARKER = ".content-marketing-team"


def find_workspace():
    """Find the workspace by walking up from cwd and scanning /mnt/."""
    # Walk up from cwd
    path = os.path.abspath(os.getcwd())
    while True:
        if os.path.isfile(os.path.join(path, MARKER)):
            return path
        parent = os.path.dirname(path)
        if parent == path:
            break
        path = parent

    # Scan /mnt/ children (Cowork deployments with custom names)
    if os.path.isdir("/mnt"):
        for entry in os.listdir("/mnt"):
            candidate = os.path.join("/mnt", entry)
            if os.path.isdir(candidate) and os.path.isfile(
                os.path.join(candidate, MARKER)
            ):
                return candidate

    return None


def summarize_input(tool_name, tool_input):
    """Extract a compact summary of what the tool did."""
    if tool_name in ("Write", "Edit", "Read"):
        return tool_input.get("file_path", "unknown file")
    elif tool_name == "Bash":
        cmd = tool_input.get("command", "")
        return cmd[:200].replace("\n", " ")
    elif tool_name == "WebSearch":
        return tool_input.get("query", "")
    elif tool_name == "WebFetch":
        return tool_input.get("url", "")
    elif tool_name in ("Grep", "Glob"):
        return tool_input.get("pattern", "")
    else:
        raw = json.dumps(tool_input)
        return raw[:200]


def main():
    try:
        input_data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    workspace = find_workspace()
    if workspace is None:
        sys.exit(0)

    log_file = os.path.join(workspace, "telemetry.jsonl")

    tool_name = input_data.get("tool_name", "unknown")
    tool_input = input_data.get("tool_input", {})

    entry = {
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "tool": tool_name,
        "summary": summarize_input(tool_name, tool_input),
    }

    try:
        with open(log_file, "a") as f:
            f.write(json.dumps(entry) + "\n")
    except (IOError, OSError):
        pass

    sys.exit(0)


if __name__ == "__main__":
    main()
