import os
import xml.etree.ElementTree as ET

from . import Feast, Feasts
from .FeastsXmlSerializer import FeastsXmlSerializer

from calendar import monthrange


class FeastsRepository:
    TYPIKON_DATA_DIR = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        '..',
        'data',
        'typikon-feasts-ru'
    )

    LS_DATA_DIR = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        '..',
        'data',
        'lives-of-the-saints-ru'
    )

    __year: int

    def __init__(self, year: int):
        self.__year = year

    def read_all(self) -> Feasts:
        result = self.read_feasts_typikon()

        # TODO: Merge
        result += self.read_feasts_ls()

        return Feasts(result)

    def read_feasts_typikon(self) -> list[Feast]:
        result = []
        for idx in range(1, 13):
            result += self.__read_xml(
                os.path.join(self.TYPIKON_DATA_DIR, f'feasts_{idx:02}.xml'))

        result += self.__read_xml(
            os.path.join(self.TYPIKON_DATA_DIR, 'feasts_movable.xml'))

        return result

    def read_feasts_ls(self) -> list[Feast]:
        result = []

        for m_idx in range(1, 13):
            for d_idx in range(1, (monthrange(self.__year, m_idx)[1]) + 1):
                result += self.__read_xml(
                    os.path.join(self.LS_DATA_DIR, f'{m_idx:02}', f'{d_idx:02}.xml'))

        return result

    def __read_xml(self, path):
        root = ET.parse(path).getroot()
        feasts = FeastsXmlSerializer.read_all(root.findall('feast'), self.__year)

        return feasts
