#!/bin/bash

LOG_FILE_PATH="logs/celery_sync_$(date +\%Y-\%m-\%d).log"
poetry run celery -A celery_task.celery_app beat --loglevel=INFO 2>&1 | tee -a $LOG_FILE_PATH
