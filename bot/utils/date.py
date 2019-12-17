import datetime


def get_time_delta(n):
    """
    Returns `timedelta` object of `n` days.
    """
    return datetime.timedelta(days=n)


def get_current_india_time():
    """
    Returns current India time.
    """
    india_offset = datetime.timedelta(hours=5, minutes=30)
    in_time = datetime.datetime.utcnow() + india_offset
    return in_time


def get_next_closest_day(weekday):
    """
    Takes a weekday and returns the next closest weekday from the current date.
    For eg. if the `weekday` is monday, then the function returns the date
    which will be the next closest monday from the current date.
    """
    names = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
    }

    today = get_current_india_time().date()
    day_shift = (names[weekday] - today.weekday()) % 7
    next_day = datetime.datetime.combine(
        today + datetime.timedelta(days=day_shift), datetime.time.min)

    if next_day.weekday() == today.weekday():
        next_day = next_day + datetime.timedelta(days=7)
    return next_day


def get_last_monday():
    """
    Gets the last monday from the current date.
    """
    today = get_current_india_time()
    # Weekday for Monday is 0.
    if today.date().weekday() == 0:
        ts = today.replace(hour=0, minute=0, second=0, microsecond=0)
    else:
        next_monday = get_next_closest_day("monday")
        week_delta = get_time_delta(7)
        ts = next_monday - week_delta
    return ts


def get_from_to(days=7):
    """
    Gets a start and end date with separated by `days` days. start date will
    always be the last monday.
    """
    date_to = get_last_monday()
    week_delta = get_time_delta(days)
    date_from = date_to - week_delta
    return date_from, date_to


day_delta = get_time_delta(1)
week_delta = get_time_delta(7)

closest_monday = get_next_closest_day("monday")
closest_tuesday = get_next_closest_day("tuesday")
closest_wednesday = get_next_closest_day("wednesday")
closest_thursday = get_next_closest_day("thursday")
closest_friday = get_next_closest_day("friday")
closest_saturday = get_next_closest_day("saturday")
closest_sunday = get_next_closest_day("sunday")
