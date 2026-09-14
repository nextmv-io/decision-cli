"""
This module defines the cloud switchback delete command for the Decision CLI.
"""

import typer

from decision.cli.configuration.config import build_cloud_app
from decision.cli.message import confirmation, info, success
from decision.cli.options import AppIDOption, DebugOption, ProfileOption, SwitchbackTestIDOption, YesOption

# Set up subcommand application.
app = typer.Typer()


@app.command()
def delete(
    app_id: AppIDOption,
    switchback_test_id: SwitchbackTestIDOption,
    yes: YesOption = False,
    _: DebugOption = False,
    profile: ProfileOption = None,
) -> None:
    """
    Deletes a Decision Cloud switchback test.

    This action is permanent and cannot be undone. The switchback test and all
    associated data, including runs, will be deleted. Use the --yes
    flag to skip the confirmation prompt.

    [bold][underline]Examples[/underline][/bold]

    - Delete the switchback test with the ID [magenta]hop-analysis[/magenta] from application
      [magenta]hare-app[/magenta].

        $ [dim]decision cloud switchback delete --app-id hare-app --switchback-test-id hop-analysis[/dim]

    - Delete the switchback test without confirmation prompt.

        $ [dim]decision cloud switchback delete --app-id hare-app --switchback-test-id carrot-routes --yes[/dim]
    """

    if not yes:
        confirm = confirmation(
            f"Are you sure you want to delete switchback test [magenta]{switchback_test_id}[/magenta] "
            f"from application [magenta]{app_id}[/magenta]? This action cannot be undone.",
        )

        if not confirm:
            info(f"Switchback test [magenta]{switchback_test_id}[/magenta] will not be deleted.")
            return

    cloud_app, _ = build_cloud_app(app_id=app_id, profile=profile)
    cloud_app.delete_switchback_test(switchback_test_id=switchback_test_id)
    success(
        f"Switchback test [magenta]{switchback_test_id}[/magenta] deleted successfully "
        f"from application [magenta]{app_id}[/magenta]."
    )
