import os
import unittest
from datetime import datetime

from data.fasts import FastsRepository
from julian_calendar import julian_to_gregorian


class FastsTestCase(unittest.TestCase):
    FASTS_DATA_PATH = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        '..',
        '..',
        'data',
        'fasts-ru',
        'fasts.xml'
    )

    repo: FastsRepository

    def setUp(self):
        self.repo = FastsRepository(2024, self.FASTS_DATA_PATH)

    def test_by_id(self):
        actual = self.repo.fasts.by_id('fast:ordinary')

        self.assertEqual('fast:ordinary', actual.id)

    def test_fasts_ordinary_mon(self):
        actual = self.repo.fasts.for_date(datetime(2024, 1, 22))

        self.assertIsNone(actual.fast)
        self.assertEqual('no-fast', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_fasts_ordinary_wed(self):
        actual = self.repo.fasts.for_date(datetime(2024, 1, 24))

        self.assertIsNotNone(actual.fast)
        self.assertEqual('oil', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_fasts_ordinary_thu(self):
        actual = self.repo.fasts.for_date(datetime(2024, 1, 25))

        self.assertIsNone(actual.fast)
        self.assertEqual('no-fast', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_fasts_ordinary_fri(self):
        actual = self.repo.fasts.for_date(datetime(2024, 1, 26))

        self.assertIsNotNone(actual.fast)
        self.assertEqual('oil', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_fasts_ordinary_sun(self):
        actual = self.repo.fasts.for_date(datetime(2024, 1, 28))

        self.assertIsNone(actual.fast)
        self.assertEqual('no-fast', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_lent_period_before(self):
        fast = self.repo.fasts.by_id('fast:lent')

        actual = fast.matches_date(datetime(2024, 3, 7))

        self.assertFalse(actual)

    def test_lent_period_start(self):
        fast = self.repo.fasts.by_id('fast:lent')

        actual = fast.matches_date(datetime(2024, 3, 18))

        self.assertTrue(actual)

    def test_lent_period_inside(self):
        fast = self.repo.fasts.by_id('fast:lent')

        actual = fast.matches_date(datetime(2024, 4, 1))

        self.assertTrue(actual)

    def test_lent_period_end(self):
        fast = self.repo.fasts.by_id('fast:lent')

        actual = fast.matches_date(datetime(2024, 5, 4))

        self.assertTrue(actual)

    def test_lent_special_1(self):
        repo2023 = FastsRepository(2023, self.FASTS_DATA_PATH)
        actual = repo2023.fasts.for_date(datetime(2023, 4, 8))

        print(datetime(2023, 4, 8) - datetime(2023, 2, 27))
        self.assertEqual('roe', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_lent_special_2(self):
        repo2023 = FastsRepository(2023, self.FASTS_DATA_PATH)
        actual = repo2023.fasts.for_date(datetime(2023, 4, 9))

        print(datetime(2023, 4, 9) - datetime(2023, 2, 27))
        self.assertEqual('fish', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_lent_start_mon(self):
        actual = self.repo.fasts.for_date(datetime(2024, 3, 18))

        self.assertEqual('fast:lent', actual.fast.id)
        self.assertEqual('no-food', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_lent_mon_w2(self):
        actual = self.repo.fasts.for_date(datetime(2024, 3, 25))

        self.assertEqual('fast:lent', actual.fast.id)
        self.assertEqual('dry', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_lent_tue_w2(self):
        actual = self.repo.fasts.for_date(datetime(2024, 3, 26))

        self.assertEqual('fast:lent', actual.fast.id)
        self.assertEqual('dry', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_lent_wed_w2(self):
        actual = self.repo.fasts.for_date(datetime(2024, 3, 27))

        self.assertEqual('fast:lent', actual.fast.id)
        self.assertEqual('dry', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_lent_thu_w2(self):
        actual = self.repo.fasts.for_date(datetime(2024, 3, 28))

        self.assertEqual('fast:lent', actual.fast.id)
        self.assertEqual('oil', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_lent_fri_w2(self):
        actual = self.repo.fasts.for_date(datetime(2024, 3, 29))

        self.assertEqual('fast:lent', actual.fast.id)
        self.assertEqual('dry', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_lent_sat_w2(self):
        actual = self.repo.fasts.for_date(datetime(2024, 3, 30))

        self.assertEqual('fast:lent', actual.fast.id)
        self.assertEqual('oil', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_lent_sun_w2(self):
        actual = self.repo.fasts.for_date(datetime(2024, 3, 31))

        self.assertEqual('fast:lent', actual.fast.id)
        self.assertEqual('oil', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_easter_sun(self):
        actual = self.repo.fasts.for_date(datetime(2024, 5, 5))

        self.assertEqual('fast:easter', actual.fast.id)
        self.assertEqual('no-fast', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_apostles_before(self):
        fast = self.repo.fasts.by_id('fast:apostles')

        # TODO: Check start date
        actual = fast.matches_date(datetime(2024, 6, 29))

        self.assertFalse(actual)

    def test_apostles_start(self):
        fast = self.repo.fasts.by_id('fast:apostles')

        actual = fast.matches_date(datetime(2024, 7, 1))

        self.assertTrue(actual)

    def test_apostles_end(self):
        fast = self.repo.fasts.by_id('fast:apostles')

        actual = fast.matches_date(datetime(2024, 7, 11))

        self.assertTrue(actual)

    def test_apostles_after(self):
        fast = self.repo.fasts.by_id('fast:apostles')

        actual = fast.matches_date(datetime(2024, 7, 12))

        self.assertFalse(actual)

    def test_christmas_before(self):
        fast = self.repo.fasts.by_id('fast:christmas')

        actual = fast.matches_date(julian_to_gregorian(datetime(2024, 11, 14)))

        self.assertFalse(actual)

    def test_christmas_start(self):
        fast = self.repo.fasts.by_id('fast:christmas')

        actual = fast.matches_date(julian_to_gregorian(datetime(2024, 11, 15)))

        self.assertTrue(actual)

    def test_christmas_end(self):
        fast = self.repo.fasts.by_id('fast:christmas')

        actual = fast.matches_date(julian_to_gregorian(datetime(2024, 12, 24)))

        self.assertTrue(actual)

    def test_christmas_after(self):
        fast = self.repo.fasts.by_id('fast:christmas')

        actual = fast.matches_date(julian_to_gregorian(datetime(2024, 12, 25)))

        self.assertFalse(actual)

    def test_christmas_s1_mon(self):
        actual = self.repo.fasts.for_date(julian_to_gregorian(datetime(2024, 11, 15)))

        self.assertEqual('fast:christmas', actual.fast.id)
        self.assertEqual('fish', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_christmas_s2_mon(self):
        actual = self.repo.fasts.for_date(julian_to_gregorian(datetime(2024, 12, 10)))

        self.assertEqual('fast:christmas', actual.fast.id)
        self.assertEqual('oil', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_christmas_s3_mon(self):
        actual = self.repo.fasts.for_date(julian_to_gregorian(datetime(2024, 12, 20)))

        self.assertEqual('fast:christmas', actual.fast.id)
        self.assertEqual('no-oil', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_special_day_baptism(self):
        actual = self.repo.fasts.for_date(julian_to_gregorian(datetime(2024, 1, 5)))

        self.assertEqual('fast:baptism', actual.fast.id)
        self.assertEqual('oil', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_special_day_hdays(self):
        actual = self.repo.fasts.for_date(julian_to_gregorian(datetime(2024, 1, 4)))

        self.assertEqual('fast:hdays', actual.fast.id)
        self.assertEqual('no-fast', actual.fast_type.id)
        self.assertIsNotNone(actual.fast_type.title)

    def test_special_week_pharisees_period(self):
        repo2023 = FastsRepository(2023, self.FASTS_DATA_PATH)
        actual = repo2023.fasts.by_id('fast:pharisees')

        self.assertEqual(datetime(2023, 2, 5), actual.start)
        self.assertEqual(datetime(2023, 2, 11), actual.end)

    def test_special_week_cheese_period(self):
        repo2023 = FastsRepository(2023, self.FASTS_DATA_PATH)
        actual = repo2023.fasts.by_id('fast:cheese')

        self.assertEqual(datetime(2023, 2, 19), actual.start)
        self.assertEqual(datetime(2023, 2, 26), actual.end)

    def test_special_week_easter_period(self):
        repo2023 = FastsRepository(2023, self.FASTS_DATA_PATH)
        actual = repo2023.fasts.by_id('fast:easter_week')

        self.assertEqual(datetime(2023, 4, 17), actual.start)
        self.assertEqual(datetime(2023, 4, 22), actual.end)

    def test_special_week_trinity_period(self):
        repo2023 = FastsRepository(2023, self.FASTS_DATA_PATH)
        actual = repo2023.fasts.by_id('fast:trinity')

        self.assertEqual(datetime(2023, 6, 5), actual.start)
        self.assertEqual(datetime(2023, 6, 10), actual.end)


if __name__ == '__main__':
    unittest.main()
