import logging.config
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)
log_handler = TimedRotatingFileHandler(
    f'logs/celery_sync_{datetime.now().strftime("%Y-%m-%d")}.log',
    when="midnight",
    interval=1,
    backupCount=7,
)

log_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d - %(message)s",
    ),
)

logging.getLogger().addHandler(log_handler)
logging.getLogger().setLevel(logging.INFO)
