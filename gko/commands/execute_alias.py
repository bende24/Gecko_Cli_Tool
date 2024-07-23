import os
import subprocess
import sys
from typing import List, Optional

from gko.alias_mapping import AliasService
from gko.types import AliasDetails


def execute_alias(alias_service: AliasService, alias: str, args: List[str]) -> None:
    """Run a command using an alias and display its output."""

    aliases = alias_service.load()

    # Find the command for the alias
    if alias not in aliases:
        print(f"Error: Alias '{alias}' not found.")
        return

    alias_detail: AliasDetails = aliases[alias]
    command_str = alias_detail["command"]

    # Build the full command string with additional arguments
    command_with_args = f"{command_str} {' '.join(args)}"

    # Execute the command and display output
    try:
        cwd: Optional[str] = os.path.dirname(alias_service.file_path()) if alias_detail["relative"] else None

        subprocess.call(command_with_args, cwd=cwd, shell=True, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}", file=sys.stderr)
