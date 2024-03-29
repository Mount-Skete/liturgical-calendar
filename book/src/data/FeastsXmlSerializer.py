from calendar import monthrange
from datetime import datetime, timedelta
from xml.etree.ElementTree import Element

from julian_calendar import (julian_to_gregorian,
                             calculate_orthodox_easter_julian)
from utils.StringUtils import StringUtils
from .Feast import Feast, FeastType, FeastRank
from .Hymns import Hymns
from .HymnsXmlSerializer import HymnsXmlSerializer


class FeastsXmlSerializer:

    @staticmethod
    def read_all(feasts: list[Element], year: int):
        result = []
        for xml in feasts:
            item = FeastsXmlSerializer.read_one(xml, year)
            if item:
                result.append(item)

        return result

    @staticmethod
    def read_one(xml: Element, year: int):
        id = xml.get('id', '')
        title = StringUtils.clean_all(xml.find('title/ru').text)
        julian = FeastsXmlSerializer.__parse_date_xml(xml, year)

        if not julian:
            # Skipping non-leap year
            return None

        gregorian = julian_to_gregorian(julian)
        feast_type = FeastType.from_str(xml.get('type'))
        feast_rank = FeastRank.from_str(xml.get('rank'))

        hymns = HymnsXmlSerializer.read_all(xml.findall('hymns/hymn'))

        hset = Hymns(title, hymns)

        content_title = ''
        content = []
        content_link = None
        if xml.find('content') is not None:
            content_link = xml.get('id')
            if xml.find('content/title/ru') is not None:
                content_title = StringUtils.clean_all(xml.find('content/title/ru').text)

            for text_el in xml.findall('content/text/ru/p'):
                content.append(text_el.text)

        content_ref = None
        if xml.find('refs') is not None:
            ref_el = xml.find('refs/ref')
            content_ref = ref_el.get('id')

        feast = Feast(
            id=id,
            title=title,
            julian=julian,
            gregorian=gregorian,
            type=feast_type,
            rank=feast_rank,
            hymns=hset,
            content_title=content_title,
            content=content,
            content_link=content_link,
            content_ref=content_ref
        )

        return feast

    @staticmethod
    def __parse_date_xml(xml, year: int) -> datetime:
        if xml.find('date/julian') is not None:
            date = xml.find('date/julian').text
            return FeastsXmlSerializer.__parse_date(year, date)
        elif xml.find('date/easter') is not None:
            easter = calculate_orthodox_easter_julian(year)
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
