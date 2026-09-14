"""
This module defines the cloud sso update command for the Decision CLI.
"""

from typing import Annotated

import typer

from decision.cli.configuration.config import build_sso_config
from decision.cli.message import in_progress, success
from decision.cli.options import DebugOption, ProfileOption

# Set up subcommand application.
app = typer.Typer()


@app.command()
def update(
    metadata_url: Annotated[
        str | None,
        typer.Option(
            "--metadata-url",
            "-u",
            help="The URL to the SSO metadata document to update.",
            metavar="METADATA_URL",
        ),
    ] = None,
    metadata_document: Annotated[
        str | None,
        typer.Option(
            "--metadata-document",
            "-d",
            help="The SSO metadata document as a string to update.",
            metavar="METADATA_DOCUMENT",
        ),
    ] = None,
    _: DebugOption = False,
    profile: ProfileOption = None,
) -> None:
    """
    Updates information of a Decision Cloud SSO configuration.

    This command allows you to update the metadata URL or metadata document of
    an existing SSO configuration. You can use the [code]decision cloud sso
    get[/code] to get the updated configuration after running this command.

    [bold][underline]Examples[/underline][/bold]

    - Update the SSO configuration with a new metadata URL.

        $ [dim]decision cloud sso update --metadata-url "https://example.com/metadata.xml"[/dim]

    - Update the SSO configuration with a new metadata document.

        $ [dim]decision cloud sso update --metadata-document "<xml>...</xml>"[/dim]
    """

    sso_config = build_sso_config(profile)
    in_progress(msg="Updating SSO configuration...")
    sso_config.update(metadata_url=metadata_url, metadata_document=metadata_document)
    success("SSO configuration updated successfully.")
