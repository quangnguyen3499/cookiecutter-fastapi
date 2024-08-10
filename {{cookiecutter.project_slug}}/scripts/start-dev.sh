#!/usr/bin/env bash

set -e

DEFAULT_MODULE_NAME=main

MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE_NAME}
VARIABLE_NAME=${VARIABLE_NAME:-app}
export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8000}
LOG_LEVEL=${LOG_LEVEL:-info}
LOG_CONFIG=${LOG_CONFIG:-/src/logging.ini}

# Start Uvicorn with live reload
bash scripts/migrate
poetry run uvicorn --proxy-headers --host $HOST --port $PORT "$APP_MODULE"
