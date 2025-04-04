import subprocess
import tempfile
import os
import asyncio
import base64
import io
import logging
import time

import mcp.types as types
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
import mcp.server.stdio
from PIL import ImageGrab
import win32com.client

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)

server = Server("illustrator")

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    logging.info("Listing available tools.")
    return [
        types.Tool(
            name="view",
            description="View a screenshot of the Adobe Illustrator window",
            inputSchema={"type": "object", "properties": {}},
        ),
        types.Tool(
            name="run",
            description="Run ExtendScript code in Illustrator",
            inputSchema={
                "type": "object",
                "properties": {
                    "code": {"type": "string", "description": "ExtendScript code to execute."}
                },
                "required": ["code"],
            },
        ),
    ]

def capture_illustrator() -> list[types.TextContent | types.ImageContent]:
    logging.info("Starting screenshot capture for Illustrator.")
    try:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("Adobe Illustrator")
        time.sleep(1)
        screenshot = ImageGrab.grab()
        buffer = io.BytesIO()
        screenshot.save(buffer, format="JPEG", quality=50, optimize=True)
        screenshot_data = base64.b64encode(buffer.getvalue()).decode("utf-8")
        logging.info("Screenshot captured successfully.")
        return [types.ImageContent(type="image", mimeType="image/jpeg", data=screenshot_data)]
    except Exception as e:
        logging.error(f"Failed to capture screenshot: {str(e)}")
        return [types.TextContent(type="text", text=f"Failed to capture screenshot: {str(e)}")]

def run_illustrator_script(code: str) -> list[types.TextContent]:
    logging.info("Running ExtendScript code in Illustrator using COM.")
    try:
        with tempfile.NamedTemporaryFile(suffix=".jsx", delete=False) as jsx_file:
            jsx_file.write(code.encode("utf-8"))
            jsx_file_path = jsx_file.name
        logging.debug(f"ExtendScript saved to: {jsx_file_path}")
        illustrator = win32com.client.Dispatch("Illustrator.Application")
        illustrator.DoJavaScriptFile(jsx_file_path)
        logging.info("ExtendScript executed successfully.")
        os.unlink(jsx_file_path)
        logging.debug("Temporary ExtendScript file removed.")
        return [types.TextContent(type="text", text="Script executed successfully")]
    except Exception as e:
        logging.error(f"Failed to execute script: {str(e)}")
        return [types.TextContent(type="text", text=f"Failed to execute script: {str(e)}")]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict | None):
    logging.info(f"Received tool call: {name} with arguments: {arguments}")
    if name == "view":
        return capture_illustrator()
    elif name == "run":
        if not arguments or "code" not in arguments:
            logging.warning("No code provided for run tool.")
            return [types.TextContent(type="text", text="No code provided")]
        return run_illustrator_script(arguments["code"])
    else:
        error_msg = f"Unknown tool: {name}"
        logging.error(error_msg)
        raise ValueError(error_msg)

async def main():
    logging.info("Initializing MCP server for Illustrator.")
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="illustrator",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )
        logging.info("MCP server is running. Awaiting commands...")
        await asyncio.Future()

if __name__ == "__main__":
    logging.info("Starting the main event loop.")
    asyncio.run(main())
