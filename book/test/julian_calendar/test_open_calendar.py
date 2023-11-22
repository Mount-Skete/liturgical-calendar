from datetime import datetime
from unittest import TestCase

from julian_calendar import (
    is_leap_julian_year,
    julian_to_julian_day,
    julian_to_gregorian,
    is_leap_gregorian_year,
    gregorian_to_julian_day,
    gregorian_to_julian
)


class TestIsLeapJulianYear(TestCase):
    def test_verify_leap_year(self):
        actual = is_leap_julian_year(2020)

        self.assertEqual(actual, True)

    def test_verify_non_leap_year(self):
        actual = is_leap_julian_year(2021)

        self.assertEqual(actual, False)


class TestJulianToJulianDayConversion(TestCase):
    def test_convert_non_leap_recent_date(self):
        feb1 = datetime(2023, 2, 1)

        actual = julian_to_julian_day(feb1)

        self.assertEqual(actual, 2459989.5)

    def test_convert_leap_recent_date(self):
        jul1 = datetime(2020, 7, 1)

        actual = julian_to_julian_day(jul1)

        self.assertEqual(actual, 2459044.5)


class TestJulianToGregorian(TestCase):
    def test_converts_date_within_month(self):
        feb1 = datetime(2023, 2, 1)

        actual = julian_to_gregorian(feb1)

        self.assertEqual(actual.isoformat(), '2023-02-14T00:00:00')


class TestIsLeapGregorianYear(TestCase):
    def test_verify_leap_year(self):
        actual = is_leap_gregorian_year(2020)

        self.assertEqual(actual, True)

    def test_verify_non_leap_year(self):
        actual = is_leap_gregorian_year(2021)

        self.assertEqual(actual, False)


class TestGregorianToJulianDayConversion(TestCase):
    def test_converts_non_leap_recent_date(self):
        feb1 = datetime(2023, 2, 1)

        actual = gregorian_to_julian_day(feb1)

        self.assertEqual(actual, 2459976.5)

    def test_converts_leap_recent_date(self):
        jul1 = datetime(2020, 7, 1)

        actual = gregorian_to_julian_day(jul1)

        self.assertEqual(actual, 2459031.5)


class TestGregorianToJulianConversion(TestCase):

    def test_converts_date_within_month(self):
        feb1 = datetime(2023, 2, 14)

        actual = gregorian_to_julian(feb1)

        self.assertEqual(actual.isoformat(), '2023-02-01T00:00:00')
