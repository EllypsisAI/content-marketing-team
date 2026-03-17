# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user connects in that category. Skills describe workflows in terms of categories, not specific products. The `.mcp.json` pre-configures specific MCP servers, but any server in that category works.

When a connector is not available, skills fall back to web search and manual methods.

## Connectors for this plugin

| Category | Placeholder | Default | Degraded mode |
|----------|-------------|---------|---------------|
| Research | `~~research` | Perplexity | Native web search for topic discovery and trend scanning |
| Sentiment | `~~sentiment` | Reddit MCP | Manual — user provides audience insights or forum quotes |
| Social | `~~social` | — (future) | Manual posting. Copy draft from queue file to LinkedIn |
| Analytics | `~~analytics` | — (manual) | User enters performance data via /month or observations.md |
| Blog source | `~~blog` | Content Engine plugin | User provides URL or text for repurpose skill |

## Note on Reddit

Reddit is a **listening post**, not a distribution channel. The Reddit MCP is used by the research skill to understand what real people are saying about AI, Danish business, and implementation reality. Never post to Reddit. Never quote Reddit usernames. Paraphrase sentiment and pain points — the value is in understanding the audience's unfiltered voice.
