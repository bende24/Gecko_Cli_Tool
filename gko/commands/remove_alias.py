import click

from gko.alias_mapping import AliasService


def remove_alias(alias_service: AliasService, alias: str) -> None:
    aliases = alias_service.load()
    if alias in aliases:
        del aliases[alias]
        alias_service.save(aliases)
        click.echo(f"Alias '{alias}' removed.")
    else:
        click.echo(f"Alias '{alias}' not found.")
