# Step 1 Create Repo

# Step 2 clone repo

Run `git clone <ssh path>`

# Step 3 initialize package (uv)

Run `uv init --package` in the directory

# Step 4 ensure ruff and pytest are installed as dev dependancies

Run `uv add ruff --dev` and
`uv add pytest --dev`

# Add Trusted publisher keys

# Testing and Linting

If you are using a tests folder ensure there is an __init__.py file so pytest recognizes it is not a flat directory structure. Additionally, ensure that you are importing src.<package_name>

testing is run with `uv run pytest`
linting is run with `uv run ruff check`
and `uv run ruff format` 
