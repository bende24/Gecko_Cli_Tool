import json
from pathlib import Path
import pytest
from click.testing import CliRunner
from gko.cli import cli
from gko.alias_mapping import load_aliases, save_aliases
from gko.types import Aliases

@pytest.fixture
def alias_file(tmp_path) -> Path:
    """Fixture to create a temporary alias file for testing."""
    return tmp_path / ".gecko.json"

def test_load_aliases(alias_file: Path) -> None:
    aliases: Aliases = {"test": {"command": "echo test", "description": "A test command"}}
    alias_file.write_text(json.dumps(aliases))
    loaded_aliases = load_aliases(alias_file)
    assert loaded_aliases == aliases

def test_save_aliases(alias_file: Path) -> None:
    aliases: Aliases = {"test": {"command": "echo test", "description": "A test command"}}
    save_aliases(alias_file, aliases)
    saved_aliases = json.loads(alias_file.read_text())
    assert saved_aliases == aliases

def test_add_alias(alias_file: Path) -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ['add', 'test', 'echo test', '-d', 'A test command'])
    assert result.exit_code == 0
    aliases = load_aliases(alias_file)
    assert 'test' in aliases
    assert aliases['test']['command'] == 'echo test'
    assert aliases['test']['description'] == 'A test command'

def test_remove_alias(alias_file: Path) -> None:
    aliases: Aliases = {"test": {"command": "echo test", "description": "A test command"}}
    save_aliases(alias_file, aliases)
    runner = CliRunner()
    result = runner.invoke(cli, ['remove', 'test'])
    assert result.exit_code == 0
    aliases = load_aliases(alias_file)
    assert 'test' not in aliases

def test_execute_alias(alias_file: Path) -> None:
    aliases: Aliases = {"test": {"command": "echo test", "description": "A test command"}}
    save_aliases(alias_file, aliases)
    runner = CliRunner()
    result = runner.invoke(cli, ['test'])
    assert result.exit_code == 0
    assert result.output == 'test\n'

def test_list_aliases(alias_file: Path) -> None:
    aliases: Aliases = {
        "test1": {"command": "echo test1", "description": "First test command"},
        "test2": {"command": "echo test2", "description": None},
    }
    save_aliases(alias_file, aliases)
    runner = CliRunner()
    result = runner.invoke(cli, ['list'])
    assert result.exit_code == 0
    output = result.output.split('\n')
    assert 'test1' in output[2]
    assert 'First test command' in output[2]
    assert 'test2' in output[3]
    assert 'echo test2' in output[3]

if __name__ == '__main__':
    pytest.main()
