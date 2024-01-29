import unittest
from datetime import datetime

from data.fasts import FastSchedule, FastDay, FastType
from data.utils import Weekday


class FastScheduleTestCase(unittest.TestCase):
    def test_order_sort(self):
        items = [
            FastSchedule(order=1, days=[]),
            FastSchedule(order=0, days=[]),
            FastSchedule(order=2, days=[])
        ]

        actual = sorted(items, reverse=True)

        self.assertEqual(2, actual[0].order)
        self.assertEqual(1, actual[1].order)
        self.assertEqual(0, actual[2].order)

    def test_get_type_for_date_weekday(self):
        schedule = FastSchedule(order=1, days=[
            FastDay(fast_type=FastType('t1', 'T1'), weekday=Weekday.WED)
        ])

        self.assertEqual('t1', schedule.get_type_for_date(datetime(2024, 1, 24)).id)
        self.assertIsNone(schedule.get_type_for_date(datetime(2024, 1, 25)))

    def test_get_type_for_date_number(self):
        schedule = FastSchedule(order=1, days=[
            FastDay(fast_type=FastType('t1', 'T1'), number=2)
        ])

        self.assertEqual('t1', schedule.get_type_for_date(datetime(2024, 1, 24), 2).id)
        self.assertIsNone(schedule.get_type_for_date(datetime(2024, 1, 25), 1))


if __name__ == '__main__':
    unittest.main()
