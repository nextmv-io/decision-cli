"""
This module defines the cloud run cancel command for the Decision CLI.
"""

import typer

from decision.cli.configuration.config import build_cloud_app
from decision.cli.message import in_progress, success
from decision.cli.options import AppIDOption, DebugOption, ProfileOption, RunIDOption

# Set up subcommand application.
app = typer.Typer()


@app.command()
def cancel(
    app_id: AppIDOption,
    run_id: RunIDOption,
    _: DebugOption = False,
    profile: ProfileOption = None,
) -> None:
    """
    Cancel a queued/running Decision Cloud application run.

    [bold][underline]Examples[/underline][/bold]

    - Cancel the run with ID [magenta]burrow-123[/magenta] belonging to an app with ID [magenta]hare-app[/magenta].

        $ [dim]decision cloud run cancel --app-id hare-app --run-id burrow-123[/dim]

    - Cancel the run with ID [magenta]burrow-123[/magenta] belonging to an app with ID [magenta]hare-app[/magenta].
      Use the profile named [magenta]hare[/magenta].

        $ [dim]decision cloud run cancel --app-id hare-app --run-id burrow-123 --profile hare[/dim]
    """

    cloud_app, _ = build_cloud_app(app_id=app_id, profile=profile)
    in_progress(msg=f"Canceling run [magenta]{run_id}[/magenta]...")
    cloud_app.cancel_run(run_id)
    success(f"Run [magenta]{run_id}[/magenta] canceled.")
