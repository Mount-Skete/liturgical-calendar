from xml.etree.ElementTree import Element

from .FastType import FastType
from .FastTypes import FastTypes


class FastTypesXmlSerializer:

    @staticmethod
    def parse_all(xml: Element) -> FastTypes:
        items = xml.findall('types/fastType')
        types = [FastTypesXmlSerializer.parse(e) for e in items]

        return FastTypes(types)

    @staticmethod
    def parse(xml: Element) -> FastType:
        id_attr = xml.get('id')
        title = None

        title_el = xml.find('title/ru')
        if title_el is not None:
            title = title_el.text

        return FastType(id_attr, title)
