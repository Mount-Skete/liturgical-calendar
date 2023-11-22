from datetime import datetime
from unittest import TestCase

from julian_calendar import calculate_echo_gregorian


class TestEchosCalculation(TestCase):
    PRE_EASTER_WEEK_ECHOS = {
        '2022-04-18T00:00:00': 2,
        '2022-04-21T00:00:00': 2,

        '2023-04-10T00:00:00': 2,
        '2023-04-15T00:00:00': 2,

        '2024-04-29T00:00:00': 6,
        '2024-05-03T00:00:00': 6,
    }

    EASTER_WEEK_ECHOS = {
        '2022-04-24T00:00:00': 1,
        '2022-04-25T00:00:00': 2,
        '2022-04-26T00:00:00': 3,
        '2022-04-27T00:00:00': 4,
        '2022-04-28T00:00:00': 5,
        '2022-04-29T00:00:00': 6,
        '2022-04-30T00:00:00': 8,

        '2023-04-16T00:00:00': 1,
        '2023-04-17T00:00:00': 2,
        '2023-04-18T00:00:00': 3,
        '2023-04-19T00:00:00': 4,
        '2023-04-20T00:00:00': 5,
        '2023-04-21T00:00:00': 6,
        '2023-04-22T00:00:00': 8,

        '2024-05-05T00:00:00': 1,
        '2024-05-06T00:00:00': 2,
        '2024-05-07T00:00:00': 3,
        '2024-05-08T00:00:00': 4,
        '2024-05-09T00:00:00': 5,
        '2024-05-10T00:00:00': 6,
        '2024-05-11T00:00:00': 8,
    }

    DATES_ECHOS = {
        # Sundays
        '2022-05-01T00:00:00': 1,
        '2022-05-08T00:00:00': 2,
        '2022-05-15T00:00:00': 3,
        '2022-05-22T00:00:00': 4,
        '2022-05-29T00:00:00': 5,
        '2022-06-05T00:00:00': 6,
        '2022-06-12T00:00:00': 7,
        '2022-06-19T00:00:00': 8,

        '2023-04-23T00:00:00': 1,
        '2023-04-30T00:00:00': 2,
        '2023-05-07T00:00:00': 3,
        '2023-05-14T00:00:00': 4,
        '2023-05-21T00:00:00': 5,
        '2023-05-28T00:00:00': 6,
        '2023-06-04T00:00:00': 7,
        '2023-06-11T00:00:00': 8,

        '2024-05-12T00:00:00': 1,
        '2024-05-19T00:00:00': 2,
        '2024-05-26T00:00:00': 3,
        '2024-06-02T00:00:00': 4,
        '2024-06-09T00:00:00': 5,
        '2024-06-16T00:00:00': 6,
        '2024-06-23T00:00:00': 7,
        '2024-06-30T00:00:00': 8,

        # Week days
        '2023-06-19T10:00:00': 1,
        '2023-06-27T10:00:00': 2,
        '2023-07-05T10:00:00': 3,
        '2023-07-13T10:00:00': 4,
        '2023-07-21T10:00:00': 5,
        '2023-07-29T10:00:00': 6,
        '2023-07-31T10:00:00': 7,
        '2023-08-08T10:00:00': 8,
    }

    def test_verify_echos_in_gregorian_calendar(self):
        for iso, echo in self.DATES_ECHOS.items():
            date = datetime.fromisoformat(iso)

            actual = calculate_echo_gregorian(date)

            self.assertEqual(actual, echo, f'Echo does not match for {iso}. {actual} != {echo}')

    def test_verify_pre_easter_week_echos_in_gregorian_calendar(self):
        for iso, echo in self.PRE_EASTER_WEEK_ECHOS.items():
            date = datetime.fromisoformat(iso)

            actual = calculate_echo_gregorian(date)

            self.assertEqual(actual, echo, f'Echo does not match for {iso}. {actual} != {echo}')

    def test_verify_easter_week_echos_in_gregorian_calendar(self):
        for iso, echo in self.EASTER_WEEK_ECHOS.items():
            date = datetime.fromisoformat(iso)

            actual = calculate_echo_gregorian(date)

            self.assertEqual(actual, echo, f'Echo does not match for {iso}. {actual} != {echo}')

    def test_verify_2023_feb_1_echo_in_gregorian_calendar(self):
        date = datetime(2023, 2, 1)
        expected = 8

        actual = calculate_echo_gregorian(date)

        self.assertEqual(
            actual,
            expected,
            f'Echo does not match for {date.isoformat()}. {actual} != {expected}',
        )
