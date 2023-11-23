from xml.etree.ElementTree import Element

from utils import StringUtils
from .Hymn import Hymn, HymnType


class HymnsXmlSerializer:

    @staticmethod
    def read_all(hymns: list[Element]):
        result = []

        if not hymns or len(hymns) == 0:
            return result

        result = [HymnsXmlSerializer.read_one(xml) for xml in hymns]
        return result

    @staticmethod
    def read_one(xml: Element):
        hymn_type = HymnType.Troparion if xml.get('type') == 'troparion' else HymnType.Kontakion

        hymn = Hymn(
            title=StringUtils.clean(xml.find('title/ru').text),
            content=StringUtils.clean(xml.find('content/ru').text),
            echo=xml.get('echo', 0),
            type=hymn_type
        )

        return hymn
