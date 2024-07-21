import json
from pathlib import Path

from setuptools.command.install import install as _install

from gko.const import DEFAULT_ALIAS_FILE, SETTINGS_FILE, USER_GKO_FOLDER
from gko.settings import DEFAULT_SETTINGS


class PostInstallCommand(_install):
    def run(self):
        _install.run(self)
        # Run post-install script
        try:
            self.create_files()
        except ImportError:
            print("Post-install script failed to import")

    def create_files(self):
        Path(USER_GKO_FOLDER).mkdir(exist_ok=True)

        if not DEFAULT_ALIAS_FILE.exists:
            with open(DEFAULT_ALIAS_FILE, "w+") as f:
                json.dump({}, f, indent=4)

        if not SETTINGS_FILE.exists:
            settings = DEFAULT_SETTINGS
            with open(SETTINGS_FILE, "w+") as f:
                json.dump(settings, f, indent=4)
