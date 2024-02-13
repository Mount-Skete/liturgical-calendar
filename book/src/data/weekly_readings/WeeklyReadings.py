from abc import abstractmethod
from collections import abc
from datetime import datetime
from typing import overload, Iterable, MutableSequence

from data.utils import Weekday
from julian_calendar import calculate_orthodox_easter_gregorian, weeks_between
from .DailyReadingData import DailyReadingData
from .WeeklyReading import WeeklyReading
from .WeeklyReadingDate import WeeklyReadingDateType, WeeklyReadingDate


class WeeklyReadings(abc.MutableSequence):
    items: list[WeeklyReading]

    def __init__(self, readings: list[WeeklyReading]):
        self.items = readings

    def find_by_week_date(self, week_date: WeeklyReadingDate):
        for item in self.items:
            if item.date.date_type == week_date.date_type and item.date.week == week_date.week:
                return item

        return None

    def for_date(self, gregorian: datetime) -> DailyReadingData:
        easter_date = calculate_orthodox_easter_gregorian(gregorian.year)
        if easter_date > gregorian:
            easter_date = calculate_orthodox_easter_gregorian(gregorian.year - 1)

        weeks = weeks_between(easter_date, gregorian)

        weekly_reading = None
        if 0 <= weeks < 8:
            weekly_reading = self.find_by_week_date(
                WeeklyReadingDate(date_type=WeeklyReadingDateType.Easter,
                                  week=weeks + 1))
        else:
            weekly_reading = self.find_by_week_date(
                WeeklyReadingDate(date_type=WeeklyReadingDateType.Pentecost,
                                  week=weeks - 8 + 1))

        if weekly_reading is not None:
            daily_reading = None
            weekday = Weekday.from_index(gregorian.weekday())
            for day in weekly_reading.days:
                if day.weekday == weekday:
                    daily_reading = day

            return DailyReadingData(week=weekly_reading, day=daily_reading)

        return None

    def insert(self, index, value):
        self.items.insert(index, value)

    @overload
    @abstractmethod
    def __getitem__(self, index: int) -> WeeklyReading:
        ...

    @overload
    @abstractmethod
    def __getitem__(self, index: slice) -> MutableSequence[WeeklyReading]:
        ...

    def __getitem__(self, index):
        return self.items[index]

    @overload
    @abstractmethod
    def __setitem__(self, index: int, value: WeeklyReading) -> None:
        ...

    @overload
    @abstractmethod
    def __setitem__(self, index: slice, value: Iterable[WeeklyReading]) -> None:
        ...

    def __setitem__(self, index, value):
        self.items[index] = value

    @overload
    @abstractmethod
    def __delitem__(self, index: int) -> None:
        ...

    @overload
    @abstractmethod
    def __delitem__(self, index: slice) -> None:
        ...

    def __delitem__(self, index):
        del self.items[index]

    def __len__(self):
        return len(self.items)
