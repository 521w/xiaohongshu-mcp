"""Xiaohongshu MCP Server - Generate Xiaohongshu content templates."""
import json
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

STYLES = {
    "caozhong": "种草文",
    "ceping": "测评文",
    "jiaocheng": "教程文",
    "kaixiang": "开箱文",
    "vlog": "Vlog文案"
}

PROMPTS = {
    "caozhong": """你是小红书资深种草文案写手。

【风格要求】
- 亲切口语，像闺蜜分享
- emoji 丰富但不泛滥（每段1-2个）
- 标题要抓眼球，用悬念/数字/对比
- 正文分3-5段，每段讲一个亮点
- 结尾加互动

【输出格式】
标题：（15-20字，含emoji）
第一段：痛点/场景引入
第二段：产品/方案亮点
第三段：使用体验/效果
第四段：性价比/推荐理由
第五段：互动收尾

【合规要求】
- 不写"最xx""第一""绝对"
- 不写医疗功效宣称
- 保持真实感，不夸张

请为以下主题生成种草文：""",

    "ceping": """你是小红书测评类文案写手。

【风格要求】
- 客观冷静，有数据支撑
- 对比维度：价格/效果/外观/使用感
- 优缺点都要写，不一边倒
- 适合数码、美妆、家居、食品

【输出格式】
标题：（含emoji + 品类关键词）
开头：为什么要测这个
产品清单：列出测评对象
对比表格：维度/产品A/产品B/产品C
实测过程：简短描述
总结：推荐排名 + 理由

请为以下主题生成测评文：""",

    "jiaocheng": """你是小红书教程类文案写手。

【风格要求】
- 步骤清晰，序号分点
- 手把手教学，新手友好
- 每个步骤配简短解释
- 干货密集，短小精悍
- 适合：美妆教程、穿搭教程、技能教程、美食教程

【输出格式】
标题：（含emoji + "xx分钟学会""手把手教你""保姆级教程"）
准备材料/工具：
第一步：xxx
第二步：xxx
第三步：xxx
成品展示：
小tips：

请为以下主题生成教程文：""",

    "kaixiang": """你是小红书开箱类文案写手。

【风格要求】
- 兴奋感拉满，像刚收到快递
- 从外包装到内物的仪式感
- 细节描写（质感、声音、味道）
- 适合：数码产品、美妆、零食、盲盒、家居

【输出格式】
标题：（含emoji + "开箱""刚收到""第一手"）
快递到了！
外包装细节
打开瞬间
产品细节
首次使用感受
值不值

请为以下主题生成开箱文：""",

    "vlog": """你是小红书Vlog类文案写手。

【风格要求】
- 生活化叙事，像日记
- 时间线结构（早上→中午→晚上）
- 场景感强，有画面描述
- 适合：日常vlog、探店、旅行、美食

【输出格式】
标题：（含emoji + "一天""打卡""记录"）
早上：
中午：
下午：
晚上：
今日感悟/小确幸：
BGM建议：
画面提示：

请为以下主题生成Vlog文案："""
}

TAGS = {
    "caozhong": "#种草 #好物分享 #平价好物 #学生党 #真实测评",
    "ceping": "#测评 #真实测评 #避雷 #种草 #好物分享",
    "jiaocheng": "#教程 #手把手 #新手必看 #技能分享 #学习",
    "kaixiang": "#开箱 #新入手 #好物分享 #购物分享 #开箱视频",
    "vlog": "#Vlog #日常 #生活方式 #记录生活 #治愈系"
}

app = Server("xiaohongshu-mcp")

@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="get_xiaohongshu_prompt",
            description="Get the Xiaohongshu writing prompt template for a specific style",
            inputSchema={
                "type": "object",
                "properties": {
                    "style": {
                        "type": "string",
                        "description": "Content style",
                        "enum": list(STYLES.keys()) + ["all"]
                    }
                },
                "required": ["style"]
            }
        ),
        Tool(
            name="get_xiaohongshu_tags",
            description="Get recommended hashtags for a specific content style",
            inputSchema={
                "type": "object",
                "properties": {
                    "style": {
                        "type": "string",
                        "description": "Content style",
                        "enum": list(STYLES.keys())
                    }
                },
                "required": ["style"]
            }
        ),
        Tool(
            name="get_xiaohongshu_styles",
            description="List all available Xiaohongshu content styles with descriptions",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "get_xiaohongshu_styles":
        result = "\n".join([f"{k}: {v}" for k, v in STYLES.items()])
        return [TextContent(type="text", text=result)]

    elif name == "get_xiaohongshu_prompt":
        style = arguments["style"]
        if style == "all":
            result = json.dumps(PROMPTS, ensure_ascii=False, indent=2)
        elif style in PROMPTS:
            result = PROMPTS[style]
        else:
            result = f"Unknown style: {style}. Available: {', '.join(STYLES.keys())}"
        return [TextContent(type="text", text=result)]

    elif name == "get_xiaohongshu_tags":
        style = arguments["style"]
        result = TAGS.get(style, f"Unknown style: {style}")
        return [TextContent(type="text", text=result)]

    return [TextContent(type="text", text="Unknown tool")]

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

def run():
    import asyncio
    asyncio.run(main())

if __name__ == "__main__":
    run()