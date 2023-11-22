import os
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from calendar import monthrange

from julian_calendar import (julian_to_gregorian,
                             calculate_orthodox_easter_julian)

from .Feast import Feast, FeastType, FeastRank
from .Feasts import Feasts
from .Hymn import Hymn, HymnType
from .Hymns import Hymns
from utils import StringUtils


class FeastsRepository:
    DEFAULT_DATA_DIR = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        '..',
        'data',
        'typikon-feasts'
    )

    __year: int

    def __init__(self, year: int):
        self.__year = year
        pass

    def read(self) -> Feasts:
        result = []
        for idx in range(1, 13):
            result += self.__read_xml(f'feasts_{idx:02}.xml')

        result += self.__read_xml('feasts_movable.xml')

        return Feasts(result)

    def __parse_date_xml(self, xml) -> datetime:
        if xml.find('date/julian') is not None:
            date = xml.find('date/julian').text
            return FeastsRepository.__parse_date(self.__year, date)
        elif xml.find('date/easter') is not None:
            easter = calculate_orthodox_easter_julian(self.__year)
            days = int(xml.find('date/easter').get('days', 0))
            return easter + timedelta(days=days)
        else:
            raise NotImplementedError('Date format not supported')

    @staticmethod
    def __parse_date(year, date):
        parts = date.split('-')
        month = int(parts[0])
        day = int(parts[1])

        month_days = monthrange(year, month)[1]
        if day > month_days:
            # Skipping non-leap year
            return None

        return datetime(year, month, day)

    def __read_hymns_xml(self, xml_hymns):
        if not xml_hymns or len(xml_hymns) == 0:
            return []

        result = []
        for xml in xml_hymns:
            htype = HymnType.Troparion if xml.get('type') == 'troparion' else HymnType.Kontakion
            result.append(Hymn(
                title=StringUtils.clean(xml.find('title/ru').text),
                content=StringUtils.clean(xml.find('content/ru').text),
                echo=xml.get('echo', 0),
                type=htype
            ))

        return result

    def __read_xml(self, filename):
        path = os.path.join(self.DEFAULT_DATA_DIR, filename)

        tree = ET.parse(path)
        root = tree.getroot()

        feasts = []
        feasts_xml = root.findall('feast')
        for xml in feasts_xml:
            title = xml.find('title/ru').text
            julian = self.__parse_date_xml(xml)

            if not julian:
                # Skipping non-leap year
                continue

            gregorian = julian_to_gregorian(julian)
            feast_type = FeastType.from_str(xml.get('type'))
            feast_rank = FeastRank.from_str(xml.get('rank'))

            hymns = self.__read_hymns_xml(xml.findall('hymns/hymn'))

            hset = Hymns(title, hymns)

            feast = Feast(
                title=title,
                julian=julian,
                gregorian=gregorian,
                type=feast_type,
                rank=feast_rank,
                hymns=hset
            )
            feasts.append(feast)

        return feasts
