from dataclasses import dataclass
from enum import Enum
from typing import Optional


class HymnType(Enum):
    Troparion = "Тропарь"
    Kontakion = "Кондак"


@dataclass
class Hymn:
    title: str
    content: str
    echo: Optional[int] = 0
    # week_day: Optional[int] = 0

    header: Optional[str] = ''
    type: Optional[HymnType] = HymnType.Troparion
