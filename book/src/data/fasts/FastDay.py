from dataclasses import dataclass

from data.utils import Weekday
from .FastType import FastType


@dataclass
class FastDay:
    fast_type: FastType

    weekday: Weekday = None
    number: int = None
