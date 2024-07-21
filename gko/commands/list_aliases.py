from pathlib import Path
import click
from gko.alias_mapping import load_aliases

def list_aliases(alias_file: Path) -> None:
    aliases = load_aliases(alias_file)
    if aliases:
        click.echo(f"{'Alias':<20}{'Description and/or Command'}")
        click.echo(f"{'-'*20}{'-'*40}")
        for alias, details in aliases.items():
            description = details.get("description", "")
            command = details["command"]
            description_part = f" ({description})" if description else ""
            click.echo(f"{alias:<20}{command}{description_part}")
    else:
        click.echo("No aliases found.")