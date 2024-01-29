from dataclasses import dataclass
from datetime import datetime

import chevron

from .CalendarUtils import CalendarUtils
from .Day import DayData, Day
from .TemplateBase import TemplateBase


@dataclass
class MonthData:
    gregorian_date: datetime
    daysData: list[DayData]

    @property
    def gregorian_month_formatted(self) -> str:
        return CalendarUtils.MONTH_NAMES_RU[self.gregorian_date.month - 1]


class Month(TemplateBase):

    def render(self, data: MonthData):
        path = self.get_template_path('month')
        data.days = [Day().render(day) for day in data.daysData]

        with open(path, 'r') as f:
            return chevron.render(f, data)

    def to_file(self, data: MonthData):
        text = self.render(data)

        path = self.get_md_month_output_path(data.gregorian_date)
        with open(path, 'w') as f:
            f.write(text)
