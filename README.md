# A basic Copier template for Python projects managed by Uv.

This Copier template is my attempt at creating new Python projects easier on Windows and Linux.

## Features
  * [Copier](https://copier.readthedocs.io/): A library and CLI app for rendering project templates.
  * [Just](https://github.com/casey/just): A handy way to save and run project-specific commands.
  * [Uv](https://docs.astral.sh/uv/): An extremely fast Python package and project manager, written in Rust.
  * [Pytest](https://docs.pytest.org/en/stable/): Makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.
  * [Sphinx-autobuild](https://github.com/sphinx-doc/sphinx-autobuild): Rebuilds Sphinx documentation on changes, with hot reloading in the browser.

## Requirement
This Copier template takes advantage of the following, which needs to be installed[^1]:
1. [Git](https://git-scm.com/downloads/): Download and run installer.[^2]
2. [Uv](https://docs.astral.sh/uv/getting-started/installation/): Prefer standalone installer method.
3. [Copier](https://github.com/copier-org/copier/): Run `uv tool install copier`.
4. [Just](https://github.com/casey/just/releases): Download and extract binary.

[^1]: All required software are available both for Windows and Linux.

[^2]: When installing Git on Windows, remember to add the installation path (e.g. `C:\Program Files\Git\usr\bin`) **first** to your `PATH` environment variable so the correct version of `find` is used in Just recipes.

## Generating a project

Generate a new project by running the `copier copy` command and answer the questions.

``` shell
C:\> copier copy --trust https://github.com/Cecron/copier-python.git my-proj
```

Copier can use dangerous features that allow arbitrary code execution in tasks and migrations. The flag `--trust` is needed in order to run tasks and migrations in this template.
[Please be sure you understand the risks when allowing unsafe features!](https://copier.readthedocs.io/en/stable/configuring/#unsafe)

## Working on the project
Move into the generated project and work on the code. There is a Justfile here that simplifies some tasks:

``` shell
C:\> cd my-proj
C:\> just
Available recipes:
    all         # run all main recepies: fresh, check-all, html

    [docs]
    html        # run Sphinx to build html documentation
    serve *args # serve html documentation

    [lifecycle]
    clean       # remove all built files
    fresh       # recreate projects virtualenv from scratch
    install     # ensure project virtualenv is up to date
    upgrade     # upgrade dependencies in pyproject.toml

    [qa]
    check-all   # perform all checks
    cov         # run tests and measure coverage
    lint        # run Ruff linter and formatter
    test *args  # run Pytest
```

## Updating the project
When a new version of the template is available, the generated project can be updated with the changes.
Make sure all files in the project are committed, and update the project by using the `copier update` command.

``` shell
C:\> git add . && git commit
C:\> copier update --trust --skip-answered
```

The flag `--skip-answered` will make Copier only ask newly added questions.

# Development
When editing the template, follow the following steps.

## Setup
Clone the copier-python repository.
``` shell
C:\> git clone git@github.com:Cecron/copier-python
```

Go into the cloned directory and setup a Python virtual environment using the just command.
``` shell
C:\> cd copier-python
C:\> just install
```

You may now edit the template.


## Generating and Updating project
When the template is ready for testing, generate a project from the local copy of the copier-python template
``` shell
C:\copier-python\> cd ..
C:\> copier copy --trust --vcs-ref=HEAD copier-python example-proj
```

The generated project can also be updated with the template changes.
Before running `copier update`, we need to commit both the generated project and the template.
``` shell
C:\> cd example-proj
C:\> git add . && git commit
C:\> cd ../copier-python
C:\> git add . && git commit
```

We also need to be standing in the same directory as when the project was generated, since the path to the template in `.copier-answers.yml` is relative.

``` shell
C:\copier-template> cd ..
C:\> copier update --trust --pretend --skip-answered --vcs-ref=HEAD example-proj
```

Useful arguments to `copier`:
* **--trust**: Allow templates with unsafe features (e.g. tasks)
* **-r, --vcs-ref HEAD**: Checkout latest version
* **-n, --pretend**: Run but do not make any changes
* **-l, --defaults**: Use default answers to all questions

Useful arguments to `copier update`:
* **- A, --skip-answered**: Skip questions that have already been answered

## Running Tests
Run tests that generates a project from the template and runs some Just commands in the newly generated project.

``` shell
C:\> cd copier-python
C:\copier-python> uv run -m pytest
```
