from datetime import datetime, timedelta


def get_current_datetime() -> datetime:
    """Get current date, considering time offset"""

    return datetime.utcnow() - timedelta(hours=3)
