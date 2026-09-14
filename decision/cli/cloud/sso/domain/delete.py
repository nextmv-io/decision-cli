"""
This module defines the cloud sso domain delete command for the Decision CLI.
"""

from typing import Annotated

import typer

from decision.cli.configuration.config import build_sso_config
from decision.cli.message import confirmation, in_progress, info, success
from decision.cli.options import DebugOption, ProfileOption, YesOption

# Set up subcommand application.
app = typer.Typer()


@app.command()
def delete(
    domain: Annotated[
        str,
        typer.Option(
            "--domain",
            "-d",
            help="The domain to delete from the SSO configuration.",
            metavar="DOMAIN",
        ),
    ],
    yes: YesOption = False,
    _: DebugOption = False,
    profile: ProfileOption = None,
) -> None:
    """
    Delete a mapped domain from a Decision Cloud SSO configuration.


    This action will prevent users from the deleted domain from accessing your
    account using SSO. Use the --yes flag to skip the confirmation prompt.

    You can use the [code]decision cloud sso get[/code] command to view all
    mapped domains in your SSO configuration.

    [bold][underline]Examples[/underline][/bold]

    - Delete a mapped domain from the SSO configuration.

        $ [dim]decision cloud sso domain delete --domain "example.com"[/dim]
    """

    if not yes:
        confirm = confirmation(
            f"Are you sure you want to delete the [magenta]{domain}[/magenta] domain? "
            "You must contact Decision support to re-add it.",
        )

        if not confirm:
            info("SSO mapped domain will not be deleted.")
            return

    sso_config = build_sso_config(profile)
    in_progress(msg="Deleting SSO mapped domain from configuration...")
    sso_config.delete_domain(domain=domain)
    success("SSO mapped domain deleted successfully.")
