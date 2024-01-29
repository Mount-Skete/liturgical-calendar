import unittest
from datetime import datetime

from data.utils import Weekday


class WeekdayTestCase(unittest.TestCase):
    def test_from_value_valid(self):
        actual = Weekday.from_value("wed")

        self.assertEqual(Weekday.WED, actual)

    def test_matches_date_valid(self):
        actual = Weekday.WED.matches_date(datetime(2024, 1, 24))

        self.assertTrue(actual)

    def test_does_not_matches_date_valid(self):
        actual = Weekday.MON.matches_date(datetime(2024, 1, 24))

        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
