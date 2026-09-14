"""
This module defines the cloud acceptance delete command for the Decision CLI.
"""

import typer

from decision.cli.configuration.config import build_cloud_app
from decision.cli.message import confirmation, info, success
from decision.cli.options import AcceptanceTestIDOption, AppIDOption, DebugOption, ProfileOption, YesOption

# Set up subcommand application.
app = typer.Typer()


@app.command()
def delete(
    app_id: AppIDOption,
    acceptance_test_id: AcceptanceTestIDOption,
    yes: YesOption = False,
    _: DebugOption = False,
    profile: ProfileOption = None,
) -> None:
    """
    Deletes a Decision Cloud acceptance test.

    This action is permanent and cannot be undone. The underlying batch
    experiment and associated data will also be deleted. Use the --yes flag to
    skip the confirmation prompt.

    [bold][underline]Examples[/underline][/bold]

    - Delete the acceptance test with the ID [magenta]test-cotton-tail[/magenta] from application
      [magenta]hare-app[/magenta].

        $ [dim]decision cloud acceptance delete --app-id hare-app --acceptance-test-id test-cotton-tail[/dim]

    - Delete the acceptance test without confirmation prompt.

        $ [dim]decision cloud acceptance delete --app-id hare-app --acceptance-test-id test-cotton-tail --yes[/dim]
    """

    if not yes:
        confirm = confirmation(
            f"Are you sure you want to delete acceptance test [magenta]{acceptance_test_id}[/magenta] "
            f"from application [magenta]{app_id}[/magenta]? This action cannot be undone.",
        )

        if not confirm:
            info(f"Acceptance test [magenta]{acceptance_test_id}[/magenta] will not be deleted.")
            return

    cloud_app, _ = build_cloud_app(app_id=app_id, profile=profile)
    cloud_app.delete_acceptance_test(acceptance_test_id=acceptance_test_id)
    success(
        f"Acceptance test [magenta]{acceptance_test_id}[/magenta] deleted successfully "
        f"from application [magenta]{app_id}[/magenta]."
    )
