import sys, os
import subprocess
import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

server = Server("os-controller")

@server.list_tools()
async def handle_list_tools():
    return [
        Tool(name="run_cmd", description="Execute a local Windows CMD command", inputSchema={"type": "object", "properties": {"command": {"type": "string"}}, "required": ["command"]}),
        Tool(name="list_dir", description="List files in a directory", inputSchema={"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]})
    ]

@server.call_tool()
async def handle_call_tool(name, arguments):
    if name == "run_cmd":
        cmd = arguments.get("command")
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding="gbk")
        return [TextContent(type="text", text=res.stdout + res.stderr)]
    elif name == "list_dir":
        path = arguments.get("path", ".")
        try:
            files = os.listdir(path)
            return [TextContent(type="text", text="\n".join(files))]
        except Exception as e:
            return [TextContent(type="text", text=str(e))]
    raise ValueError("Unknown tool")

async def main():
    async with stdio_server() as (r, w):
        await server.run(r, w, server.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
