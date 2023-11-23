from enum import Enum
from datetime import datetime, timedelta
from dataclasses import dataclass

from .Hymn import Hymn
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
