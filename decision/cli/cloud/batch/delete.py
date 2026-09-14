"""
This module defines the cloud batch delete command for the Decision CLI.
"""

import typer

from decision.cli.configuration.config import build_cloud_app
from decision.cli.message import confirmation, info, success
from decision.cli.options import AppIDOption, BatchExperimentIDOption, DebugOption, ProfileOption, YesOption

# Set up subcommand application.
app = typer.Typer()


@app.command()
def delete(
    app_id: AppIDOption,
    batch_experiment_id: BatchExperimentIDOption,
    yes: YesOption = False,
    _: DebugOption = False,
    profile: ProfileOption = None,
) -> None:
    """
    Deletes a Decision Cloud batch experiment.

    This action is permanent and cannot be undone. The batch experiment and all
    associated data, including runs, will be deleted. Use the --yes
    flag to skip the confirmation prompt.

    [bold][underline]Examples[/underline][/bold]

    - Delete the batch experiment with the ID [magenta]hop-analysis[/magenta] from application
      [magenta]hare-app[/magenta].

        $ [dim]decision cloud batch delete --app-id hare-app --batch-experiment-id hop-analysis[/dim]

    - Delete the batch experiment without confirmation prompt.

        $ [dim]decision cloud batch delete --app-id hare-app --batch-experiment-id carrot-routes --yes[/dim]
    """

    if not yes:
        confirm = confirmation(
            f"Are you sure you want to delete batch experiment [magenta]{batch_experiment_id}[/magenta] "
            f"from application [magenta]{app_id}[/magenta]? This action cannot be undone.",
        )

        if not confirm:
            info(f"Batch experiment [magenta]{batch_experiment_id}[/magenta] will not be deleted.")
            return

    cloud_app, _ = build_cloud_app(app_id=app_id, profile=profile)
    cloud_app.delete_batch_experiment(batch_id=batch_experiment_id)
    success(
        f"Batch experiment [magenta]{batch_experiment_id}[/magenta] deleted successfully "
        f"from application [magenta]{app_id}[/magenta]."
    )
