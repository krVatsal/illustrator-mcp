# Illustrator MCP Server (Windows)

Welcome to the **Illustrator MCP Server**! 🎨🚀

This project allows Claude to **directly create vector graphics** inside **Adobe Illustrator** using natural language prompts.  
It works by sending TypeScript commands to Illustrator via a local server.

> Imagine simply describing what you want — like *"draw a small coffee shop during rain"* — and Illustrator brings it to life!

This version works on **Windows** by communicating with Illustrator’s scripting engine directly.

---

## ✨ Features
- Control Adobe Illustrator programmatically using AI prompts
- Send TypeScript (.tsx) scripts directly to Illustrator
- Open-source and lightweight
- Designed to work with **Claude Desktop** (but can work with any agent that speaks MCP)

---

## 💻 Installation

1. **Install Python 3.11+**

   Make sure you have Python installed.  
   [Download Python here](https://www.python.org/downloads/).

2. **Clone this repository**

   ```bash
   git clone https://github.com/krVatsal/illustrator-mcp-server.git
   cd illustrator-mcp-server
   ```

3. **Create a virtual environment** (recommended)

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   or
   uv sync
   ```

5. **Start the MCP Server**

   ```bash
   python server.py
   ```

---

## 🛠️ Setting up Claude Desktop

To allow Claude Desktop to communicate with the MCP server:

1. Open the configuration file:

   ```
   %APPDATA%\Claude\claude_desktop_config.json
   ```

2. Add the MCP server configuration:

   ```json

    "mcpServers": {
        "illustrator": {
            "command": "python",
            "args": [
                "/absolute/path/to/server.py"
            ]
        }
    }

   ```

   Replace `/absolute/path/to/server.py` with the correct path on your machine.

3. Restart Claude Desktop after saving the config.
NOTE: Same method can be used with Cursor also, if Claude desktop fails(Might be bug in claude desktop with versions) then try on Cursor
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


## 🧐 Notes

- You need **Adobe Illustrator** installed on your system.
- Make sure Illustrator scripting is enabled.
- This server sends TypeScript (.tsx) to Illustrator — Illustrator handles the execution.
- Claude Desktop currently does not allow setting system prompts, so you might need to guide it a little during use.

---


## 📢 Contributing

Pull requests are welcome!  
Feel free to open issues for feature requests, bugs, or suggestions.
![Stars](https://img.shields.io/github/stars/krVatsal/illustrator-mcp)
![Forks](https://img.shields.io/github/forks/krVatsal/illustrator-mcp)
![License](https://img.shields.io/github/license/krVatsal/illustrator-mcp)

---

Happy creating! 🌈💛
