from dataclasses import dataclass
from enum import Enum


class WeeklyReadingDateType(Enum):
    Easter = 1
    Pentecost = 9
    Lent = -5


@dataclass
class WeeklyReadingDate:
    date_type: WeeklyReadingDateType
    week: int
