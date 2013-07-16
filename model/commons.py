import datetime
import pytz


def get_current_utcdatetime():
    return datetime.datetime.utcnow().replace(tzinfo=pytz.utc)


def get_past_utcdatetime(zero_hour=True, **deltatime_kwargs):
    current_datetime = get_current_utcdatetime()
    if zero_hour:
        current_datetime = current_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = datetime.timedelta(**deltatime_kwargs)
    return current_datetime - delta
