from dataclasses import dataclass
from datetime import datetime

from .FastSchedule import FastSchedule


@dataclass
class Fast:
    order: int
    schedules: list[FastSchedule]

    id: str = None
    title: str = None
    start: datetime = None
    end: datetime = None

    def __lt__(self, other):
        return self.order < other.order

    def matches_date(self, gregorian: datetime):
        if self.start is not None and self.end is not None:
            return self.start <= gregorian <= self.end

        return self.start is None and self.end is None

    def get_fast_for_date(self, gregorian: datetime):
        schedules = sorted(self.schedules, reverse=True)

        day_index = None
        if self.start is not None:
            day_index = (gregorian - self.start).days

        for schedule in schedules:
            fast_type = schedule.get_type_for_date(gregorian, day_index=day_index)
            if fast_type is not None:
                return fast_type

        return None
