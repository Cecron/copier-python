import pytest


licenses = [
    {
        "copyright_license": "GNU GPLv3",
        "first_line": "GNU GENERAL PUBLIC LICENSE",
    },
    {
        "copyright_license": "MIT",
        "first_line": "MIT License",
    },
    {
        "copyright_license": "Unlicense",
        "first_line": "This is free and unencumbered software released into the public domain.",
    },
]


@pytest.mark.parametrize("license", licenses)
def test_licenses(copie, license):
    """Test generated license file

    Generate projects with different answers to the
    'copyright_license' question, and verify that the first row of the
    generated license file is correct.

    """
    answers = {
        "copyright_license": license["copyright_license"],
    }
    result = copie.copy(extra_answers=answers)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    line = None
    with open(result.project_dir / "LICENSE.txt") as f:
        for line in f:
            if line.strip():
                break
    print(f"First non-empty line: {line}")
    assert license["first_line"] in line
