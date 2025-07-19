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
C:\> copier update myproj
```

# Development

1. Clone the copier-python repository.
``` shell
C:\> git clone git@github.com:Cecron/copier-python
```

2. Generate a project from a local copy of the copier-python template
``` shell
C:\> copier copy --vcs-ref=HEAD copier-python example-proj
```

3. Go into the template and edit
``` shell
C:\> cd copier-python
```


4. Update the generated project
We need to stand in the same directory as when the project was generated, since the path to the template in `.copier-answers.yml` is relative.

``` shell
C:\copier-template> cd ..
C:\> copier update
```
To update to the latest commit, add `--vcs-ref=HEAD`.


5. When done, commit, add a tag, and push
``` shell
C:\> cd copier-template
C:\copier-template> git add .
C:\copier-template> git commit -m "Update template"
C:\copier-template> git tag -a 0.1.0 -m "New release"
C:\copier-template> git push origin
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
