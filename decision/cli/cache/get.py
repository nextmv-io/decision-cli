"""
This module defines the cache get command for the Decision CLI.
"""

import typer
from nextmv.cache import get_cache

from decision.cli.message import print_json, success
from decision.cli.options import DebugOption

# Set up subcommand application.
app = typer.Typer()


@app.command()
def get(_: DebugOption = False) -> None:
    """
    Gets general information about the Decision cache.

    [bold][underline]Examples[/underline][/bold]

    - Get cache information.

        $ [dim]decision cache get[/dim]
    """

    info = get_cache()
    success("Cache information retrieved successfully.")
    print_json(info)
