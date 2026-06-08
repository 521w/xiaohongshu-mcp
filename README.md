# Xiaohongshu MCP Server

An MCP server that gives AI agents structured Xiaohongshu-style content templates, writing styles, and hashtag suggestions.

It is designed for creators, operators, and AI assistants that need repeatable Chinese social-media content workflows.

## What It Does

- Lists supported Xiaohongshu content styles
- Returns structured prompt templates for each style
- Provides recommended hashtags
- Helps agents generate more consistent Xiaohongshu drafts
- Works without external API keys

## Tools

| Tool | Description |
| --- | --- |
| `get_xiaohongshu_styles` | List available content styles with descriptions |
| `get_xiaohongshu_prompt` | Get a structured prompt template for a specific style |
| `get_xiaohongshu_tags` | Get recommended hashtags for a specific style |

## Supported Styles

| Style | Use Case |
| --- | --- |
| 种草文 | Product recommendation and lifestyle sharing |
| 测评文 | Comparison review and pros/cons analysis |
| 教程文 | Step-by-step guide or how-to post |
| 开箱文 | Unboxing and first-impression content |
| Vlog 文案 | Short video script and daily-life storytelling |

## Good For

- Xiaohongshu content drafting
- AI creator assistants
- Product review templates
- Social media operation workflows
- Repeatable brand or personal-account content production

## Installation

```bash
pip install git+https://github.com/521w/xiaohongshu-mcp.git
```

Or install from source:

```bash
git clone https://github.com/521w/xiaohongshu-mcp.git
cd xiaohongshu-mcp
pip install -e .
```

## MCP Configuration

```json
{
  "mcpServers": {
    "xiaohongshu": {
      "command": "python3",
      "args": ["-m", "xiaohongshu_mcp.server"]
    }
  }
}
```

## Example Agent Flow

```text
User asks for a Xiaohongshu product review.
Agent calls get_xiaohongshu_styles.
Agent calls get_xiaohongshu_prompt with the chosen style.
Agent calls get_xiaohongshu_tags for matching hashtags.
Agent drafts the final post using the returned structure.
```

## Example Agent Tasks

- "Write a Xiaohongshu product recommendation post for wireless earbuds."
- "Turn this travel experience into a Xiaohongshu Vlog script."
- "Give me hashtags for a skincare comparison review."
- "Create a reusable Xiaohongshu content workflow for a small brand."

## Why This Server

- **No API key**: fully local prompt/template tool
- **Agent-native**: exposes reusable writing assets through MCP
- **Consistent output**: reduces random style drift across drafts
- **Productizable**: useful as a content-ops component for creator services or small businesses

## Requirements

- Python >= 3.10
- `mcp >= 1.0.0`

## Notes

This server provides writing structures and prompt assets. It does not publish content, scrape Xiaohongshu, or bypass platform controls.

## Verified Status

Verified on Termux/Android with Python 3.13:

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e .
xiaohongshu-mcp
```

MCP initialization, tool listing, and `get_xiaohongshu_styles` tool calls were verified successfully.

## License

MIT
