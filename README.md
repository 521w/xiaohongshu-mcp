# Xiaohongshu MCP Server

MCP Server for generating Xiaohongshu (小红书) content with AI assistants. Provides structured prompt templates for 5 popular writing styles, recommended hashtags, and style discovery.

## Features

- **5 content styles**: 种草文 (product review), 测评文 (comparison review), 教程文 (tutorial), 开箱文 (unboxing), Vlog文案 (vlog script)
- **Structured prompts**: Optimized templates designed for Chinese social media
- **Hashtag recommendations**: Curated tags for each content type
- **Style discovery**: List all available styles at a glance

## Installation

```bash
pip install git+https://github.com/521w/xiaohongshu-mcp.git
```

Or from source:

```bash
git clone https://github.com/521w/xiaohongshu-mcp.git
cd xiaohongshu-mcp
pip install -e .
```

## Usage

Add to your MCP client configuration:

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

## Tools

| Tool | Description |
|------|-------------|
| `get_xiaohongshu_styles` | List all available content styles with descriptions |
| `get_xiaohongshu_prompt` | Get a structured prompt template for a specific style |
| `get_xiaohongshu_tags` | Get recommended hashtags for a specific style |

## Example

```
User: Can you write a Xiaohongshu product review for wireless earbuds?

AI calls get_xiaohongshu_prompt(style="caozhong")
AI calls get_xiaohongshu_tags(style="caozhong")
AI generates the content using the returned templates
```

## Requirements

- Python >= 3.10
- mcp >= 1.0.0

## License

MIT