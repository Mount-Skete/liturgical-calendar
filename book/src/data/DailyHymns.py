import os
from datetime import datetime
from xml.etree import ElementTree

from .Hymn import WeeklyHymn
from .HymnsXmlSerializer import HymnsXmlSerializer


class DailyHymns:
    __hymns: list[WeeklyHymn]

    def __init__(self):
        self.__hymns = DailyHymns.parse()

    @staticmethod
    def get_data_path():
        return os.path.join(os.path.dirname(__file__), '..', '..', 'res', 'daily_hymns.xml')

    @staticmethod
    def parse():
        tree = ElementTree.parse(DailyHymns.get_data_path())
        items = tree.getroot().findall('hymn')
        hymns = HymnsXmlSerializer.read_all_weekly(items)

        return hymns

    def get_all(self):
        return self.__hymns

    def for_date(self, date: datetime, echo: int) -> WeeklyHymn:  # -> list[Hymn]:
        week_day = date.isoweekday()

        hymns = self.__hymns
        if date.isoweekday() == 7:
            return list(filter(lambda d: d.echo == echo and d.weekday == week_day, hymns))[0]
        else:
            return list(filter(lambda d: d.weekday == week_day, hymns))[0]
