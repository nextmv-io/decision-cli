"""
This module defines the cloud batch command tree for the Decision CLI.
"""

import typer

from decision.cli.cloud.batch.create import app as create_app
from decision.cli.cloud.batch.delete import app as delete_app
from decision.cli.cloud.batch.get import app as get_app
from decision.cli.cloud.batch.list import app as list_app
from decision.cli.cloud.batch.metadata import app as metadata_app
from decision.cli.cloud.batch.update import app as update_app

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
    Create and manage Decision Cloud batch experiments.
    """
    pass
