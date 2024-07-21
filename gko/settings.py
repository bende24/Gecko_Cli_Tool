import json
from pathlib import Path
from gko.const import DEFAULT_ALIAS_FILE
from gko.types import Settings


def load_settings(settings_file: Path) -> Settings:
    if settings_file.exists():
        with open(settings_file, "r") as f:
            return json.load(f)

    settings = {"currentAliases": str(DEFAULT_ALIAS_FILE)}
    save_settings(settings_file, settings)
    return settings


def save_settings(settings_file: Path, settings: Settings) -> None:
    with open(settings_file, "w+") as f:
        json.dump(settings, f, indent=4)
