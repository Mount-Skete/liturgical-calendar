import unittest
import xml.etree.ElementTree as ET
from datetime import datetime

from data.utils import DateXmlSerializer
from julian_calendar import gregorian_to_julian


class DateXmlSerializerTestCase(unittest.TestCase):

    def test_parse_julian(self):
        xml = ET.XML('<date><julian>11-15</julian></date>')

        actual = DateXmlSerializer.parse(xml, 2024)

        self.assertEqual(datetime(2024, 11, 15), actual)

    def test_parse_easter(self):
        xml = ET.XML('<date><easter/></date>')

        actual = DateXmlSerializer.parse(xml, 2024)

        self.assertEqual(datetime(2024, 4, 22), actual)

    def test_parse_trinity(self):
        xml = ET.XML('<date><easter days="+49"/></date>')

        actual = DateXmlSerializer.parse(xml, 2024)

        self.assertEqual(datetime(2024, 6, 10), actual)

    def test_parse_negative(self):
        xml = ET.XML('<date><easter days="-2"/></date>')

        actual = DateXmlSerializer.parse(xml, 2024)

        self.assertEqual(datetime(2024, 4, 20), actual)

    def test_parse_with_shift(self):
        xml = ET.XML('<date><easter days="+49" shift="2:mon" /></date>')

        actual = DateXmlSerializer.parse(xml, 2024)

        # TODO: Check start date
        self.assertEqual(gregorian_to_julian(datetime(2024, 6, 30)), actual)
        self.assertEqual(0, actual.weekday())


if __name__ == '__main__':
    unittest.main()
