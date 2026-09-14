"""
This module defines the cloud marketplace app get command for the Decision CLI.
"""

import json
from typing import Annotated

import typer

from decision.cli.configuration.config import build_marketplace_app
from decision.cli.message import in_progress, print_json, success
from decision.cli.options import DebugOption, MarketplaceAppIDOption, MarketplacePartnerIDOption, ProfileOption

# Set up subcommand application.
app = typer.Typer()


@app.command()
def get(
    app_id: MarketplaceAppIDOption,
    partner_id: MarketplacePartnerIDOption,
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
    Get a Decision Marketplace application.


    [bold][underline]Examples[/underline][/bold]

    - Get the marketplace application with the ID [magenta]marketplace-hare[/magenta].

        $ [dim]decision cloud marketplace app get --partner-id my-partner \\
            --app-id marketplace-hare[/dim]

    - Get the marketplace application and save the information to an [magenta]app.json[/magenta] file.

        $ [dim]decision cloud marketplace app get --partner-id my-partner \\
            --app-id marketplace-hare --output app.json[/dim]
    """

    in_progress(msg="Getting application...")
    mkt_app = build_marketplace_app(app_id=app_id, partner_id=partner_id, profile=profile)
    mkt_app_dict = mkt_app.to_dict()

    if output is not None and output != "":
        with open(output, "w") as f:
            json.dump(mkt_app_dict, f, indent=2)

        success(msg=f"Application information saved to [magenta]{output}[/magenta].")

        return

    print_json(mkt_app_dict)
