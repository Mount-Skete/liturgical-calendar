from dataclasses import dataclass
from datetime import datetime

from .FastDay import FastDay


@dataclass
class FastSchedule:
    days: list[FastDay]

    order: int = 0
    start: datetime = None
    end: datetime = None

    def __lt__(self, other):
        return self.order < other.order

    def get_type_for_date(self, gregorian: datetime, day_index: int = None):
        if self.start is None or self.start <= gregorian <= self.end:
            for day in self.days:
                if day.number is not None and day.number == day_index:
                    return day.fast_type

                if day.weekday is not None and day.weekday.matches_date(gregorian):
                    return day.fast_type

        return None
