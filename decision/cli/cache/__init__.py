"""
This module defines the cache command tree for the Decision CLI.
"""

import typer

from decision.cli.cache.delete import app as delete_app
from decision.cli.cache.get import app as get_app

# Set up subcommand application.
app = typer.Typer()
app.add_typer(delete_app)
app.add_typer(get_app)


@app.callback()
def callback() -> None:
    """
    Manage the cache used for Decision operations.
    """
    pass
