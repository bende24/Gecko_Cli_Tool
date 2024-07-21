import json
from pathlib import Path

from gko.settings import SettingsService
from gko.types import Aliases


class AliasService:
    def __init__(self, settings: SettingsService) -> None:
        self.settings = settings

    def load(self) -> Aliases:
        alias_file = self.file_path()
        if alias_file.exists():
            with open(alias_file, "r") as f:
                return json.load(f)

        if not alias_file.exists():
            raise Exception(f"Error: Alias file does not exist: {alias_file}")

    def save(self, aliases: Aliases) -> None:
        alias_file = self.file_path()
        with open(alias_file, "w+") as f:
            json.dump(aliases, f, indent=4)

    def file_path(self) -> Path:
        return Path(self.settings.load()["currentAliases"])
