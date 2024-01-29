import copy
from collections import namedtuple
from datetime import datetime
from xml.etree.ElementTree import Element

from data.utils import Weekday
from data.utils.DateXmlSerializer import DateXmlSerializer
from .Fast import Fast
from .FastDay import FastDay
from .FastSchedule import FastSchedule
from .FastTypes import FastTypes
from .Fasts import Fasts


class FastsXmlSerializer:
    Period = namedtuple('Period', ['start', 'end'])

    fast_types: FastTypes
    year: int

    def __init__(self, fast_types: FastTypes, year: int):
        self.fast_types = fast_types
        self.year = year

    def parse_all(self, xml: Element) -> Fasts:
        items = xml.findall('fast')
        fasts = [self.parse(e) for e in items]

        extra_fasts = []
        # Cross year fasts (e.g. Christmas)
        # TODO: Add tests
        for fast in fasts:
            if (fast.start is not None and fast.end is not None
                    and fast.start.year != fast.end.year):
                prev_fast = copy.deepcopy(fast)
                prev_fast.start = datetime(fast.start.year - 1, fast.start.month, fast.start.day)
                prev_fast.end = datetime(fast.end.year - 1, fast.end.month, fast.end.day)

                for sch in prev_fast.schedules:
                    if sch.start is not None and sch.end is not None:
                        sch.start = datetime(sch.start.year - 1, sch.start.month, sch.start.day)
                        sch.end = datetime(sch.end.year - 1, sch.end.month, sch.end.day)

                extra_fasts.append(prev_fast)

        fasts += extra_fasts

        return Fasts(fasts, self.fast_types)

    def parse(self, xml: Element) -> Fast:
        order = int(xml.get('order', 0))

        title = None
        title_el = xml.find('title/ru')
        if title_el is not None:
            title = title_el.text

        id = xml.get('id')

        period = self.__parse_period(xml)

        schedules = [self.parse_schedule(s) for s in xml.findall('schedule')]

        return Fast(order=order,
                    id=id,
                    title=title,
                    schedules=schedules,
                    start=period.start,
                    end=period.end)

    def parse_schedule(self, xml: Element):
        days = [self.parse_day(d) for d in xml.findall('day')]
        order = int(xml.get('order', 0))

        period = self.__parse_period(xml)

        schedule = FastSchedule(days=days, order=order, start=period.start, end=period.end)

        return schedule

    def parse_day(self, xml: Element):
        weekday = None
        weekday_el = xml.get('weekday', None)
        if weekday_el is not None:
            weekday = Weekday.from_value(weekday_el)

        number = None
        number_el = xml.get('number', None)
        if number_el is not None:
            number = int(number_el)

        fast_type_id = xml.get('fastType')
        fast_type = self.fast_types.by_id(fast_type_id)

        return FastDay(fast_type=fast_type,
                       weekday=weekday,
                       number=number)

    def __parse_period(self, xml: Element) -> Period:
        start = self.__parse_date(xml, 'start')
        end = self.__parse_date(xml, 'end')

        if start is not None and end is not None:
            if start > end:
                start = datetime(start.year - 1, start.month, start.day)

        return self.Period(start=start, end=end)

    def __parse_date(self, xml: Element, name: str):
        result = None
        el = xml.find(name)
        if el is not None:
            result = DateXmlSerializer.parse_to_gregorian(el, self.year)

        return result
