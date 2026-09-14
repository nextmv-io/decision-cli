"""MCP (Model Context Protocol) server for the Decision CLI.

Requires the ``mcp`` optional extra: ``pip install decision-cli[mcp]``.
"""

# Fail fast at import time so that main.py's try/except can gate the
# subcommand registration.
import importlib.util

if importlib.util.find_spec("mcp") is None:
    raise ImportError(
        "The mcp extra is not installed. Install it with: pip install decision-cli[mcp]"
    )

import typer

from decision.cli.mcp.serve import app as serve_app

# Set up subcommand application.
app = typer.Typer()
app.add_typer(serve_app)


@app.callback()
def callback() -> None:
    """
    Model Context Protocol (MCP) server for LLM integrations.

    Start an MCP server so that any MCP-compatible client (Claude Code,
    Cursor, VS Code, etc.) can interact with Decision Cloud through natural
    language.

    [bold][underline]Quick start[/underline][/bold]

    - Register with Claude Code.
        $ [dim]claude mcp add decision -- decision mcp serve[/dim]
    """
    pass
