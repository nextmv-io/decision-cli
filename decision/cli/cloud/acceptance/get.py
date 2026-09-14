"""
This module defines the cloud acceptance get command for the Decision CLI.
"""

import json
from typing import Annotated

import typer
from nextmv.polling import default_polling_options

from decision.cli.configuration.config import build_cloud_app
from decision.cli.message import in_progress, print_json, success
from decision.cli.options import AcceptanceTestIDOption, AppIDOption, DebugOption, ProfileOption

# Set up subcommand application.
app = typer.Typer()


@app.command()
def get(
    app_id: AppIDOption,
    acceptance_test_id: AcceptanceTestIDOption,
    output: Annotated[
        str | None,
        typer.Option(
            "--output",
            "-o",
            help="Waits for the acceptance test to complete and saves the results to this location.",
            metavar="OUTPUT_PATH",
        ),
    ] = None,
    timeout: Annotated[
        int,
        typer.Option(
            "--timeout",
            help="The maximum time in seconds to wait for results when polling. Poll indefinitely if not set.",
            metavar="TIMEOUT_SECONDS",
        ),
    ] = -1,
    wait: Annotated[
        bool,
        typer.Option(
            "--wait",
            "-w",
            help="Wait for the acceptance test to complete. Results are printed to [magenta]stdout[/magenta]. "
            "Specify output location with --output.",
        ),
    ] = False,
    _: DebugOption = False,
    profile: ProfileOption = None,
) -> None:
    """
    Get a Decision Cloud acceptance test.

    Use the --wait flag to wait for the acceptance test to complete, polling
    for results. Using the --output flag will also activate waiting, and allows
    you to specify a destination file for the results.

    [bold][underline]Examples[/underline][/bold]

    - Get the acceptance test with ID [magenta]test-123[/magenta] from application
      [magenta]hare-app[/magenta].

        $ [dim]decision cloud acceptance get --app-id hare-app --acceptance-test-id test-123[/dim]

    - Get the acceptance test and wait for it to complete if necessary.

        $ [dim]decision cloud acceptance get --app-id hare-app --acceptance-test-id test-123 --wait[/dim]

    - Get the acceptance test and save the results to a file.

        $ [dim]decision cloud acceptance get --app-id hare-app \\
            --acceptance-test-id test-123 --output results.json[/dim]

    - Get the acceptance test using a specific profile.

        $ [dim]decision cloud acceptance get --app-id hare-app --acceptance-test-id test-123 --profile prod[/dim]
    """

    cloud_app, _ = build_cloud_app(app_id=app_id, profile=profile)

    # Build the polling options.
    polling_options = default_polling_options()
    polling_options.max_duration = timeout

    # Determine if we should wait
    should_wait = wait or (output is not None and output != "")

    in_progress(msg="Getting acceptance test...")
    if should_wait:
        acceptance_test = cloud_app.acceptance_test_with_polling(
            acceptance_test_id=acceptance_test_id,
            polling_options=polling_options,
        )
    else:
        acceptance_test = cloud_app.acceptance_test(acceptance_test_id=acceptance_test_id)

    acceptance_test_dict = acceptance_test.to_dict()

    # Handle output
    if output is not None and output != "":
        with open(output, "w") as f:
            json.dump(acceptance_test_dict, f, indent=2)

        success(msg=f"Acceptance test results saved to [magenta]{output}[/magenta].")

        return

    print_json(acceptance_test_dict)
