from pathlib import Path
from typing import List, Optional

import click

from gko.commands.add_alias import add_alias
from gko.commands.list_aliases import list_aliases
from gko.commands.open_file import open_file
from gko.commands.remove_alias import remove_alias
from gko.const import SETTINGS_FILE
from gko.domain.file_extension import check_gecko_json_extension
from gko.settings import load_settings, save_settings


@click.group()
def cli() -> None:
    """Gko management commands"""
    pass


@cli.command()
@click.argument("alias")
@click.argument("command", nargs=-1)
@click.option("-d", "--description", default=None, help="Description of the alias")
@click.option("-r", "--relative", is_flag=True, help="Whether the alias command is relative to the alias file location")
def add(alias: str, command: List[str], description: Optional[str], relative: Optional[bool]) -> None:
    """Add a new alias."""
    settings = load_settings(SETTINGS_FILE)
    alias_file = Path(settings["currentAliases"])
    command_str = " ".join(command)
    add_alias(alias_file, alias, command_str, description, relative)


@cli.command()
@click.argument("alias")
def remove(alias: str) -> None:
    """Remove an alias."""
    settings = load_settings(SETTINGS_FILE)
    alias_file = Path(settings["currentAliases"])
    remove_alias(alias_file, alias)


@cli.command()
def list() -> None:
    """List all aliases."""
    settings = load_settings(SETTINGS_FILE)
    alias_file = Path(settings["currentAliases"])
    list_aliases(alias_file)


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
    save_settings(SETTINGS_FILE, settings)
    click.echo(f"Switched to new alias file: {alias_file_path}")


@cli.command()
def aliases() -> None:
    """Open the current alias file with the default system application."""
    settings = load_settings(SETTINGS_FILE)
    alias_file = Path(settings["currentAliases"])
    open_file(alias_file)


@cli.command()
def settings() -> None:
    """Open the settings file with the default system application."""
    open_file(SETTINGS_FILE)


if __name__ == "__main__":
    cli()
