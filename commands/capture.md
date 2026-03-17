---
description: Quick idea capture — turns raw input into a structured content item
allowed-tools: Read, Write
args: idea
---

# Capture

Thin command wrapper around the capture skill. Pass the raw input directly — no questions asked.

## Usage

`/capture I had a great meeting with a logistics company today. They've been trying to use AI for route optimization but keep hitting the same wall — their data is scattered across 4 different systems and nobody owns the integration. Classic translation layer problem.`

## Process

1. Take everything after `/capture` as the raw input
2. Invoke the capture skill with this input
3. Present the structured result: pillar, format, language, hook, and queue file location

If no input is provided after `/capture`, ask "What's the idea?" — one question, then process whatever comes back.
