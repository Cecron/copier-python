set dotenv-load

ARGS_TEST := env("_UV_RUN_ARGS_TEST", "")

@_:
    just --list --justfile '{{ justfile() }}'

# run tests  Try -n auto (for xdist) or --keep-copied-projects
[group('qa')]
test *args:
    uv run {{ ARGS_TEST }} -m pytest {{ args }}

# ensure we have an up-to-date Python virtual environment
[group('lifecycle')]
install:
    if [ ! -d ".venv" ]; then uv venv --seed; fi
    uv pip install -r requirements.txt

# remove Python virtual environment and temporary files
[group('lifecycle')]
clean:
    rm -rf .venv .pytest_cache
    find . -type d -name "__pycache__" -exec rm -r {} +

# regenerate Python virtual environment from scratch
[group('lifecycle')]
fresh: clean install
