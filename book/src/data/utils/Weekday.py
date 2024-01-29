from enum import Enum
from datetime import datetime


class Weekday(Enum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6

    @staticmethod
    def from_value(val: str):
        if val is None:
            return None

        return Weekday[val.upper()]

    def matches_date(self, date: datetime):
        return self.value == date.weekday()
