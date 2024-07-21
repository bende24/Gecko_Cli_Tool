from pathlib import Path
from typing import List

import click

from gko.commands.execute_alias import execute_alias
from gko.const import SETTINGS_FILE
from gko.settings import load_settings


@click.command()
@click.argument("alias")
@click.argument("args", nargs=-1)
def cli(alias: str, args: List[str]) -> None:
    """Run a command using an alias.\n
    Use gkom for additional commands."""
    settings = load_settings(SETTINGS_FILE)
    alias_file = Path(settings["currentAliases"])
    execute_alias(alias_file, alias, args)


if __name__ == "__main__":
    cli()
