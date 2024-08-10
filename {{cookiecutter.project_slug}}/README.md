## FastAPI CookieCutter

This project using FastAPI to build Backend platform

### Installation

- Create a new virtual environment with **Python >= 3.10**
- Install dependencies:

  - Install ``poetry`` [here](https://python-poetry.org/docs/#installing-with-the-official-installer) for the entire OS or with ``pip install poetry==1.7.0`` for your current environment only
  - Install all nessecary packages and dependecies through:

    ```
    poetry install --no-root
    ```
- Create an .env file with the content from .env.example
- Run ``pre-commit install`` in your terminal to install pre-commit hooks

  + **Optional**: you can run ``pre-commit run --all-files`` to run the pre-commit hooks against all your files in current working directory

## Installing and runnning project

1. `cp .env.example .env`
2. `cd docker`
3. `docker-compose -f docker-compose.yml up -d --build`

### Migrations

- Create an automatic migration from changes in `configs/database/db.py`

```shell
docker compose exec app scripts/makemigrations *migration_name*
```

- Run migrations

```shell
docker compose exec app scripts/migrate
```

  Downgrade migrations

```shell
docker compose exec app downgrade -1  # or -2 or base or hash of the migration
```

### Tests

All tests are integrational and require DB connection.

- Tests are run with upgrading & downgrading alembic migrations.
- Run `pytest` for testing all functions

  or `pytest <path_to_file>` to run for a specific test file.
