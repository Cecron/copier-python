import plumbum

def test_template_copy(copie):
    result = copie.copy()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    # make sure at least one file got generated
    assert (result.project_dir / "pyproject.toml").exists()
    # make sure uv sync ran in tasks
    assert (result.project_dir / "uv.lock").exists()


def test_just_cov(copie):
    result = copie.copy()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()

    with plumbum.local.cwd(result.project_dir):
        plumbum.local.cmd.just("cov")
    assert (result.project_dir / "htmlcov" / "index.html").exists()


def test_just_lint(copie):
    result = copie.copy()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()

    with plumbum.local.cwd(result.project_dir):
        plumbum.local.cmd.just("lint")
    # how do we make sure lint was run?


def test_just_html(copie):
    result = copie.copy()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()

    with plumbum.local.cwd(result.project_dir):
        plumbum.local.cmd.just("html")
    assert (result.project_dir / "docs" / "build" / "html" / "index.html").exists()
