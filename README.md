# 🤖 My Custom Gemini CLI Project

This repository serves as a starting point for developing with the **Gemini Command Line Interface (CLI)** and integrating custom tools using the **Model Context Protocol (MCP)**.

## 🛠️ Prerequisites

1.  **Node.js** (v20 or higher is recommended)
2.  **npm** (Node Package Manager)
3.  **Gemini API Key** (Set as an environment variable `GEMINI_API_KEY`)
4.  **Gemini CLI** (Install globally via npm):
    ```bash
    npm install -g @google/gemini-cli
    ```

## 🚀 Gemini CLI Usage

The Gemini CLI can be used in an interactive mode or for single-shot prompts.

| Command | Description | Example |
| :--- | :--- | :--- |
| `gemini` | **Interactive Mode** (REPL). Starts a conversational session. | `gemini` |
| `gemini -p` | **Non-Interactive Mode**. Gets a single response. | `gemini -p "Write a hello world script in Python."` |
| `gemini -v` | **Check Version**. Displays the installed CLI version. | `gemini -v` |
| `echo "..." \| gemini` | **Piping Content**. Sends piped content as a prompt. | `echo "Explain this file: @./src/main.js" \| gemini` |

### ✨ Helpful Slash Commands (within interactive mode)

* `/help`: Display all available commands and shortcuts.
* `/tools`: List available built-in and MCP tools.
* `/mcp`: List configured MCP servers and their available tools.
* `/init`: Generate a starting `GEMINI.md` context file for your project.
* `/settings`: Open your `settings.json` file for customization.

## ⚙️ Integrating the Sample MCP Server

This repository includes a sample MCP server in the `./mcp-server` directory (which you will add). To connect it to your Gemini CLI session:

1.  **Start the MCP Server:** Navigate to the server directory and run it. *(The specific command will depend on your server's language/framework, e.g., `npm start` or `python server.py`)*.
2.  **Configure in `settings.json`:** Add an entry to your CLI's configuration to tell it where to find your server. Use the `/settings` command inside the CLI to edit this file.

    ```json
    {
      "mcpServers": {
        "custom-tool": {
          "command": "npm", // or 'python', etc.
          "args": ["start"],
          "cwd": "./mcp-server" // Path to your server's directory
        }
      }
    }
    ```

3.  **Restart/Use CLI:** The new tools from your custom MCP server should now be available for Gemini to use. You can verify this with the `/mcp` or `/tools` commands.

## ✍️ Customization and Further Development

Feel free to customize this project by:

* **Editing `GEMINI.md`:** Use this file to provide high-level instructions, style guides, and context to the Gemini model for your specific project.
* **Developing the MCP Server:** Expand the server in `./mcp-server` by adding more tools to integrate with external APIs, databases, or internal systems.
* **Creating Extensions:** Explore the Gemini CLI documentation for building extensions for more advanced integrations.
