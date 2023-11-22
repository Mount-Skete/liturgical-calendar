from abc import abstractmethod
from collections import abc
from typing import overload, Iterable, MutableSequence

from .Hymn import Hymn


class Hymns(abc.MutableSequence):
    hymns: list[Hymn]
    title: str

    def __init__(self, title='', hymns=None):
        if hymns is None:
            hymns = []

        self.hymns = hymns
        self.title = title

    def insert(self, index, value):
        self.hymns.insert(index, value)

    @overload
    @abstractmethod
    def __getitem__(self, index: int) -> Hymn: ...

    @overload
    @abstractmethod
    def __getitem__(self, index: slice) -> MutableSequence[Hymn]: ...

    def __getitem__(self, index):
        return self.hymns[index]

    @overload
    @abstractmethod
    def __setitem__(self, index: int, value: Hymn) -> None: ...

    @overload
    @abstractmethod
    def __setitem__(self, index: slice, value: Iterable[Hymn]) -> None: ...

    def __setitem__(self, index, value):
        self.hymns[index] = value

    @overload
    @abstractmethod
    def __delitem__(self, index: int) -> None: ...

    @overload
    @abstractmethod
    def __delitem__(self, index: slice) -> None: ...

    def __delitem__(self, index):
        del self.hymns[index]

    def __len__(self):
        return len(self.hymns)
