from dataclasses import dataclass
from book.data import HymnSet


@dataclass
class Event:
    id: str
    header: str
    hymns: HymnSet

    content: list[str]
    is_special: bool = False


