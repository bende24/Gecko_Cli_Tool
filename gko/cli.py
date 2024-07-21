from typing import List

import click

from gko.commands.execute_alias import execute_alias
from gko.settings import SettingsService

settings_service = SettingsService()


@click.command()
@click.argument("alias")
@click.argument("args", nargs=-1)
def cli(alias: str, args: List[str]) -> None:
    """Run a command using an alias.\n
    Use gkom for additional commands."""
    execute_alias(settings_service, alias, args)


if __name__ == "__main__":
    cli()
