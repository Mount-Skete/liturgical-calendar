import os
import unittest
import xml.etree.ElementTree as ET
from datetime import datetime
from xml.etree.ElementTree import Element

from data.fasts import FastsXmlSerializer, FastTypesXmlSerializer, FastTypes
from data.utils import Weekday


class FastsXmlSerializerTestCase(unittest.TestCase):
    FASTS_DATA_PATH = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        'res',
        'fasts.xml'
    )

    root: Element
    types: FastTypes

    def setUp(self):
        self.root = ET.parse(self.FASTS_DATA_PATH).getroot()
        self.types = FastTypesXmlSerializer.parse_all(self.root)

    def test_parse_verify(self):
        items = FastsXmlSerializer(self.types, 2024).parse_all(self.root)
        self.assertEqual(2, len(items))

    def test_parse_verify_ordinary(self):
        items = FastsXmlSerializer(self.types, 2024).parse_all(self.root)
        actual = items[0]

        self.assertEqual(0, actual.order)
        self.assertIsNone(actual.title)
        self.assertIsNone(actual.id)
        self.assertIsNone(actual.start)
        self.assertIsNone(actual.end)

        self.assertEqual(2, len(actual.schedules))

        self.assertEqual(3, len(actual.schedules[0].days))
        self.assertEqual(0, actual.schedules[0].order)

        self.assertEqual(1, len(actual.schedules[1].days))
        self.assertEqual(1, actual.schedules[1].order)

        self.assertEqual(Weekday.WED, actual.schedules[0].days[0].weekday)
        self.assertEqual('type-1', actual.schedules[0].days[0].fast_type.id)

        self.assertEqual(Weekday.FRI, actual.schedules[0].days[1].weekday)
        self.assertEqual('type-2', actual.schedules[0].days[1].fast_type.id)

        self.assertEqual(Weekday.SAT, actual.schedules[0].days[2].weekday)
        self.assertEqual('type-2', actual.schedules[0].days[2].fast_type.id)

        self.assertEqual(Weekday.SAT, actual.schedules[1].days[0].weekday)
        self.assertEqual('type-3', actual.schedules[1].days[0].fast_type.id)

    def test_parse_verify_lent(self):
        items = FastsXmlSerializer(self.types, 2024).parse_all(self.root)
        actual = items[1]

        self.assertEqual(1, actual.order)
        self.assertEqual("Lent type", actual.title)
        self.assertEqual("id-1", actual.id)
        self.assertEqual(datetime(2024, 3, 18), actual.start)
        self.assertEqual(datetime(2024, 5, 5), actual.end)

        self.assertEqual(2, len(actual.schedules))

        self.assertEqual(1, len(actual.schedules[0].days))
        self.assertEqual(0, actual.schedules[0].order)

        self.assertEqual(2, len(actual.schedules[1].days))
        self.assertEqual(1, actual.schedules[1].order)

        self.assertEqual(Weekday.MON, actual.schedules[0].days[0].weekday)
        self.assertEqual('type-1', actual.schedules[0].days[0].fast_type.id)
        self.assertIsNone(actual.schedules[0].days[0].number)

        self.assertEqual(datetime(2024, 2, 15), actual.schedules[1].start)
        self.assertEqual(datetime(2024, 3, 16), actual.schedules[1].end)

        self.assertEqual(0, actual.schedules[1].days[0].number)
        self.assertEqual('type-2', actual.schedules[1].days[0].fast_type.id)
        self.assertIsNone(actual.schedules[1].days[1].weekday)

        self.assertEqual(10, actual.schedules[1].days[1].number)
        self.assertEqual('type-3', actual.schedules[1].days[1].fast_type.id)
        self.assertIsNone(actual.schedules[1].days[1].weekday)


if __name__ == '__main__':
    unittest.main()
