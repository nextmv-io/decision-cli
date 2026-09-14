"""
This module defines the local app registered command for the Decision CLI.
"""

import os

import typer
from nextmv.local.registry import Registry

from decision.cli.message import in_progress, print_json
from decision.cli.options import DebugOption, LocalAppIDOption, LocalAppSrcOption

# Set up subcommand application.
app = typer.Typer()


@app.command()
def registered(
    app_id: LocalAppIDOption = None,
    app_src: LocalAppSrcOption = None,
    _: DebugOption = False,
) -> None:
    """
    Check if a Decision application is registered locally.

    You may identify the app by using --app-src or --app-id. This command is
    useful in scripting applications to verify the existence of a local
    application.

    [bold][underline]Examples[/underline][/bold]

    - Check if the application with the ID [magenta]hare-app[/magenta] is registered.

        $ [dim]decision local app registered --app-id hare-app[/dim]

    - Check if the application with source path [magenta]./hare-app/[/magenta] is registered.

        $ [dim]decision local app registered --app-src ./hare-app/[/dim]
    """

    if (app_id is None or app_id == "") and (app_src is None or app_src == ""):
        app_src = "."

    if app_src is not None and app_src != "":
        app_src = os.path.abspath(app_src)

    in_progress(msg="Checking if application is registered...")
    reg = Registry.from_yaml()
    entry = reg.entry(app_id=app_id, src=app_src)
    ok = entry is not None
    print_json({"registered": ok})
    if not ok:
        raise typer.Exit(code=1)
