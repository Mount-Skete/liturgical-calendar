import os
import xml.etree.ElementTree as ET
from calendar import monthrange

from .Feast import Feast
from .Feasts import Feasts
from .FeastsXmlSerializer import FeastsXmlSerializer


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
        typikon = self.read_feasts_typikon()
        book = self.read_feasts_ls()

        refs_list = {}
        for item in typikon:
            if item.content_ref:
                refs_list[item.content_ref] = item

        result = typikon
        for item in book:
            if item.id in refs_list.keys():
                self.merge(refs_list[item.id], item)
            else:
                result.append(item)

        return Feasts(result)

    def merge(self, feast_to: Feast, feast_from: Feast):
        feast_to.content_title = feast_from.content_title
        feast_to.content_ref = feast_from.content_ref
        feast_to.content_link = feast_from.content_link
        feast_to.content = feast_from.content
        feast_to.title = feast_from.title

        # TODO: Hymns

    def read_feasts_typikon(self) -> list[Feast]:
        result = []
        for idx in range(1, 13):
            result += self.__read_xml(
                os.path.join(self.TYPIKON_DATA_DIR, f'feasts_{idx:02}.xml'))

        result += self.__read_xml(
            os.path.join(self.TYPIKON_DATA_DIR, 'feasts_movable.xml'))

        return result

    def read_feasts_ls(self) -> Feasts:
        result = []

        for m_idx in range(1, 13):
            for d_idx in range(1, (monthrange(self.__year, m_idx)[1]) + 1):
                result += self.__read_xml(
                    os.path.join(self.LS_DATA_DIR, f'{m_idx:02}', f'{d_idx:02}.xml'))

        return Feasts(result)

    def __read_xml(self, path):
        root = ET.parse(path).getroot()
        feasts = FeastsXmlSerializer.read_all(root.findall('feast'), self.__year)

        return feasts
