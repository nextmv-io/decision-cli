"""
This module defines the cloud run metadata command for the Decision CLI.
"""

import json
from typing import Annotated

import typer

from decision.cli.configuration.config import build_cloud_app
from decision.cli.message import in_progress, print_json, success, warning
from decision.cli.options import AppIDOption, DebugOption, ProfileOption, RunIDOption

# Set up subcommand application.
app = typer.Typer()


@app.command(deprecated=True)
def metadata(
    app_id: AppIDOption,
    run_id: RunIDOption,
    output: Annotated[
        str | None,
        typer.Option(
            "--output",
            "-o",
            help="Saves the metadata to this location.",
            metavar="OUTPUT_PATH",
        ),
    ] = None,
    _: DebugOption = False,
    profile: ProfileOption = None,
) -> None:
    """
    This command is deprecated, use [code]decision cloud run information[/code] instead.

    Get the metadata of a Decision Cloud application run.

    By default, the metadata is fetched and printed to [magenta]stdout[/magenta].
    Use the --output flag to save the metadata to a file.

    [bold][underline]Examples[/underline][/bold]

    - Get the metadata of a run with ID [magenta]burrow-123[/magenta], belonging to an app with ID
      [magenta]hare-app[/magenta]. Metadata is printed to [magenta]stdout[/magenta].

        $ [dim]decision cloud run metadata --app-id hare-app --run-id burrow-123[/dim]

    - Get the metadata of a run with ID [magenta]burrow-123[/magenta], belonging to an app with ID
      [magenta]hare-app[/magenta]. Save the metadata to a [magenta]metadata.json[/magenta] file.

        $ [dim]decision cloud run metadata --app-id hare-app --run-id burrow-123 --output metadata.json[/dim]

    - Get the metadata of a run with ID [magenta]burrow-123[/magenta], belonging to an app with ID
      [magenta]hare-app[/magenta]. Use the profile named [magenta]hare[/magenta].

        $ [dim]decision cloud run metadata --app-id hare-app --run-id burrow-123 --profile hare[/dim]
    """

    warning(
        "The [code]decision cloud run metadata[/code] command is deprecated and "
        "will be removed in the next major release. "
        "Please use the [code]decision cloud run information[/code] command instead."
    )

    cloud_app, _ = build_cloud_app(app_id=app_id, profile=profile)
    in_progress(msg="Getting run metadata...")
    run_info = cloud_app.run_metadata(run_id)
    info_dict = run_info.to_dict()

    if output is not None and output != "":
        with open(output, "w") as f:
            json.dump(info_dict, f, indent=2)

        success(msg=f"Run metadata saved to [magenta]{output}[/magenta].")

        return

    print_json(info_dict)
