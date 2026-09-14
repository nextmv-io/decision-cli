"""
This module defines the cloud instance exists command for the Decision CLI.
"""

import typer

from decision.cli.configuration.config import build_cloud_app
from decision.cli.message import in_progress, print_json
from decision.cli.options import AppIDOption, DebugOption, InstanceIDOption, ProfileOption

# Set up subcommand application.
app = typer.Typer()


@app.command()
def exists(
    app_id: AppIDOption,
    instance_id: InstanceIDOption,
    _: DebugOption = False,
    profile: ProfileOption = None,
) -> None:
    """
    Check if a Decision Cloud application instance exists.

    This command is useful in scripting applications to verify the existence of
    a Decision Cloud application instance by its ID.

    [bold][underline]Examples[/underline][/bold]

    - Check if the instance with the ID [magenta]prod[/magenta] exists in application [magenta]hare-app[/magenta].

        $ [dim]decision cloud instance exists --app-id hare-app --instance-id prod[/dim]

    - Check if the instance exists using the profile named [magenta]hare[/magenta].

        $ [dim]decision cloud instance exists --app-id hare-app --instance-id prod --profile hare[/dim]
    """

    cloud_app, _ = build_cloud_app(app_id=app_id, profile=profile)
    in_progress(msg="Checking if instance exists...")
    ok = cloud_app.instance_exists(instance_id=instance_id)
    print_json({"exists": ok})
    if not ok:
        raise typer.Exit(code=1)
