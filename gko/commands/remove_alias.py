from pathlib import Path

import click

from gko.alias_mapping import load_aliases, save_aliases


def remove_alias(alias_file: Path, alias: str) -> None:
    aliases = load_aliases(alias_file)
    if alias in aliases:
        del aliases[alias]
        save_aliases(alias_file, aliases)
        click.echo(f"Alias '{alias}' removed.")
    else:
        click.echo(f"Alias '{alias}' not found.")
