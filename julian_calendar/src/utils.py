import math
from datetime import datetime, timedelta

from .easter import calculate_orthodox_easter_gregorian


def add_days(date: datetime, days: int) -> datetime:
    return date + timedelta(days=days)


def weeks_between(date1: datetime, date2: datetime) -> int:
    return int(math.fabs((date1 - date2).days / 7))


def days_between(date1: datetime, date2: datetime) -> int:
    return int(math.fabs((date1 - date2).days))


def is_same_day(date1: datetime, date2: datetime) -> bool:
    """
    Compares dates ignoring time.
    :param date1: First date
    :param date2: Second date
    :return: true if date matches
    """
    return date1.year == date2.year and date1.month == date2.month and date1.day == date2.day


def calculate_echo_gregorian(date: datetime) -> int:
    """
    Calculates Echo for a given date in Gregorian calendar.
    :param date: Date in Gregorian calendar
    :return: Echo as number 1 to 8.
    """
    year = date.year
    easter = calculate_orthodox_easter_gregorian(year)
    echo_start = add_days(easter, 7)

    # Bright Week Saturday should have echo 8.
    if is_same_day(date, add_days(easter, 6)):
        return 8

    # Bright Week should have echo calculated by days.
    if easter <= date <= add_days(easter, 6):
        return days_between(easter, date) + 1

    # Date is before year's Easter.
    # Calculating from previous Easter.
    if date < echo_start:
        echo_start = add_days(calculate_orthodox_easter_gregorian(year - 1), 7)

    weeks = math.floor(weeks_between(date, echo_start))
    echo = (weeks % 8) + 1

    return echo
