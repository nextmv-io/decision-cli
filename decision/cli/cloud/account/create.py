"""
This module defines the cloud account create command for the Decision CLI.
"""

from typing import Annotated

import typer
from nextmv.cloud.account import Account
from nextmv.cloud.client import Client

from decision.cli.message import in_progress, print_json
from decision.cli.options import DebugOption, ProfileOption

# Set up subcommand application.
app = typer.Typer()


@app.command()
def create(
    admins: Annotated[
        list[str],
        typer.Option(
            "--admins",
            "-a",
            help="Email addresses of the administrators for the account. "
            "Pass multiple emails by repeating the flag, or separating with commas.",
            metavar="ADMINS",
        ),
    ],
    name: Annotated[
        str,
        typer.Option(
            "--name",
            "-n",
            help="A name for the account.",
            metavar="NAME",
        ),
    ],
    _: DebugOption = False,
    profile: ProfileOption = None,
) -> None:
    """
    Create a new Decision Cloud account in your organization.

    To create managed accounts, SSO must be configured for your organization.
    Please contact [link=https://www.nextmv.io/contact][bold]Decision
    support[/bold][/link] for assistance. You may use the [code]decision cloud
    sso[/code] command tree to manage the SSO configuration for your
    organization.

    At least one administrator email address must be provided. Multiple
    administrators can be specified by repeating the --admins flag or by
    separating email addresses with commas.

    [bold][underline]Examples[/underline][/bold]

    - Create an account named [magenta]Bunny Logistics[/magenta] with a single administrator.

        $ [dim]decision cloud account create --name "Bunny Logistics" \\
            --admins peter.rabbit@carrotexpress.com[/dim]

    - Create an account named [magenta]Hare Delivery Co[/magenta] with multiple administrators.

        $ [dim]decision cloud account create --name "Hare Delivery Co" \\
            --admins bugs@acme.com --admins roger@toontown.com[/dim]

    - Create an account using the profile named [magenta]hare[/magenta].

        $ [dim]decision cloud account create --name "Cottontail Couriers" \\
            --admins fluffy@hopmail.com --profile hare[/dim]

    - Create an account with comma-separated administrators.

        $ [dim]decision cloud account create --name "Whiskers Warehouse" \\
            --admins "thumper@forestmail.com,flopsy@warren.io"[/dim]
    """

    client = Client(profile=profile)
    in_progress(msg="Creating account...")

    admin_list = []
    for admin in admins:
        # It is possible to pass multiple emails separated by commas. The
        # default way though is to use the flag multiple times to specify
        # different options.
        sub_admins = admin.split(",")
        for sub_admin in sub_admins:
            admin_list.append(sub_admin.strip())

    account = Account.new(client=client, name=name, admins=admin_list)
    print_json(account.to_dict())
