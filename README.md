# A basic Copier template for Python projects managed by Uv.

[Copier](https://copier.readthedocs.io/) is a library for rendering project templates, which lives at [github.com/copier-org/copier](https://github.com/copier-org/copier/). This template has been updated to be used with Copier v.9.8.0
[Uv](https://docs.astral.sh/uv/) makes Python packaging and dependency management easy using pyproject.toml.

This Copier template is my first attempt at using these two tools togehter to make creating new Python projects easier on Windows.

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

Useful arguments to Copier:

**--skip-answered**: Skip questions that have already been answered
**--vcs-ref HEAD**: Checkout latest version
**--trust**: Allow templates with unsafe features (tasks)
**--pretend**: Run but do not make any changes

5. When done, commit, add a tag, and push
``` shell
C:\> cd copier-template
C:\copier-template> git add .
C:\copier-template> git commit -m "Update template"
C:\copier-template> git tag -a 0.1.0 -m "New release"
C:\copier-template> git push origin
```
