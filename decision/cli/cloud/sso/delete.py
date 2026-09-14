"""
This module defines the cloud sso delete command for the Decision CLI.
"""

import typer

from decision.cli.configuration.config import build_sso_config
from decision.cli.message import confirmation, info, success
from decision.cli.options import DebugOption, ProfileOption, YesOption

# Set up subcommand application.
app = typer.Typer()


@app.command()
def delete(
    yes: YesOption = False,
    _: DebugOption = False,
    profile: ProfileOption = None,
) -> None:
    """
    Deletes the SSO configuration.

    You must have the [magenta]administrator[/magenta] role on the organization
    in order to delete it. Use the --yes flag to skip the confirmation prompt.
    You can create a new SSO configuration again with [code]decision cloud sso create[/code].

    [bold][underline]Examples[/underline][/bold]

    - Delete the SSO configuration.

        $ [dim]decision cloud sso delete[/dim]

    - Delete the SSO configuration without confirmation prompt.

        $ [dim]decision cloud sso delete --yes[/dim]
    """

    if not yes:
        confirm = confirmation(
            "Are you sure you want to delete the sso configuration? "
            "You can create it again with [code]decision cloud sso create[/code].",
        )

        if not confirm:
            info("SSO configuration will not be deleted.")
            return

    sso_config = build_sso_config(profile)
    sso_config.delete()
    success("SSO configuration has been deleted. You can create it again with [code]decision cloud sso create[/code].")
