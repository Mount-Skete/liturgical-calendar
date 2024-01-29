from dataclasses import dataclass
from datetime import datetime

import chevron

from data import Feast, Hymns, WeeklyHymn
from data.fasts import  FastData
from .TemplateBase import TemplateBase


@dataclass
class DayData:
    gregorian_date: datetime
    julian_date: datetime
    feasts: list[Feast]
    fast_data: FastData
    echo: int
    daily_hymn: WeeklyHymn

    @property
    def gregorian_date_formatted(self) -> str:
        return self.gregorian_date.strftime('%d %B (%A)')

    @property
    def julian_date_formatted(self) -> str:
        return self.julian_date.strftime('%d %B (%Y)')

    @property
    def date_link(self) -> str:
        return TemplateBase.get_date_link(self.gregorian_date)

    @property
    def page_break(self) -> str:
        return '<div style="page-break-before:always;"></div>'

    @property
    def hymns(self) -> list[Hymns]:
        daily = Hymns(self.daily_hymn.title, hymns=[self.daily_hymn])
        hymns = [daily]
        for feast in self.feasts:
            hymns.append(feast.hymns)

        return hymns


class Day(TemplateBase):

    def render(self, data: DayData):
        path = self.get_template_path('day')

        with open(path, 'r') as f:
            return chevron.render(f, data)
