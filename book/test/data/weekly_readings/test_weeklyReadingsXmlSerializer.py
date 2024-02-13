import os
import unittest
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

from data.utils import Weekday
from data.weekly_readings import WeeklyReadingXmlSerializer, WeeklyReadingDate, WeeklyReadingDateType


class WeeklyReadingsXmlSerializerTestCase(unittest.TestCase):
    WEEKLY_READINGS_DATA_PATH = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        'res',
        'weekly_readings.xml'
    )

    root: Element

    def setUp(self):
        self.root = ET.parse(self.WEEKLY_READINGS_DATA_PATH).getroot()

    def test_parse_valid(self):
        actual = WeeklyReadingXmlSerializer.parse_all(self.root)

        self.assertEqual(3, len(actual))

        self.assertEqual('E1', actual[0].title)
        self.assertEqual(WeeklyReadingDateType.Easter, actual[0].date.date_type)
        self.assertEqual(1, actual[0].date.week)

        self.assertEqual(7, len(actual[0].days))

        # Sunday
        self.assertEqual(Weekday.SUN, actual[0].days[0].weekday)
        self.assertEqual(1, len(actual[0].days[0].orthros))
        self.assertEqual('SUN-O1', actual[0].days[0].orthros[0])
        self.assertEqual(2, len(actual[0].days[0].liturgy))
        self.assertEqual('SUN-L1', actual[0].days[0].liturgy[0])
        self.assertEqual('SUN-L2', actual[0].days[0].liturgy[1])
        self.assertIsNone(actual[0].days[0].vespers)
        self.assertEquals([], actual[0].days[0].readings)

        self.assertEqual(3, len(actual[0].days[0].all_readings))
        self.assertEqual('SUN-O1', actual[0].days[0].all_readings[0])
        self.assertEqual('SUN-L1', actual[0].days[0].all_readings[1])
        self.assertEqual('SUN-L2', actual[0].days[0].all_readings[2])

        # Monday
        self.assertEqual(Weekday.MON, actual[0].days[1].weekday)
        self.assertIsNone(actual[0].days[1].orthros)
        self.assertIsNone(actual[0].days[1].liturgy)
        self.assertIsNone(actual[0].days[1].vespers)

        self.assertEqual(2, len(actual[0].days[1].readings))
        self.assertEqual('MON-1', actual[0].days[1].readings[0])
        self.assertEqual('MON-2', actual[0].days[1].readings[1])

        self.assertEqual(2, len(actual[0].days[1].all_readings))
        self.assertEqual('MON-1', actual[0].days[1].all_readings[0])
        self.assertEqual('MON-2', actual[0].days[1].all_readings[1])

        self.assertIsNone(actual[1].title)
        self.assertEqual(WeeklyReadingDateType.Pentecost, actual[1].date.date_type)
        self.assertEqual(3, actual[1].date.week)
        self.assertEqual(7, len(actual[1].days))

        self.assertEqual('L1', actual[2].title)
        self.assertEqual(WeeklyReadingDateType.Lent, actual[2].date.date_type)
        self.assertEqual(1, actual[2].date.week)
        self.assertEqual(7, len(actual[2].days))

        # Monday
        self.assertEqual(Weekday.MON, actual[2].days[1].weekday)
        self.assertIsNone(actual[2].days[1].orthros)
        self.assertIsNone(actual[2].days[1].liturgy)
        self.assertEqual(1, len(actual[2].days[1].vespers))
        self.assertEqual('V-1', actual[2].days[1].vespers[0])

        self.assertEqual(2, len(actual[2].days[1].readings))
        self.assertEqual('MON-1', actual[2].days[1].readings[0])
        self.assertEqual('MON-2', actual[2].days[1].readings[1])

        self.assertEqual(3, len(actual[2].days[1].all_readings))
        self.assertEqual('V-1', actual[2].days[1].all_readings[0])
        self.assertEqual('MON-1', actual[2].days[1].all_readings[1])
        self.assertEqual('MON-2', actual[2].days[1].all_readings[2])


if __name__ == '__main__':
    unittest.main()
