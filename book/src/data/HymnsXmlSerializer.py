from xml.etree.ElementTree import Element

from utils import StringUtils
from .Hymn import Hymn, HymnType, WeeklyHymn


class HymnsXmlSerializer:

    @staticmethod
    def read_all(hymns: list[Element]) -> list[Hymn]:
        result = []

        if not hymns or len(hymns) == 0:
            return result

        result = [HymnsXmlSerializer.read_one(xml) for xml in hymns]

        return result

    @staticmethod
    def read_one(xml: Element) -> Hymn:
        hymn_type = HymnType.Troparion if xml.get('type') == 'troparion' else HymnType.Kontakion

        hymn = Hymn(
            title=StringUtils.clean_all(xml.find('title/ru').text),
            content=StringUtils.clean(xml.find('content/ru').text),
            echo=xml.get('echo', 0),
            type=hymn_type
        )

        return hymn

    @staticmethod
    def read_all_weekly(hymns: list[Element]) -> list[WeeklyHymn]:
        result = []

        if not hymns or len(hymns) == 0:
            return result

        result = [HymnsXmlSerializer.read_one_weekly(xml) for xml in hymns]

        return result

    @staticmethod
    def read_one_weekly(xml: Element) -> WeeklyHymn:
        hymn_type = HymnType.Troparion if xml.get('type') == 'troparion' else HymnType.Kontakion

        hymn = WeeklyHymn(
            title=StringUtils.clean_all(xml.find('title/ru').text),
            content=StringUtils.clean(xml.find('content/ru').text),
            echo=int(xml.get('echo', 0)),
            type=hymn_type,
            weekday=int(xml.get('weekday', 0))
        )

        return hymn
