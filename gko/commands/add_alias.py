from pathlib import Path
from typing import Optional

import click

from gko.alias_mapping import load_aliases, save_aliases
from gko.settings import SettingsService


def add_alias(
    settings_service: SettingsService,
    alias_file: Path,
    alias: str,
    command: str,
    description: Optional[str] = None,
    relative: Optional[bool] = None,
) -> None:
    if relative is None:
        relative = settings_service.load()["defaultRelative"]

    aliases = load_aliases(alias_file)
    aliases[alias] = {"command": command, "description": description, "relative": relative}
    save_aliases(alias_file, aliases)
    click.echo(f"Alias '{alias}' added with description: '{description}'" if description else f"Alias '{alias}' added.")
