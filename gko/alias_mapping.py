import json
from pathlib import Path

from gko.const import DEFAULT_ALIAS_FILE
from gko.types import Aliases


def load_aliases(alias_file: Path) -> Aliases:
    if alias_file.exists():
        with open(alias_file, "r") as f:
            return json.load(f)

    aliases = {}
    save_aliases(DEFAULT_ALIAS_FILE, aliases)
    return aliases


def save_aliases(alias_file: Path, aliases: Aliases) -> None:
    with open(alias_file, "w+") as f:
        json.dump(aliases, f, indent=4)
