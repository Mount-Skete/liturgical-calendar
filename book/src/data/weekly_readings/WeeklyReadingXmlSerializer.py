from xml.etree.ElementTree import Element

from data.utils.Weekday import Weekday
from .DailyReading import DailyReading
from .WeeklyReading import WeeklyReading
from .WeeklyReadingDate import WeeklyReadingDate, WeeklyReadingDateType
from .WeeklyReadings import WeeklyReadings


class WeeklyReadingXmlSerializer:

    @staticmethod
    def parse_all(xml: Element) -> WeeklyReadings:
        items = xml.findall('week')
        weeks = [WeeklyReadingXmlSerializer.parse(w) for w in items]

        return WeeklyReadings(weeks)

    @staticmethod
    def parse(xml: Element) -> WeeklyReading:
        title = None
        title_el = xml.find('title/ru')
        if title_el is not None:
            title = title_el.text

        date = WeeklyReadingXmlSerializer.parse_date(xml.find('date'))
        days = [WeeklyReadingXmlSerializer.parse_day(d) for d in xml.findall('day')]

        return WeeklyReading(date=date, days=days, title=title)

    @staticmethod
    def parse_date(xml: Element) -> WeeklyReadingDate:
        date_type = None
        week = 0

        if xml.find('easter') is not None:
            date_type = WeeklyReadingDateType.Easter
            week = int(xml.find('easter').get('week', 0))

        if xml.find('pentecost') is not None:
            date_type = WeeklyReadingDateType.Pentecost
            week = int(xml.find('pentecost').get('week', 0))

        if xml.find('lent') is not None:
            date_type = WeeklyReadingDateType.Lent
            week = int(xml.find('lent').get('week', 0))

        return WeeklyReadingDate(date_type=date_type, week=week)

    @staticmethod
    def parse_day(xml: Element):
        weekday = Weekday.from_value(xml.get('weekday'))

        orthros = WeeklyReadingXmlSerializer.parse_readings(xml.find('orthros'))
        liturgy = WeeklyReadingXmlSerializer.parse_readings(xml.find('liturgy'))
        vespers = WeeklyReadingXmlSerializer.parse_readings(xml.find('vespers'))
        readings = [WeeklyReadingXmlSerializer.parse_reading(r) for r in xml.findall('reading')]

        return DailyReading(weekday=weekday,
                            orthros=orthros,
                            liturgy=liturgy,
                            vespers=vespers,
                            readings=readings)

    @staticmethod
    def parse_readings(xml: Element):
        if xml is not None:
            readings = xml.findall('reading')
            return [WeeklyReadingXmlSerializer.parse_reading(r) for r in readings]

        return None

    @staticmethod
    def parse_reading(xml: Element):
        if xml is not None:
            return xml.text

        return None
