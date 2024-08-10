from datetime import datetime
from datetime import timezone


def datetime_to_string(data: datetime) -> str:
    """
    Format a datetime object to a string using the specified format.

    Parameters:
        dt (datetime): The datetime object to be formatted.
        format (str): The format string for the desired output. Default is "%Y-%m-%d %H:%M:%S".

    Returns:
        str: The formatted string representation of the datetime object.
    """
    return data.strftime("%Y-%m-%d %H:%M:%S")


def current_time() -> datetime:
    return datetime.now(timezone.utc).replace(tzinfo=None)
