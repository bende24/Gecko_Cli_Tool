import json
from pathlib import Path
from gko.const import DEFAULT_ALIAS_FILE, SETTINGS_FILE, USER_GKO_FOLDER
from setuptools.command.install import install as _install


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
            settings = {"currentAliases": str(DEFAULT_ALIAS_FILE)}
            with open(SETTINGS_FILE, "w+") as f:
                json.dump(settings, f, indent=4)
