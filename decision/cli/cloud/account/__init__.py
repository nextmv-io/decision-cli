"""
This module defines the cloud account command tree for the Decision CLI.
"""

import typer

from decision.cli.cloud.account.create import app as create_app
from decision.cli.cloud.account.delete import app as delete_app
from decision.cli.cloud.account.get import app as get_app
from decision.cli.cloud.account.update import app as update_app

# Set up subcommand application.
app = typer.Typer()
app.add_typer(create_app)
app.add_typer(delete_app)
app.add_typer(get_app)
app.add_typer(update_app)


@app.callback()
def callback() -> None:
    """
    Manage your Decision Cloud account (organization).

    Please contact [link=https://www.nextmv.io/contact][bold]Decision
    support[/bold][/link] for assistance configuring SSO for your organization.
    You may use the [code]decision cloud sso[/code] command tree to manage the
    SSO configuration for your organization.
    """
    pass
