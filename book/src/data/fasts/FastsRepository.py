import os
import xml.etree.ElementTree as ET

from .FastTypes import FastTypes
from .FastTypesXmlSerializer import FastTypesXmlSerializer
from .Fasts import Fasts
from .FastsXmlSerializer import FastsXmlSerializer


class FastsRepository:
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

    types: FastTypes
    fasts: Fasts

    def __init__(self, year: int, path: str = FASTS_DATA_PATH):
        self.load_all(path, year)

    def load_all(self, path: str, year: int):
        root = ET.parse(path).getroot()

        self.types = FastTypesXmlSerializer.parse_all(root)
        self.fasts = FastsXmlSerializer(self.types, year).parse_all(root)
