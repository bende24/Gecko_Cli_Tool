from typing import List

import click

from gko.alias_mapping import AliasService
from gko.commands.execute_alias import execute_alias
from gko.settings import SettingsService

settings_service = SettingsService()
alias_service = AliasService(settings_service)

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("alias")
@click.argument("args", nargs=-1)
def cli(alias: str, args: List[str]) -> None:
    """Run a command using an alias.\n
    Use gkom for additional commands."""
    execute_alias(alias_service, alias, args)


if __name__ == "__main__":
    cli()
