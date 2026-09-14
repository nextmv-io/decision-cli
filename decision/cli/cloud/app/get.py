"""
This module defines the cloud app get command for the Decision CLI.
"""

import json
from typing import Annotated

import typer
from nextmv.cloud.application import Application
from nextmv.cloud.client import Client

from decision.cli.message import in_progress, print_json, success
from decision.cli.options import AppIDOption, DebugOption, ProfileOption

# Set up subcommand application.
app = typer.Typer()


@app.command()
def get(
    app_id: AppIDOption,
    output: Annotated[
        str | None,
        typer.Option(
            "--output",
            "-o",
            help="Saves the app information to this location.",
            metavar="OUTPUT_PATH",
        ),
    ] = None,
    _: DebugOption = False,
    profile: ProfileOption = None,
) -> None:
    """
    Get a Decision Cloud application.

    This command is useful to get the attributes of an existing Decision Cloud
    application by its ID.

    [bold][underline]Examples[/underline][/bold]

    - Get the application with the ID [magenta]hare-app[/magenta].

        $ [dim]decision cloud app get --app-id hare-app[/dim]

    - Get the application with the ID [magenta]hare-app[/magenta] and save the information to an
      [magenta]app.json[/magenta] file.

        $ [dim]decision cloud app get --app-id hare-app --output app.json[/dim]
    """

    client = Client(profile=profile)
    in_progress(msg="Getting application...")

    cloud_app = Application.get(client=client, id=app_id)
    cloud_app_dict = cloud_app.to_dict()

    if output is not None and output != "":
        with open(output, "w") as f:
            json.dump(cloud_app_dict, f, indent=2)

        success(msg=f"Application information saved to [magenta]{output}[/magenta].")

        return

    print_json(cloud_app_dict)
