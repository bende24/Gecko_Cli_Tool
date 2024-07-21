import json

from gko.const import DEFAULT_ALIAS_FILE, SETTINGS_FILE
from gko.types import Settings

DEFAULT_SETTINGS: Settings = {"currentAliases": str(DEFAULT_ALIAS_FILE), "defaultRelative": False}


class SettingsService:
    settings_file = SETTINGS_FILE

    def load(self) -> Settings:
        if self.settings_file.exists():
            with open(self.settings_file, "r") as f:
                return json.load(f)

        settings = {"currentAliases": str(DEFAULT_ALIAS_FILE)}
        self.save(self.settings_file, settings)
        return settings

    def save(self, settings: Settings) -> None:
        with open(self.settings_file, "w+") as f:
            json.dump(settings, f, indent=4)
