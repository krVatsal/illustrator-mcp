# Illustrator MCP Server (Windows & macOS)

Welcome to the **Illustrator MCP Server**! 🎨🚀

This project allows AI agents to **directly create vector graphics** inside **Adobe Illustrator** using natural language prompts.  
It works by sending ExtendScript commands to Illustrator via a local MCP (Model Context Protocol) server.

> Imagine simply describing what you want — like *"draw a small coffee shop during rain"* — and Illustrator brings it to life!

Works on **Windows** (COM automation) and **macOS** (AppleScript/osascript).

---

## ✨ Features
- Control Adobe Illustrator programmatically using AI prompts
- Send ExtendScript (.jsx) scripts directly to Illustrator
- Capture screenshots of the Illustrator window
- Open-source and lightweight
- **Cross-platform:** Windows & macOS
- **Multi-client:** Works with Claude Desktop, Claude Code, Cursor, VS Code Copilot, and JetBrains Copilot

---

## 💻 Installation

### Prerequisites
- **Python 3.12+** — [Download Python](https://www.python.org/downloads/)
- **Adobe Illustrator** installed and running
- **macOS only:** Grant Automation permissions when prompted (System Settings → Privacy & Security → Automation)

### 1. Clone the repository

   ```bash
   git clone https://github.com/krVatsal/illustrator-mcp.git
   cd illustrator-mcp
   ```

### 2. Create a virtual environment

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```
> On macOS, `pywin32` is automatically skipped. No extra macOS packages required.

### 4. Start the MCP Server (manual / debug mode)

```bash
python -m illustrator
```

### Run with one script (cross-platform)

```bash
bash run_server.sh
```

This script auto-detects your platform, creates a `.venv`, installs dependencies, and starts the server.

---

## 🔌 Client Configuration

The server uses **stdio transport** — compatible with all major MCP clients.

> **Important:** Do NOT start the server manually when using it through a client. The client starts and manages the server process automatically.

### Claude Desktop

**macOS** — edit `~/Library/Application Support/Claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "illustrator": {
      "command": "/path/to/illustrator-mcp/.venv/bin/python3",
      "args": ["-m", "illustrator"]
    }
  }
}
```

**Windows** — edit `%APPDATA%\Claude\claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "illustrator": {
      "command": "C:\\Users\\<YourUser>\\illustrator-mcp\\.venv\\Scripts\\python.exe",
      "args": ["-m", "illustrator"]
    }
  }
}
```

### Claude Code (CLI)

A `.claude/mcp.json` is included in the repo. Claude Code will auto-detect it. Or add manually:

```bash
claude mcp add illustrator python3 -- -m illustrator
```

### GitHub Copilot (VS Code)

A `.vscode/mcp.json` is included in the repo. VS Code (1.99+) will auto-detect it. Or add to your `settings.json`:

```json
{
  "mcp": {
    "servers": {
      "illustrator": {
        "type": "stdio",
        "command": "python3",
        "args": ["-m", "illustrator"]
      }
    }
  }
}
```
---

## 🎯 Enhanced Prompt System

This MCP server now includes an advanced prompt system to help you create better content! Use these new tools:

- **`get_prompt_suggestions`** - Get categorized prompt examples for different types of content
- **`get_system_prompt`** - Get the optimal system prompt for AI guidance
- **`get_prompting_tips`** - Get tips for creating more effective prompts
- **`get_advanced_template`** - Get structured templates for complex design tasks
- **`help`** - Display comprehensive help and guidance

### 📚 Prompt Categories Available:
- 🎨 Basic Shapes & Geometry
- 📝 Typography & Text  
- 🏢 Logos & Branding
- 🌆 Illustrations & Scenes
- 🎭 Icons & UI Elements
- 🎨 Artistic & Creative
- 📊 Charts & Infographics
- 🏷️ Print & Layout

### 💡 Quick Start with Prompts
Try asking: *"Get me prompt suggestions for logos"* or *"Show me prompting tips"*

For detailed examples and templates, see [PROMPT_EXAMPLES.md](./PROMPT_EXAMPLES.md)

---

## 📋 Sample Prompts I Tried

Here are some prompts I used along with the results it generated:

- **Prompt 1:**  
  *Design a clean, minimal vector art of a small coffee shop during rain, featuring a simple storefront, puddles on the street, and gentle grey clouds in the sky.*

- **Prompt 2:**  
  *Create a watercolor-style illustration of the Mumbai skyline at sunset.*

- **Prompt 3:**  
  *Create a modern, minimalistic logo for a tech startup called 'NeuraTech'.*

*(See attached images for the results!)*

---

## 🍎 macOS Notes

- Adobe Illustrator must be installed and running
- On first use, macOS will ask for **Automation permission** — allow your terminal/IDE to control Illustrator
- If you see "Application not running" errors, open Illustrator first
- Screenshots capture the full screen (Illustrator should be in foreground)

## 🪟 Windows Notes

- Adobe Illustrator must be installed
- The `pywin32` package is required (installed automatically)
- Illustrator scripting must be enabled

---


## 📢 Contributing

Pull requests are welcome!  
Feel free to open issues for feature requests, bugs, or suggestions.
![Stars](https://img.shields.io/github/stars/krVatsal/illustrator-mcp)
![Forks](https://img.shields.io/github/forks/krVatsal/illustrator-mcp)
![License](https://img.shields.io/github/license/krVatsal/illustrator-mcp)

---

Happy creating! 🌈💛
