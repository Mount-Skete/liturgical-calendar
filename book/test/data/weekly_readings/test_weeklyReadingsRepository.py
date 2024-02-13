import os
import unittest

from data.weekly_readings import WeeklyReadingsRepository


class WeeklyReadingsRepositoryTestCase(unittest.TestCase):
    WEEKLY_READINGS_DATA_PATH = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        'res',
        'weekly_readings.xml'
    )

    repo: WeeklyReadingsRepository

    def setUp(self):
        self.repo = WeeklyReadingsRepository(self.WEEKLY_READINGS_DATA_PATH)

    def test_load_all(self):
        self.assertGreater(len(self.repo.weekly_readings), 0)


if __name__ == '__main__':
    unittest.main()
