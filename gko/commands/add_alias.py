from pathlib import Path
from typing import Optional

import click

from gko.alias_mapping import load_aliases, save_aliases


def add_alias(alias_file: Path, alias: str, command: str, description: Optional[str] = None) -> None:
    aliases = load_aliases(alias_file)
    aliases[alias] = {"command": command, "description": description}
    save_aliases(alias_file, aliases)
    click.echo(f"Alias '{alias}' added with description: '{description}'" if description else f"Alias '{alias}' added.")
