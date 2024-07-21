import os
import subprocess
from pathlib import Path
import json
from typing import List
import sys


def execute_alias(alias_file: Path, alias: str, args: List[str]) -> None:
    """Run a command using an alias and display its output."""
    # Load the alias mapping from the JSON file
    if not alias_file.exists():
        print(f"Error: Alias file does not exist: {alias_file}")
        return

    with alias_file.open("r") as f:
        aliases = json.load(f)

    # Find the command for the alias
    if alias not in aliases:
        print(f"Error: Alias '{alias}' not found.")
        return

    command_str = aliases[alias]["command"]

    # Build the full command string with additional arguments
    command_with_args = f"{command_str} {' '.join(args)}"

    # Execute the command and display output
    try:
        cwd = os.path.dirname(alias_file)
        result = subprocess.Popen(
            command_with_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, cwd=cwd
        )

        for line in result.stdout:
            sys.stdout.write(line)
        if result.stderr:
            for line in result.stderr:
                sys.stderr.write(line)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}", file=sys.stderr)
