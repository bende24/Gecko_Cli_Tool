import pytest
from file_extension import check_gecko_json_extension


def test_gecko_json_extension():
    assert check_gecko_json_extension("example/path/to/file.gecko.json") is True
    assert check_gecko_json_extension("example/path/to/file.json") is False
    assert check_gecko_json_extension("example/path/to/file.GECKO.JSON") is True
    assert check_gecko_json_extension("example/path/to/file.gecko.JSON") is True
    assert check_gecko_json_extension("example/path/to/file.geckojson") is False
    assert check_gecko_json_extension("example/path/to/.gecko.json") is True
    assert check_gecko_json_extension("example/path/to/file.gecko.json.backup") is False
    assert check_gecko_json_extension("example/path/to/.GECKO.JSON") is True
    assert check_gecko_json_extension("") is False
    assert check_gecko_json_extension("example/path/to/file.geckojson.") is False


if __name__ == "__main__":
    pytest.main()
