import math
from datetime import datetime
from .open_calendar import julian_to_gregorian


def calculate_orthodox_easter_julian(year: int) -> datetime:
    """
    Calculates Orthodox Easter date in Julian calendar.
    Calculation is performed according to Meeus's Julian algorithm.

    https://en.wikipedia.org/wiki/Date_of_Easter#Meeus's_Julian_algorithm
    :param year: year
    :return: Easter date in UTC time zone.
    """
    a = year % 4
    b = year % 7
    c = year % 19
    d = (19 * c + 15) % 30
    e = (2 * a + 4 * b - d + 34) % 7
    month = math.floor((d + e + 114) / 31)
    day = ((d + e + 114) % 31) + 1

    return datetime(year, month, day)


def calculate_orthodox_easter_gregorian(year: int) -> datetime:
    """
    Calculation is performed according to Meeus's Julian algorithm
    and converts it to Gregorian calendar.

    https://en.wikipedia.org/wiki/Date_of_Easter#Meeus's_Julian_algorithm
    :param year: year
    :return: Easter date in UTC time zone.
    """
    return julian_to_gregorian(calculate_orthodox_easter_julian(year))


def calculate_catholic_easter_gregorian(year: int) -> datetime:
    """
    Calculates Catholic Easter date in Gregorian calendar.
    Calculation is performed according to corrected Meeus/Jones/Butcher algorithm.

    https://en.wikipedia.org/wiki/Date_of_Easter#Anonymous_Gregorian_algorithm
    :param year: year
    :return: Easter date in UTC time zone.
    """
    a = year % 19
    b = math.floor(year / 100)
    c = year % 100
    d = math.floor(b / 4)
    e = b % 4
    g = math.floor((8 * b + 13) / 25)
    h = (19 * a + b - d - g + 15) % 30
    i = math.floor(c / 4)
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = math.floor((a + 11 * h + 19 * l) / 433)
    n = math.floor((h + l - 7 * m + 90) / 25)
    p = (h + l - 7 * m + 33 * n + 19) % 32

    return datetime(year, n, p)
