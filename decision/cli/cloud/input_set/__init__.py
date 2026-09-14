"""
This module defines the cloud input-set command tree for the Decision CLI.
"""

import typer

from decision.cli.cloud.input_set.create import app as create_app
from decision.cli.cloud.input_set.delete import app as delete_app
from decision.cli.cloud.input_set.get import app as get_app
from decision.cli.cloud.input_set.list import app as list_app
from decision.cli.cloud.input_set.update import app as update_app

# Set up subcommand application.
app = typer.Typer()
app.add_typer(create_app)
app.add_typer(delete_app)
app.add_typer(get_app)
app.add_typer(list_app)
app.add_typer(update_app)


@app.callback()
def callback() -> None:
    """
    Create and manage Decision Cloud input sets.

    An input set is a collection of inputs from associated runs that can be
    reused across multiple experiments. Input sets allow you to test different
    configurations of your decision model using the same set of inputs for
    consistent comparison.
    """
    pass
