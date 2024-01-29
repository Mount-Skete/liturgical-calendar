from dataclasses import dataclass

from .Month import MonthData, Month
from .TemplateBase import TemplateBase


@dataclass
class YearData:
    year: int
    monthsData: list[MonthData]


class Year(TemplateBase):
    def render(self, data: YearData):
        months = [Month().render(mdata) for mdata in data.monthsData]
        return ''.join(months)

    def to_file(self, data: YearData):
        [Month().to_file(mdata) for mdata in data.monthsData]
