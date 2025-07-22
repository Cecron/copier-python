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

Generate a new project by using the `copier copy` command.

``` shell
C:\> copier copy --trust https://github.com/Cecron/copier-python.git my-proj
```

## Updating a project

Update the project by using the `copier update` command.
``` shell
C:\> copier update --trust my-proj
```

# Development

1. Clone the copier-python repository.
``` shell
C:\> git clone git@github.com:Cecron/copier-python
```

2. Generate a project from a local copy of the copier-python template
``` shell
C:\> copier copy --trust --vcs-ref=HEAD copier-python example-proj
```

3. Go into the template directory and edit some files in the template
``` shell
C:\> cd copier-python
```

4. Generate a new project based on the new template
``` shell
C:\> cd ..
C:\> copier copy --trust --vcs-ref=HEAD copier-python new-example-proj
```

5. Update the generated project
Before running `copier update`, we now need to commit the template.
``` shell
C:\> cd copier-python
C:\> git add . && git commit
```

We need to stand in the same directory as when the project was generated, since the path to the template in `.copier-answers.yml` is relative.

``` shell
C:\copier-template> cd ..
C:\> copier update --trust --pretend --skip-answered --vcs-ref=HEAD example-proj
```

Useful arguments to `copier`:
* **--trust**: Allow templates with unsafe features (tasks)
* **-r, --vcs-ref HEAD**: Checkout latest version
* **-n, --pretend**: Run but do not make any changes
* **-l, --defaults**: Use default answers to all questions

Useful arguments to `copier update`:
**--skip-answered**: Skip questions that have already been answered


5. When done, commit, add a tag, and push
``` shell
C:\> cd copier-template
C:\copier-template> git add .
C:\copier-template> git commit -m "Update template"
C:\copier-template> git tag -a 0.1.0 -m "New release"
C:\copier-template> git push origin
```
