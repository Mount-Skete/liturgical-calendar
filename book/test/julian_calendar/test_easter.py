from unittest import TestCase

from julian_calendar import (
    calculate_orthodox_easter_julian,
    calculate_orthodox_easter_gregorian,
    calculate_catholic_easter_gregorian
)


class TestOrthodoxEasterCalculation(TestCase):
    EASTER_DATES = {
        2020: '2020-04-19T00:00:00',
        2021: '2021-05-02T00:00:00',
        2022: '2022-04-24T00:00:00',
        2023: '2023-04-16T00:00:00',
        2024: '2024-05-05T00:00:00',
        2025: '2025-04-20T00:00:00',
        2026: '2026-04-12T00:00:00',
        2027: '2027-05-02T00:00:00',
        2028: '2028-04-16T00:00:00',
        2029: '2029-04-08T00:00:00',
        2030: '2030-04-28T00:00:00',
        2031: '2031-04-13T00:00:00',
        2032: '2032-05-02T00:00:00',
    }

    EASTER_DATES_JULIAN = {
        2023: '2023-04-03T00:00:00',
        2024: '2024-04-22T00:00:00',
    }

    def test_verify_orthodox_easter_dates_in_gregorian_calendar(self):
        for year, iso in self.EASTER_DATES.items():
            actual = calculate_orthodox_easter_gregorian(year)

            self.assertEqual(actual.isoformat(), iso)

    def test_verify_orthodox_easter_dates_in_julian_calendar(self):
        for year, iso in self.EASTER_DATES_JULIAN.items():
            actual = calculate_orthodox_easter_julian(year)

            self.assertEqual(actual.isoformat(), iso)


class TestCatholicEasterCalculation(TestCase):
    EASTER_DATES = {
        1961: '1961-04-02T00:00:00',
        2020: '2020-04-12T00:00:00',
        2021: '2021-04-04T00:00:00',
        2022: '2022-04-17T00:00:00',
        2023: '2023-04-09T00:00:00',
        2024: '2024-03-31T00:00:00',
        2025: '2025-04-20T00:00:00',
        2026: '2026-04-05T00:00:00',
        2027: '2027-03-28T00:00:00',
        2028: '2028-04-16T00:00:00',
        2029: '2029-04-01T00:00:00',
        2030: '2030-04-21T00:00:00',
        2031: '2031-04-13T00:00:00',
        2032: '2032-03-28T00:00:00',
    }

    def test_verify_catholic_easter_dates_in_gregorian_calendar(self):
        for year, iso in self.EASTER_DATES.items():
            actual = calculate_catholic_easter_gregorian(year)

            self.assertEqual(actual.isoformat(), iso)
