import os
import unittest
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

from data.fasts import FastTypesXmlSerializer


class FastTypesXmlSerializerTestCase(unittest.TestCase):
    FAST_TYPES_DATA_PATH = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        'res',
        'fast_types.xml'
    )

    root: Element

    def setUp(self):
        self.root = ET.parse(self.FAST_TYPES_DATA_PATH).getroot()

    def test_parse_valid(self):
        actual = FastTypesXmlSerializer.parse_all(self.root)

        self.assertEqual(2, len(actual))
        self.assertEqual('type-1', actual[0].id)
        self.assertEqual('Type 1', actual[0].title)
        self.assertEqual('type-2', actual[1].id)
        self.assertEqual('Type 2', actual[1].title)


if __name__ == '__main__':
    unittest.main()
