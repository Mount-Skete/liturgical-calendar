import unittest
from datetime import datetime

from data.fasts import Fast


class FastTestCase(unittest.TestCase):

    def test_order_sort(self):
        items = [
            Fast(order=1, schedules=[]),
            Fast(order=0, schedules=[]),
            Fast(order=2, schedules=[])
        ]

        actual = sorted(items)

        self.assertEqual(0, actual[0].order)
        self.assertEqual(1, actual[1].order)
        self.assertEqual(2, actual[2].order)

    def test_period_matches_date_inside(self):
        fast = Fast(order=1,
                    schedules=[],
                    start=datetime(2024, 1, 10),
                    end=datetime(2024, 1, 17))

        actual = fast.matches_date(datetime(2024, 1, 12))

        self.assertTrue(actual)

    def test_period_matches_date_start(self):
        fast = Fast(order=1,
                    schedules=[],
                    start=datetime(2024, 1, 10),
                    end=datetime(2024, 1, 17))

        actual = fast.matches_date(datetime(2024, 1, 10))

        self.assertTrue(actual)

    def test_period_matches_date_end(self):
        fast = Fast(order=1,
                    schedules=[],
                    start=datetime(2024, 1, 10),
                    end=datetime(2024, 1, 17))

        actual = fast.matches_date(datetime(2024, 1, 17))

        self.assertTrue(actual)

    def test_period_does_not_match_outside(self):
        fast = Fast(order=1,
                    schedules=[],
                    start=datetime(2024, 1, 10),
                    end=datetime(2024, 1, 17))

        actual = fast.matches_date(datetime(2024, 1, 9))

        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
