# ~/.gemini/extensions/mcp/server.py
from absl import app
from src.tools import modulus
from src.tools import sqrt
from mcp.server import fastmcp

# --- Main Server Setup ---
def main(argv: list[str]) -> None:
  if len(argv) > 1:
    raise app.UsageError("Too many command-line arguments.")

  # Create an MCP server instance. The name is used for identification.
  mcp = fastmcp.FastMCP("bhs-agent")

  # Add your tool functions to the server.
  mcp.add_tool(modulus)
  mcp.add_tool(sqrt)

  # Run the server. "stdio" transport is used when Gemini CLI launches the server as a command.
  mcp.run(transport="stdio")

if __name__ == "__main__":
  app.run(main)
