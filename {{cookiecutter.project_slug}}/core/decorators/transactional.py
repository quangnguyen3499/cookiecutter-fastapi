from functools import wraps

from configs.database import get_db
from core.loggers.app_logging import logger


def transactional(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        db_session = kwargs.get("db", next(get_db()))
        if db_session is None:
            raise ValueError("No database session")

        try:
            result = func(*args, **kwargs)
            db_session.commit()
            return result
        except Exception as e:
            db_session.rollback()
            logger.error(f"Error during transaction: {repr(e)}")
            raise

    return wrapper
