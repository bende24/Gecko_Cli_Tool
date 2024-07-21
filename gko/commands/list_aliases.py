import click

from gko.alias_mapping import AliasService


def list_aliases(alias_service: AliasService) -> None:
    aliases = alias_service.load()
    if aliases:
        click.echo(f"{'Alias':<20}{'Description and/or Command [Relative/Global]'}")
        click.echo(f"{'-'*20}{'-'*40}")
        for alias, details in aliases.items():
            description = details.get("description", "")
            command = details["command"]
            description_part = f" ({description})" if description else ""
            relative = "[Relative]" if details["relative"] else "[Global]"
            click.echo(f"{alias:<20}{command}{description_part} {relative}")
    else:
        click.echo("No aliases found.")
