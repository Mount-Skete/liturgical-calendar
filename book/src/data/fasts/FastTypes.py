from abc import abstractmethod
from collections import abc
from typing import overload, Iterable, MutableSequence

from .FastType import FastType


class FastTypes(abc.MutableSequence):
    items: list[FastType]

    def __init__(self, items: list[FastType]):
        self.items = items

    def by_id(self, id: str) -> FastType:
        for typ in self.items:
            if typ.id == id:
                return typ

        return None

    def insert(self, index, value):
        self.items.insert(index, value)

    @overload
    @abstractmethod
    def __getitem__(self, index: int) -> FastType:
        ...

    @overload
    @abstractmethod
    def __getitem__(self, index: slice) -> MutableSequence[FastType]:
        ...

    def __getitem__(self, index):
        return self.items[index]

    @overload
    @abstractmethod
    def __setitem__(self, index: int, value: FastType) -> None:
        ...

    @overload
    @abstractmethod
    def __setitem__(self, index: slice, value: Iterable[FastType]) -> None:
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
