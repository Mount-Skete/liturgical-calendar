from dataclasses import dataclass

from .DailyReading import DailyReading
from .WeeklyReading import WeeklyReading


@dataclass
class DailyReadingData:
    week: WeeklyReading
    day: DailyReading

    @property
    def format_display(self):
        if self.day is None:
            return ''

        # Temp
        if self.day.all_readings[0] is None and self.week.title is not None:
            return self.week.title

        readings = ' '.join(self.day.all_readings)

        if self.week.title is not None:
            return f'##### {self.week.title}\n{readings}'

        return readings
