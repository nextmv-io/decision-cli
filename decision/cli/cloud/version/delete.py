"""
This module defines the cloud version delete command for the Decision CLI.
"""

import typer

from decision.cli.configuration.config import build_cloud_app
from decision.cli.message import confirmation, info, success
from decision.cli.options import AppIDOption, DebugOption, ProfileOption, VersionIDOption, YesOption

# Set up subcommand application.
app = typer.Typer()


@app.command()
def delete(
    app_id: AppIDOption,
    version_id: VersionIDOption,
    yes: YesOption = False,
    _: DebugOption = False,
    profile: ProfileOption = None,
) -> None:
    """
    Deletes a Decision Cloud application version.

    This action is permanent and cannot be undone. Use the --yes
    flag to skip the confirmation prompt.

    [bold][underline]Examples[/underline][/bold]

    - Delete the version with the ID [magenta]v1[/magenta] from application [magenta]hare-app[/magenta].

        $ [dim]decision cloud version delete --app-id hare-app --version-id v1[/dim]

    - Delete the version without confirmation prompt.

        $ [dim]decision cloud version delete --app-id hare-app --version-id v1 --yes[/dim]
    """

    if not yes:
        confirm = confirmation(
            f"Are you sure you want to delete version [magenta]{version_id}[/magenta] "
            f"from application [magenta]{app_id}[/magenta]? This action cannot be undone.",
        )

        if not confirm:
            info(f"Version [magenta]{version_id}[/magenta] will not be deleted.")
            return

    cloud_app, _ = build_cloud_app(app_id=app_id, profile=profile)
    cloud_app.delete_version(version_id=version_id)
    success(
        f"Version [magenta]{version_id}[/magenta] deleted successfully from application [magenta]{app_id}[/magenta]."
    )
