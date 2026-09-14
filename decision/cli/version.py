"""
This module defines the version command for the Decision CLI.
"""

import typer

from decision.__about__ import __version__
from decision.cli.options import DebugOption

# Set up subcommand application.
app = typer.Typer()


@app.command()
def version(_: DebugOption = False) -> None:
    """
    Show the current version of the Decision CLI.

    [bold][underline]Examples[/underline][/bold]

    - Show the version.

        $ [dim]decision version[/dim]
    """

    version_callback(True)


def version_callback(value: bool):
    """
    Callback function to display the version.

    Parameters
    ----------
    value : bool
        If True, print the version and exit.
    """
    if value:
        print(__version__)
        raise typer.Exit()
