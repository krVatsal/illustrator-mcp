# Illustrator MCP Server
Adobe Illustrator is compatible with JavaScript. In fact, some super big stuff you need to programmatically generate with these scripts. Bots are good at JavaScript.

This MCP server let's bots send scripts straight to Illustrator and look at the result.

Since it depends on AppleScript, it's only compatible with MacOS. and I've only tested it with Claude Desktop.
`~/Library/Application\ Support/Claude/claude_desktop_config.json`

```
{
    "mcpServers": {
        "illustrator": {
            "command": "uv",
            "args": [
                "--directory",
                "/Users/you/code/mcp/illustrator-mcp-server",
                "run",
                "illustrator"
            ]
        }
    }
}
```
