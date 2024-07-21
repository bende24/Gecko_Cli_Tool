from typing import Optional

import click

from gko.alias_mapping import AliasService
from gko.settings import SettingsService


def add_alias(
    settings_service: SettingsService,
    alias_service: AliasService,
    alias: str,
    command: str,
    description: Optional[str] = None,
    relative: Optional[bool] = None,
) -> None:
    if relative is None:
        relative = settings_service.load()["defaultRelative"]

    aliases = alias_service.load()
    aliases[alias] = {"command": command, "description": description, "relative": relative}
    alias_service.save(aliases)
    click.echo(f"Alias '{alias}' added with description: '{description}'" if description else f"Alias '{alias}' added.")
