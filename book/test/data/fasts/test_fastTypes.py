import os
import unittest
import xml.etree.ElementTree as ET

from data.fasts import FastTypesXmlSerializer, FastTypes


class FastTypesTestCase(unittest.TestCase):
    FAST_TYPES_DATA_PATH = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        'res',
        'fast_types.xml'
    )

    items: FastTypes

    def setUp(self):
        root = ET.parse(self.FAST_TYPES_DATA_PATH).getroot()
        self.items = FastTypesXmlSerializer.parse_all(root)

    def test_by_id_existing(self):
        actual = self.items.by_id('type-2')

        self.assertEqual('type-2', actual.id)
        self.assertEqual('Type 2', actual.title)


if __name__ == '__main__':
    unittest.main()
