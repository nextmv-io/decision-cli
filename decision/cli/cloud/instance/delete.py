"""
This module defines the cloud instance delete command for the Decision CLI.
"""

import typer

from decision.cli.configuration.config import build_cloud_app
from decision.cli.message import confirmation, info, success
from decision.cli.options import AppIDOption, DebugOption, InstanceIDOption, ProfileOption, YesOption

# Set up subcommand application.
app = typer.Typer()


@app.command()
def delete(
    app_id: AppIDOption,
    instance_id: InstanceIDOption,
    yes: YesOption = False,
    _: DebugOption = False,
    profile: ProfileOption = None,
) -> None:
    """
    Deletes a Decision Cloud application instance.

    This action is permanent and cannot be undone. Use the --yes
    flag to skip the confirmation prompt.

    [bold][underline]Examples[/underline][/bold]

    - Delete the instance with the ID [magenta]prod[/magenta] from application [magenta]hare-app[/magenta].

        $ [dim]decision cloud instance delete --app-id hare-app --instance-id prod[/dim]

    - Delete the instance without confirmation prompt.

        $ [dim]decision cloud instance delete --app-id hare-app --instance-id prod --yes[/dim]
    """

    if not yes:
        confirm = confirmation(
            f"Are you sure you want to delete instance [magenta]{instance_id}[/magenta] "
            f"from application [magenta]{app_id}[/magenta]? This action cannot be undone.",
        )

        if not confirm:
            info(f"Instance [magenta]{instance_id}[/magenta] will not be deleted.")
            return

    cloud_app, _ = build_cloud_app(app_id=app_id, profile=profile)
    cloud_app.delete_instance(instance_id=instance_id)
    success(
        f"Instance [magenta]{instance_id}[/magenta] deleted successfully from application [magenta]{app_id}[/magenta]."
    )
