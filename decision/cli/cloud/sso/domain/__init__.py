"""
This module defines the cloud sso domain command tree for the Decision CLI.
"""

import typer

from decision.cli.cloud.sso.domain.delete import app as delete_app

# Set up subcommand application.
app = typer.Typer()
app.add_typer(delete_app)


@app.callback()
def callback() -> None:
    """
    Manage SSO mapped domains for your Decision Cloud organization (account).

    Mapped domains redirect additional domains to your IDP for federated authentication.

    Please contact [link=https://www.nextmv.io/contact][bold]Decision support[/bold][/link]
    for assistance configuring SSO for your organization.
    """
    pass
