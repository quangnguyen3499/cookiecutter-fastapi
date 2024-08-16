FastAPI Cookiecutter Template
=============================

## !Important TODO:
- Add decorator method class
- Refactor SQLAlchemy

Introduction
------------

This projects consist of a `cookiecutter` template that generates a full structure
for creating a RESTful API service project based on FastAPI following the MVC
(Model-View-Controller) structure.

While using this project, you will be asked to provide some inputs such the authors, the name of the project, etc. As result you will obtain the
complete file and folder structure to quickly start to code your project.

Prerequisites
-------------

It uses ``Python`` (>=3.10) behind the scenes. Please install the Python package `cookiecutter` before using it.

Project Generation Options
--------------------------

project_name:
  Your project's human-readable name, capitals and spaces allowed.

project_slug:
    Your project's slug without dashes or spaces. Used to name your repo
    and in other places where a Python-importable version of your project name
    is needed.

author:
    This is you! The value goes into places like ``README.md`` and such.

email:
    The email address you want to identify yourself in the project.

short_description:
    Describes your project briefly and gets used in places like ``README.md``.

version:
    The version of the project at its inception.

use_database:
    Indicates whether the project should be configured for using database. The choices are:

    1. PostgreSQL
    2. MySQL
    3. No

ci_tool:
    Select a CI tool. The choices are:

    1. GitHub
    2. GitLab
    3. Bitbucket
    4. None

python_version:
    Select the python version for configuring the created project's CI/CD pipeline. The choices are:

    1. 3.12
    2. 3.11
    3. 3.10

Tutorial
--------

First, get Cookiecutter. Trust me, it's awesome::

    $ pip install "cookiecutter>=1.7.0"

Now run it against this repo::

    $ cookiecutter`<path-to-local-folder>`

Redirect to project folder

    $ pre-commit install

You'll be prompted for some values. Provide them, then a FastAPI project will be created for you.

Project Structure
-----------------

Files related to application are in the ``<project_slug`` directories.
Application components are::

    {{cookiecutter.project_slug}}
    ├-- alembic                         - migrations folder
    ├── app                             - main app
    ├-- celery_task                     - celery tasks folder
    ├-- configs
    ├-- core
    ├-- docker
    ├── docs                            - project documentation
    ├-- nginx
    ├-- resources
    ├── scripts                         - scripts
    │   │   ├── database_backup         - database script backup
    │   │   ├── database_restore        - database script restore from backup
    │   │   ├── celery_beat.sh          - run celery scheduler
    │   │   ├── celery_worker.sh        - run celery worker
    │   │   ├── format
    │   │   ├── makemigrations
    │   │   ├── migrate
    │   │   ├── start-dev.sh            - start app in dev/local
    │   │   ├── start-prod.sh           - start app in prod
    ├── static                          - static files
    ├── templates                       - templates
    ├── tests                           - unit tests
    │   ├── conftest.py                 - fixtures in tests
    │   └── ...
    ├── README.md                       - documentation
    ├── .env.example
    ├── .gitlab-ci.yml                  - CI/CD for Gitlab
    ├── bitbucket-pipelines.yml         - CI/CD for Bitbucket
    ├── buildspec.yml                   - CI/CD for AWS CodeCommit
    ├── alembic.ini
    ├── .pre-commit-config.yaml
    ├── logging.ini
    ├── logging_prod.ini
    ├── main.py
    ├── pyproject.toml                  - libraries used in application

Reference
---------

.. _`cookiecutter`: https://github.com/cookiecutter/cookiecutter


.. _uvicorn-gunicorn-docker: https://github.com/tiangolo/uvicorn-gunicorn-docker
