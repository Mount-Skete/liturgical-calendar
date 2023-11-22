from abc import abstractmethod
from collections import abc
from datetime import datetime
from typing import overload, Iterable, MutableSequence

from .Feast import Feast


class Feasts(abc.MutableSequence):
    feasts: list[Feast]

    def __init__(self, feasts=None):
        if feasts is None:
            feasts = []

        self.feasts = feasts

    def for_date(self, gregorian: datetime):
        result = []
        for item in self.feasts:
            if item.gregorian.month == gregorian.month and item.gregorian.day == gregorian.day:
                result.append(item)

        return result

    def insert(self, index, value):
        self.feasts.insert(index, value)

    @overload
    @abstractmethod
    def __getitem__(self, index: int) -> Feast:
        ...

    @overload
    @abstractmethod
    def __getitem__(self, index: slice) -> MutableSequence[Feast]:
        ...

    def __getitem__(self, index):
        return self.feasts[index]

    @overload
    @abstractmethod
    def __setitem__(self, index: int, value: Feast) -> None:
        ...

    @overload
    @abstractmethod
    def __setitem__(self, index: slice, value: Iterable[Feast]) -> None:
        ...

    def __setitem__(self, index, value):
        self.feasts[index] = value

    @overload
    @abstractmethod
    def __delitem__(self, index: int) -> None:
        ...

    @overload
    @abstractmethod
    def __delitem__(self, index: slice) -> None:
        ...

    def __delitem__(self, index):
        del self.feasts[index]

    def __len__(self):
        return len(self.feasts)
