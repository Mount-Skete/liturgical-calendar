from abc import abstractmethod
from collections import abc
from dataclasses import dataclass
from datetime import datetime
from typing import overload, Iterable, MutableSequence

from .Fast import Fast
from .FastType import FastType
from .FastTypes import FastTypes


@dataclass
class FastData:
    fast: Fast
    fast_type: FastType

    @property
    def format_display(self):
        if self.fast is not None and self.fast.title is not None:
            return f'{self.fast.title}: {self.fast_type.title}'

        return f'{self.fast_type.title}'


class Fasts(abc.MutableSequence):
    items: list[Fast]
    fast_types: FastTypes

    def __init__(self, fasts: list[Fast], fast_types: FastTypes):
        self.items = fasts
        self.fast_types = fast_types

    def by_id(self, id: str):
        for fast in self.items:
            if fast.id == id:
                return fast

        return None

    def for_date(self, gregorian: datetime) -> FastData:
        fasts = sorted(self.items, reverse=True)

        for fast in fasts:
            if fast.matches_date(gregorian):
                fast_type = fast.get_fast_for_date(gregorian)

                if fast_type is not None:
                    return FastData(fast=fast, fast_type=fast_type)

        return FastData(fast=None, fast_type=self.fast_types[0])

    def insert(self, index, value):
        self.items.insert(index, value)

    @overload
    @abstractmethod
    def __getitem__(self, index: int) -> Fast:
        ...

    @overload
    @abstractmethod
    def __getitem__(self, index: slice) -> MutableSequence[Fast]:
        ...

    def __getitem__(self, index):
        return self.items[index]

    @overload
    @abstractmethod
    def __setitem__(self, index: int, value: Fast) -> None:
        ...

    @overload
    @abstractmethod
    def __setitem__(self, index: slice, value: Iterable[Fast]) -> None:
        ...

    def __setitem__(self, index, value):
        self.items[index] = value

    @overload
    @abstractmethod
    def __delitem__(self, index: int) -> None:
        ...

    @overload
    @abstractmethod
    def __delitem__(self, index: slice) -> None:
        ...

    def __delitem__(self, index):
        del self.items[index]

    def __len__(self):
        return len(self.items)
