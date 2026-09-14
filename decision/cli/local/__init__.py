"""
This module defines the local command tree for the Decision CLI.
"""

import typer

from decision.cli.local.app import app as app_app
from decision.cli.local.run import app as run_app

# Set up subcommand application.
app = typer.Typer()
app.add_typer(app_app, name="app")
app.add_typer(run_app, name="run")


@app.callback()
def callback() -> None:
    """
    Interact with local Decision apps and make runs.
    """
    pass
