# Xiaohongshu MCP Server

MCP Server for generating Xiaohongshu (小红书) content with AI assistants.

## Features

- 5 content styles: 种草文 (product review), 测评文 (comparison review), 教程文 (tutorial), 开箱文 (unboxing), Vlog文案 (vlog script)
- Structured prompt templates for each style
- Recommended hashtags for each content type
- Style listing and discovery tools

## Installation

```bash
pip install xiaohongshu-mcp
```

Or from source:

```bash
git clone https://github.com/YOUR_USERNAME/xiaohongshu-mcp
cd xiaohongshu-mcp
pip install -e .
```

## Usage

Add to your MCP client config (Claude Desktop, Cursor, etc.):

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
| `get_xiaohongshu_styles` | List all available content styles |
| `get_xiaohongshu_prompt` | Get prompt template for a style |
| `get_xiaohongshu_tags` | Get recommended hashtags |

## Example

```
User: Can you write a Xiaohongshu product review for wireless earbuds?

AI calls get_xiaohongshu_prompt(style="caozhong")
AI calls get_xiaohongshu_tags(style="caozhong")
AI generates the content using the returned templates
```