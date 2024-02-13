import unittest
import os
from data.weekly_readings import WeeklyReadingsRepository, WeeklyReadingDateType
from datetime import datetime


class WeeklyReadingsTestCase(unittest.TestCase):
    WEEKLY_READINGS_DATA_PATH = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        '..',
        '..',
        'data',
        'gospel-and-apostolic-readings-ru',
        'weekly-readings-index.xml'
    )

    repo: WeeklyReadingsRepository

    def setUp(self):
        self.repo = WeeklyReadingsRepository(self.WEEKLY_READINGS_DATA_PATH)

    def test_weekly_readings_easter(self):
        actual = self.repo.weekly_readings.for_date(datetime(2024, 5, 5))

        self.assertIsNotNone(actual)
        self.assertIsNotNone(actual.week.title)

        self.assertEqual(WeeklyReadingDateType.Easter, actual.week.date.date_type)
        self.assertEqual(1, actual.week.date.week)

    def test_weekly_readings_easter_1(self):
        actual = self.repo.weekly_readings.for_date(datetime(2024, 5, 6))

        self.assertIsNotNone(actual)
        self.assertIsNotNone(actual.week.title)

        self.assertEqual(WeeklyReadingDateType.Easter, actual.week.date.date_type)
        self.assertEqual(1, actual.week.date.week)

    # def test_weekly_readings_pentecost_week(self):
    #     actual = self.repo.weekly_readings.for_date(datetime(2024, 6, 23))
    #
    #     self.assertIsNotNone(actual)
    #     self.assertIsNotNone(actual.week.title)
    #
    #     self.assertEqual(WeeklyReadingDateType.Easter, actual.week.date.date_type)
    #     self.assertEqual(8, actual.week.date.week)

    def test_weekly_readings_pentecost_1(self):
        actual = self.repo.weekly_readings.for_date(datetime(2024, 6, 30))

        self.assertIsNotNone(actual)
        self.assertIsNotNone(actual.week.title)

        self.assertEqual(WeeklyReadingDateType.Pentecost, actual.week.date.date_type)
        self.assertEqual(1, actual.week.date.week)

    # def test_weekly_readings_pentecost_33(self):
    #     actual = self.repo.weekly_readings.for_date(datetime(2024, 2, 12))
    #
    #     self.assertIsNotNone(actual)
    #     self.assertIsNotNone(actual.week.title)
    #
    #     self.assertEqual(WeeklyReadingDateType.Pentecost, actual.week.date.date_type)
    #     self.assertEqual(1, actual.week.date.week)


if __name__ == '__main__':
    unittest.main()
