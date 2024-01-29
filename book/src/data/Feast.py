from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

# from views.markdown import TemplateBase
from .Hymns import Hymns


class FeastType(Enum):
    GREAT = "great"
    MIDDLE = "middle"
    SMALL = "low"

    @staticmethod
    def from_str(label: str):
        for e in FeastType:
            if label == e.value:
                return e

        return None


# https://azbyka.ru/days/p-znaki-prazdnikov
# https://www.oca.org/liturgics/outlines/classes-of-feasts
class FeastRank(Enum):
    VIGIL = "vigil"
    POLYELEOS = "polyeleos"
    GREAT_DOXOLOGY = "great_doxology"
    SIX_STICHERA = "six_stichera"
    ORDINARY = "ordinary"

    @staticmethod
    def from_str(label: str):
        for e in FeastRank:
            if label == e.value:
                return e

        return None


@dataclass
class Feast:
    title: str

    julian: datetime
    gregorian: datetime

    type: FeastType
    rank: FeastRank

    hymns: Hymns

    id: str | None = None
    content: list[str] = field(default_factory=list)
    content_title: str = ''
    content_link: str | None = None
    content_ref: str | None = None

    @property
    def gregorian_date_formatted(self) -> str:
        return self.gregorian.strftime('%d %B (%A)')

    @property
    def date_link(self) -> str:
        return Feast.get_date_link(self.gregorian)

    @staticmethod
    def get_date_link(date: datetime):
        return date.strftime('date-%Y-%m-%d')
