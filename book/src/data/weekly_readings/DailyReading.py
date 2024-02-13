from dataclasses import dataclass
from typing import List

from data.utils import Weekday


@dataclass
class DailyReading:
    weekday: Weekday

    liturgy: List[str] = None
    vespers: List[str] = None
    orthros: List[str] = None

    readings: List[str] = None

    @property
    def all_readings(self):
        result = []

        if self.orthros is not None:
            result += self.orthros

        if self.liturgy is not None:
            result += self.liturgy

        if self.vespers is not None:
            result += self.vespers

        if self.readings is not None:
            result += self.readings

        return result
