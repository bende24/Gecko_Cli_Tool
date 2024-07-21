from pathlib import Path
import platform
import subprocess

import click


def open_file(file: Path):
    if file.exists():
        __open_file(file)
    else:
        click.echo(f"Alias file does not exist: {file}")


def __open_file(filepath: Path) -> None:
    """Open the specified file using the default system application."""
    if platform.system() == "Windows":
        subprocess.run(["start", filepath], shell=True)
    elif platform.system() == "Darwin":  # macOS
        subprocess.run(["open", filepath])
    else:  # Linux and others
        subprocess.run(["xdg-open", filepath])
