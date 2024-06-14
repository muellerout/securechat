import os
import pytest
from .core import detect_data_leaks

dataset = [
    ("My password: secret", [r".*password\:|\s.*"], r".*password\:|\s.*"),
    ("My id is ID12345!", [r".*ID\d+.*", r".*password\:|\s.*"], r".*ID\d+.*"),
    (
        "Debit card: 1234 5678 9012 3456",
        [
            r".*ID\d+.*",
            r".*password\:|\s.*",
            r".*[0-9]{4}\s[0-9]{4}\s[0-9]{4}\s[0-9]{4}.*",
        ],
        r".*[0-9]{4}\s[0-9]{4}\s[0-9]{4}\s[0-9]{4}.*",
    ),
    ("Very sensitive information!", [], None),
    (
        "Very secure message without any leaks...",
        [
            r".*ID\d+.*",
            r".*password\:|\s.*",
            r".*[0-9]{4}\s[0-9]{4}\s[0-9]{4}\s[0-9]{4}.*",
        ],
        None,
    ),
]


@pytest.mark.parametrize("input,regexs,expected", dataset)
def test_detect_data_leaks(tmp_path, input, regexs, expected):
    with open(tmp_path / "input.txt", "w") as inputfile:
        filepath = os.path.abspath(inputfile.name)

        inputfile.write(input)

    assert detect_data_leaks(filepath=filepath, regexs=regexs) == expected
