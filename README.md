# A basic Copier template for Python projects managed by Poetry.

[Copier](https://copier.readthedocs.io/) is a library for rendering project templates, which lives at [github.com/copier-org/copier](https://github.com/copier-org/copier/).
[Poetry](https://python-poetry.org/) makes Python packaging and dependency management easy using pyproject.toml, and lives at [github.com/python-poetry/poetry](https://github.com/python-poetry/poetry/)

This copier template is my first attempt at using these two tools togehter to make creating new Python projects easier on Windows.

## Usage

I'm more of a traditionalist and want the virtual environment files in a .venv directory in each project, so I have done:
``` shell
PS C:\> poetry config virtualenvs.in-project true
```
This will globally configure poetry to do so and will let me do the following:

``` shell
PS C:\> copier https://github.com/Cecron/copier-python.git myproj
PS C:\> cd myproj
PS C:\> poetry install
PS C:\> py -3 -m venv .\.venv\ --prompt .  # Set virtual env prompt to show directory name
PS C:\> .venv\Scripts\activate.ps1
```


To give a basic understanding of how to create and use a copier template, I'll show how the first versions of this template was created, including how to apply the template to both generate a new project and also how to update the project whith a an improved version of the template.

### Create a directory to place the template in

``` shell
PS C:\> mkdir copier-template
PS C:\> cd copier-template
```

#### Create a short `pyproject.toml.tmpl` with ninja variables like `[[ package_name ]]`

``` shell
PS C:\copier-template> type pyproject.toml.tmpl
[build-system]
requires = ["poetry>=0.12"]
build-backend = "poetry.masonry.api"

[tool.poetry]
name = "[[ package_name ]]"
version = "0.1.0"
description = "[[ package_description ]]"
authors = ["[[ author_name ]] <[[ author_email ]]>"]
maintainers = ["[[ author_name ]] <[[ author_email ]]>"]
license = "[[ copyright_license ]]"
readme = "README.rst"

[tool.poetry.dependencies]
python = "^3.8"

[tool.poetry.dev-dependencies]
pytest = "^5.2"
```

### Create `copier.yaml` with questions and settings

``` shell
PS C:\copier-template> type copier.yaml
package_name: mypackage
package_description: A short description of the package.
author_name: Cecron
author_email: Cecron@example.com
copyright_license: "CC-BY-4.0"

_exclude:
    # Exclude git repo
    - ".git"
    # Don't match emacs backup files
    - "*~"
```

### Create `[[ _copier_conf.answers_file ]].tmpl` so copier registers answers

``` shell
PS C:\copier-template> type *answers*
# Changes here will be overwritten by Copier
[[_copier_answers|to_nice_yaml]]
```

### Register, commit and create a tag in git

``` shell
PS C:\copier-template> git init
PS C:\copier-template> git add .
PS C:\copier-template> git commit -m "Initial template version"
PS C:\copier-template> git tag -a 0.1.0 -m "Initial release"
```

### Run copier to create project

``` shell
PS C:\copier-template> cd ..
PS C:\> copier copier-template myproj
# Answer questions
package_name? Format: yaml
🎤 [mypackage]:

package_description? Format: yaml
🎤 [A short description of the package.]:

author_name? Format: yaml
🎤 [Cecron]:

author_email? Format: yaml
🎤 [Cecron@example.com]:

copyright_license? Format: yaml
🎤 [CC-BY-4.0]:

    create  copier.yaml
    create  pyproject.toml
    create  .copier-answers.yml
```

### Run Poetry to install the dependencies and create virtual environment

``` shell
PS C:\> cd myproj
PS C:\myproj> poetry install
```

### Register project and commit to git

``` shell
PS C:\myproj> git init
PS C:\myproj> git add .
PS C:\myproj> git commit -m "Initial project version"
```

### Do some updates in the project, e.g. add a `main.py`, and commit

``` shell
PS C:\myproj> type main.py
print("Hello World")
PS C:\myproj> git add main.py
PS C:\myproj> git commit -m "Added main.py"
```

### Do an update to the template, e.g. add a `.gitignore`, and commit

``` shell
PS C:\myproj> cd ..\copier-template
PS C:\copier-template> type .gitignore
# Emacs backup files
*~
\#*\#
PS C:\copier-template> git add .gitignore
PS C:\copier-template> git commit -m "Added gitignore file"
PS C:\copier-template> git tag -a 0.2.0 -m "Release of v0.2.0"
```

### Update the project from the template

You need to stand in the same directory as when you created the project,
since the path to the template in `.copier-answers.yml` is relative

``` shell
PS C:\copier-template> cd ..
PS C:\> copier update myproj

package_name? Format: yaml
🎤 [mypackage]:

package_description? Format: yaml
🎤 [A short description of the package.]:

author_name? Format: yaml
🎤 [Cecron]:

author_email? Format: yaml
🎤 [Cecron@example.com]:

copyright_license? Format: yaml
🎤 [CC-BY-4.0]:

    create  .gitignore
 identical  copier.yaml
 identical  pyproject.toml
  conflict  .copier-answers.yml
 Overwrite C:\proj\python\copier\tagtest\myproj\.copier-answers.yml? [Y/n]
     force  .copier-answers.yml
```

### Review changes made, and commit

``` shell
(copier) PS C:\myproj> git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .copier-answers.yml

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore

no changes added to commit (use "git add" and/or "git commit -a")

PS C:\> cd myproj
PS C:\myproj> git diff
diff --git a/.copier-answers.yml b/.copier-answers.yml
index 2850703..ba49cb9 100644
--- a/.copier-answers.yml
+++ b/.copier-answers.yml
@@ -1,5 +1,5 @@
 # Changes here will be overwritten by Copier
-_commit: 1b4d418
+_commit: a86b2dd^M
 _src_path: copier-template
 author_email: Cecron@example.com
 author_name: Cecron
PS C:\> git add .gitignore
PS C:\> git commit -a -m "Updated to template v0.2.0"
```
