"""
This module defines the cloud upload create command for the Decision CLI.
"""

import typer

from decision.cli.configuration.config import build_cloud_app
from decision.cli.message import in_progress, print_json, success
from decision.cli.options import AppIDOption, DebugOption, ProfileOption

# Set up subcommand application.
app = typer.Typer()


@app.command()
def create(
    app_id: AppIDOption,
    _: DebugOption = False,
    profile: ProfileOption = None,
) -> None:
    """
    Create a new Decision Cloud application upload URL.

    [bold][underline]Examples[/underline][/bold]

    - Create an upload URL for application [magenta]hare-app[/magenta].

        $ [dim]decision cloud upload create --app-id hare-app[/dim]

    - Create an upload URL for application [magenta]hare-app[/magenta] using profile [magenta]hare[/magenta].

        $ [dim]decision cloud upload create --app-id hare-app --profile hare[/dim]
    """

    cloud_app, _ = build_cloud_app(app_id=app_id, profile=profile)
    in_progress(msg="Creating upload URL...")
    upload_url = cloud_app.upload_url()
    success(
        f"Upload URL created for application [magenta]{app_id}[/magenta]. "
        "This URL is valid for [magenta]10 minutes[/magenta]."
    )
    print_json(upload_url.to_dict())
