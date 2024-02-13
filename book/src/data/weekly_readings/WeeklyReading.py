from dataclasses import dataclass
from typing import List

from .DailyReading import DailyReading
from .WeeklyReadingDate import WeeklyReadingDate


@dataclass
class WeeklyReading:
    date: WeeklyReadingDate
    days: List[DailyReading]

    title: str = None
