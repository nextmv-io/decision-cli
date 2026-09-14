"""
This module defines the cloud scenario command tree for the Decision CLI.
"""

import typer

from decision.cli.cloud.scenario.create import app as create_app
from decision.cli.cloud.scenario.delete import app as delete_app
from decision.cli.cloud.scenario.get import app as get_app
from decision.cli.cloud.scenario.list import app as list_app
from decision.cli.cloud.scenario.metadata import app as metadata_app
from decision.cli.cloud.scenario.update import app as update_app

# Set up subcommand application.
app = typer.Typer()
app.add_typer(create_app)
app.add_typer(delete_app)
app.add_typer(get_app)
app.add_typer(list_app)
app.add_typer(metadata_app)
app.add_typer(update_app)


@app.callback()
def callback() -> None:
    """
    Create and manage Decision Cloud scenario tests.
    """
    pass
