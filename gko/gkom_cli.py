from pathlib import Path
from typing import List, Optional

import click

from gko.alias_mapping import AliasService
from gko.commands.add_alias import add_alias
from gko.commands.list_aliases import list_aliases
from gko.commands.open_file import open_file
from gko.commands.remove_alias import remove_alias
from gko.const import SETTINGS_FILE
from gko.domain.file_extension import check_gecko_json_extension
from gko.settings import SettingsService

settings_service = SettingsService()
alias_service = AliasService(settings_service)


@click.group()
def cli() -> None:
    """Gko management commands"""
    pass


@cli.command()
@click.argument("alias")
@click.argument("command", nargs=-1)
@click.option("-d", "--description", default=None, help="Description of the alias")
@click.option(
    "-r",
    "--relative",
    is_flag=True,
    help="Whether the alias command is relative to the alias file location (Default = False)",
)
def add(alias: str, command: List[str], description: Optional[str], relative: Optional[bool]) -> None:
    """Add a new alias."""
    command_str = " ".join(command)
    add_alias(settings_service, alias_service, alias, command_str, description, relative)


@cli.command()
@click.argument("alias")
def remove(alias: str) -> None:
    """Remove an alias."""
    remove_alias(alias_service, alias)


@cli.command()
def list() -> None:
    """List all aliases.
    Relative scripts are relative to the alias file.
    Global scripts are not."""
    list_aliases(alias_service)


@cli.command()
@click.argument("alias_file_path", type=click.Path(exists=True, dir_okay=False, resolve_path=True))
def switch(alias_file_path: str) -> None:
    """Switch to a new alias file"""
    if not alias_file_path.lower().endswith(".json"):
        click.echo(f"Error: The file '{alias_file_path}' is not a JSON file.")
        return

    if not check_gecko_json_extension(alias_file_path):
        click.echo("Warning: It is recommended to use .gecko.json extension for your alias files.")

    settings = {"currentAliases": alias_file_path}
    settings_service.save(settings)
    click.echo(f"Switched to new alias file: {alias_file_path}")


@cli.command()
def alias() -> None:
    """Open the current alias file with the default system application."""
    settings = settings_service.load()
    alias_file = Path(settings["currentAliases"])
    open_file(alias_file)


@cli.command()
def settings() -> None:
    """Open the settings file with the default system application."""
    open_file(SETTINGS_FILE)


if __name__ == "__main__":
    cli()
