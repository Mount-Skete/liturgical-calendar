"""
Julian and Gregorian calendars calculations are based
on the algorithms from Fourmilab.

https://www.fourmilab.ch/documents/calendar/
"""
import math
from datetime import datetime

GREGORIAN_EPOCH = 1721425.5


def mod(a, b):
    return a - (b * math.floor(a / b))


def is_leap_gregorian_year(year: int):
    """
    Is a given year in the Gregorian calendar a leap year?
    :param year: Year
    :return: true if the given year is a leap year
    """
    return ((year % 4) == 0) and (not (((year % 100) == 0) and ((year % 400) != 0)))


def is_leap_julian_year(year):
    """
    Is a given year in the Julian calendar a leap year?
    :param year: Year
    :return: true if the given year is a leap year
    """
    return mod(year, 4) == (0 if (year > 0) else 3)


def gregorian_to_jd(year: int, month: int, day: int):
    return (((((GREGORIAN_EPOCH - 1)
               + (365 * (year - 1))
               + math.floor((year - 1) / 4))
              + (-math.floor((year - 1) / 100)))
             + math.floor((year - 1) / 400))
            + math.floor((((367 * month) - 362) / 12)
                         + (0 if (month <= 2) else
                            (-1 if is_leap_gregorian_year(year) else -2)
                            )
                         + day))


def gregorian_to_julian_day(date: datetime):
    """
    Calculates Julian day number from Gregorian calendar date.
    :param date: Gregorian calendar date
    :return: Julian day number for a given date
    """
    return gregorian_to_jd(date.year, date.month, date.day)


def julian_to_julian_day(date: datetime):
    """
    Calculates Julian day number from Julian calendar date.
    :param date: Julian calendar date
    :return: Julian day number
    """
    year = date.year
    month = date.month
    day = date.day

    # Adjust negative common era years to the zero-based notation we use.
    if year < 1:
        year += 1

    # Algorithm as given in Meeus, Astronomical Algorithms, Chapter 7, page 61
    if month <= 2:
        year -= 1
        month += 12

    return ((math.floor((365.25 * (year + 4716)))
             + math.floor((30.6001 * (month + 1))) + day)
            - 1524.5)


def julian_day_to_gregorian(julianDay: float):
    """
    Calculates Gregorian calendar date from Julian day.
    :param julianDay: Julian day
    :return: Gregorian calendar date
    """
    wjd = math.floor(julianDay - 0.5) + 0.5
    depoch = wjd - GREGORIAN_EPOCH
    quadricent = math.floor(depoch / 146097)
    dqc = mod(depoch, 146097)
    cent = math.floor(dqc / 36524)
    dcent = mod(dqc, 36524)
    quad = math.floor(dcent / 1461)
    dquad = mod(dcent, 1461)
    yindex = math.floor(dquad / 365)

    year = (quadricent * 400) + (cent * 100) + (quad * 4) + yindex
    if not ((cent == 4) or (yindex == 4)):
        year += 1

    yearday = wjd - gregorian_to_jd(year, 1, 1)
    leapadj = (0 if (wjd < gregorian_to_jd(year, 3, 1)) else
               (1 if is_leap_gregorian_year(year) else 2))
    month = math.floor((((yearday + leapadj) * 12) + 373) / 367)
    day = (wjd - gregorian_to_jd(year, month, 1)) + 1

    return datetime(year, month, int(day))


def julian_day_to_julian(julianDay):
    """
    Calculates Julian calendar date from Julian day.
    :param julianDay: Julian day number
    :return: Julian date as Date object
    """
    jd = julianDay + 0.5
    z = math.floor(jd)

    a = z
    b = a + 1524
    c = math.floor((b - 122.1) / 365.25)
    d = math.floor(365.25 * c)
    e = math.floor((b - d) / 30.6001)

    month = math.floor((e - 1) if (e < 14) else (e - 13))
    year = math.floor((c - 4716) if (month > 2) else (c - 4715))
    day = b - d - math.floor(30.6001 * e)

    """
    If year is less than 1, subtract one to convert from
    a zero based date system to the common era system in
    which the year -1 (1 B.C.E) is followed by year 1 (1 C.E.). 
    """
    if year < 1:
        year -= 1

    return datetime(year, month, day)


def gregorian_to_julian(date: datetime):
    """
    Converts date in Gregorian calendar to a date in Julian calendar.
    :param date: Julian calendar date.
    :return: Gregorian calendar date.
    """
    return julian_day_to_julian(gregorian_to_julian_day(date))


def julian_to_gregorian(date: datetime):
    """
    Converts date in Julian calendar to a date in Gregorian calendar.
    :param date: Julian calendar date.
    :return: Gregorian calendar date.
    """
    return julian_day_to_gregorian(julian_to_julian_day(date))
