FROM python:3.12-slim

LABEL maintainer="{{ cookiecutter.email }}"

RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt clean && \
    rm -rf /var/cache/apt/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8

RUN pip install poetry

WORKDIR /src
COPY pyproject.toml /src/

COPY . /src

ENV PATH "$PATH:/src/scripts"

WORKDIR /src

COPY scripts/ /src/scripts/
RUN poetry lock
RUN poetry install --no-root --no-interaction
RUN find /src/scripts -type f -iname '*.sh' -exec chmod +x {} +

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

RUN exec "$0"
