import chevron
from datetime import datetime
from dataclasses import dataclass
from .TemplateBase import TemplateBase
from book.data import Hymn, HymnSet, Event


@dataclass
class DayData:
    gregorian_date: datetime
    julian_date: datetime
    hymns: list[HymnSet]
    events: list[Event]
    echo: int

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
    def special_event(self) -> Event:
        return next(filter(lambda x: x.is_special, self.events), None)


class Day(TemplateBase):

    def render(self, data: DayData):
        path = self.get_template_path('day')

        with open(path, 'r') as f:
            return chevron.render(f, data)
