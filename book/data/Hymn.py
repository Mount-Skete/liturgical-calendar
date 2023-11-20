from typing import Optional
from xml.etree.ElementTree import Element
from dataclasses import dataclass
from book.utils import StringUtils
from enum import Enum


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

    # @staticmethod
    # def from_xml(item: Element):
    #     # TODO: verify tag name
    #
    #     type = item.attrib.get('type')
    #     h_type = HymnType.Troparion
    #     if type and type == 'kontakion':
    #         h_type = HymnType.Kontakion
    #
    #     return Hymn(title=StringUtils.clean(item.find('title').text),
    #                 content=StringUtils.clean(item.find('content').text),
    #                 echo=int(item.attrib['echo']),
    #                 week_day=int(item.attrib['week_day']) if item.get('week_day') else 0,
    #                 type=h_type)


@dataclass
class HymnSet:
    hymns: list[Hymn]
    title: str

    # @property
    # def title(self) -> str:
    #     if len(self.hymns) > 0:
    #         return self.hymns[0].title
    #
    #     return ''
