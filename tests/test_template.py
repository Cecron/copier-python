import plumbum

def test_template_copy(copie):
    """Test that template generation works with default answers

    Make sure that no errors were reported, and that at least one file
    got generated.

    """
    result = copie.copy()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    # make sure at least one file got generated
    assert (result.project_dir / "pyproject.toml").exists()
    # make sure uv sync ran in tasks
    assert (result.project_dir / "uv.lock").exists()


def test_just_cov(copie):
    """Test the 'just cov' command

    Make sure that the index of the coverage report is created.

    """
    result = copie.copy()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()

    with plumbum.local.cwd(result.project_dir):
        plumbum.local.cmd.just("cov")
    assert (result.project_dir / "htmlcov" / "index.html").exists()


def test_just_lint(copie):
    """Test the 'just lint' command

    Make sure that running ruff format and linting did not fail.
    The main purpose of this test is to verify that we have no
    formating or linting errors in the generated project.

    """
    result = copie.copy()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()

    with plumbum.local.cwd(result.project_dir):
        plumbum.local.cmd.just("lint")
    # how do we make sure lint was run?


def test_just_html(copie):
    """Test the 'just html' command

    Make sure that the index page of from the documentation generation
    is created.

    """
    result = copie.copy()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()

    with plumbum.local.cwd(result.project_dir):
        plumbum.local.cmd.just("html")
    assert (result.project_dir / "docs" / "build" / "html" / "index.html").exists()
