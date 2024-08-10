from celery import Celery

import celery_task.tasks  # noqa
from configs.common_config import settings


celery_app = Celery("{{ cookiecutter.project_slug }}_cronjob", broker=settings.CELERY_BROKER_URL)

celery_app.conf.beat_schedule = {
    # Define your cron job here
    # "sync-airtable-every-midnight": {
    #     "task": "celery_task.tasks.sync_db.sync_airtable_task",
    #     "schedule": crontab(hour="0", minute="0"),
    # }
}
celery_app.conf.timezone = "UTC"
