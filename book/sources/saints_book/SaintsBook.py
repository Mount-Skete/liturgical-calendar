import math
import re
import os
from julian_calendar import julian_to_gregorian, gregorian_to_julian
from calendar import monthrange
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from typing import Type, Optional
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
from bs4 import Tag
from book.data import Event, Hymn, HymnSet, HymnType


@dataclass
class BookDay:
    julian: datetime = Optional[datetime]
    gregorian: datetime = Optional[datetime]
    events: list[Event] = field(default_factory=list)


# @dataclass
class BookMonth:
    days: list[BookDay]

    def __init__(self):
        self.days = []
        for i in range(32):
            self.days.append(BookDay())


# @dataclass
class BookYear:
    months: list[BookMonth]

    def __init__(self):
        self.months = []
        for i in range(13):
            self.months.append(BookMonth())


class SaintsBook:
    _BOOK_SRC = "source_data/saints_book.html"
    # _BOOK_SRC = "source_data/saints_short.html"
    _BOOK_OUTPUT = 'output_data/xml'
    _BOOK_START_DATE = datetime(2019, 9, 1)  # SEP 1
    _DEBUG = False
    _book: BookYear

    soup: BeautifulSoup

    def __init__(self):
        pass

    def read_soup(self):
        with open(self._BOOK_SRC, 'r') as fp:
            self.soup = BeautifulSoup(fp, 'lxml')

    def print(self):
        print(self.soup)

    def read_book(self):
        self.read_soup()
        # this.book = this.createYearPages();
        last_day_index = 4 if self._DEBUG else 379
        skip_days = 0

        days: list[BookDay] = []
        for i in range(1, last_day_index):
            # if i != 378:
            #     continue

            julian = datetime(2019, 9, 1) + timedelta(days=i - skip_days - 1)

            day = self.query_day(julian, skip_days)

            if day is None:
                skip_days += 1
                continue

            if len(day.events) == 0:
                print(f'No events found for day {julian.isoformat()}')

            for event in day.events:
                print(event.header)

            days.append(day)

        year = BookYear()
        for day in days:
            year.months[day.julian.month].days[day.julian.day] = day

        self._book = year

    def print_book(self):
        print(self._book)

    def save_book(self):
        # days: list[BookDay] = []
        for m in self._book.months:
            for d in m.days:
                if len(d.events) > 0:
                    self.save_day(d)
                # days.append(d)

    def save_day(self, book_day: BookDay):
        day = ET.Element('day', {
            'julian': book_day.julian.isoformat(),
            'gregorian': book_day.gregorian.isoformat()
        })

        events = ET.SubElement(day, 'events')
        for book_event in book_day.events:
            event = ET.SubElement(events, 'event')

            id = ET.SubElement(event, 'id')
            id.text = book_event.id

            header = ET.SubElement(event, 'header')
            header.text = book_event.header

            content = ET.SubElement(event, 'content')
            for text in book_event.content:
                txt = ET.SubElement(content, 'text')
                txt.text = text

            if book_event.hymns and book_event.hymns.hymns and len(book_event.hymns.hymns) > 0:
                hymns = ET.SubElement(event, 'hymns')
                for hymn in book_event.hymns.hymns:
                    hmn = ET.SubElement(hymns, 'hymn', {
                        'echo': str(hymn.echo),
                        'type': 'troparion' if hymn.type == HymnType.Troparion else 'kontakion'
                    })

                    title = ET.SubElement(hmn, 'title')
                    title.text = hymn.title

                    h_content = ET.SubElement(hmn, 'content')
                    h_content.text = hymn.content

        tree = ET.ElementTree(day)
        ET.indent(tree)

        # ET.dump(day)

        out_path = f'{self._BOOK_OUTPUT}/{book_day.julian.month}'
        if not os.path.exists(out_path):
            os.makedirs(out_path)

        with open(f'{out_path}/{book_day.julian.day}.xml', 'wb') as f:
            tree.write(f, encoding='utf-8', xml_declaration=True)

    def read_book_xml(self):
        print('Reading book')

        days: list[BookDay] = []
        for m in range(1, 13):
            for d in range(1, monthrange(2020, m)[1] + 1):
                julian = datetime(2020, m, d)
                day = self.read_day_xml(julian)
                if day:
                    days.append(day)

        return days

    def filter_days(self, days: list[BookDay], gregorian: datetime) -> BookDay:
        ds = list(filter(lambda d: d.gregorian.month == gregorian.month and d.gregorian.day == gregorian.day, days))
        if len(ds) > 0:
            return ds[0]
        else:
            print(f'Nothing found for day: {gregorian.isoformat()} julian={gregorian_to_julian(gregorian)}')

    def read_day_xml(self, julian: datetime):
        in_path = f'{self._BOOK_OUTPUT}/{julian.month}/{julian.day}.xml'

        if not os.path.exists(in_path):
            # print(f'Day not found for {julian.isoformat()}')
            return None

        tree = ET.parse(in_path)
        day = tree.getroot()

        book_day = BookDay()
        book_day.julian = datetime.fromisoformat(day.get('julian'))
        book_day.gregorian = datetime.fromisoformat(day.get('gregorian'))

        events = []
        xml_events = day.findall('events/event')
        for xml_event in xml_events:
            xml_texts = [txt.text for txt in xml_event.findall('content/text')]

            hymns = []
            xml_hymns = xml_event.findall('hymns/hymn')
            if len(xml_hymns) > 0:
                hymns = [Hymn.from_xml(el) for el in xml_hymns]

            header = xml_event.find('header').text
            event = Event(
                id=xml_event.find('id').text,
                header=header,
                content=xml_texts,
                hymns=HymnSet(hymns, title=header)
            )
            events.append(event)

        book_day.events = events

        return book_day

    @staticmethod
    def days_between(date1: datetime, date2: datetime) -> int:
        return int(math.fabs((date1 - date2).days))

    def calc_day_index_ref(self, julian_day) -> int:
        day_index = SaintsBook.days_between(self._BOOK_START_DATE, julian_day) + 1

        return day_index

    @staticmethod
    def find_day_id(day_links):
        for link in day_links:
            if link['id'] and 'headertemplate' in link['id']:
                return link

        return None

    def query_day(self, julian_day, skip_days) -> BookDay | None:
        day_index = self.calc_day_index_ref(julian_day) + skip_days
        day_book_ref = f'div[id*="c{day_index}_"]'
        day_links = self.soup.select(day_book_ref)
        day_link = SaintsBook.find_day_id(day_links)

        if not day_link:
            raise Exception(f'Header template not found for {day_book_ref}')

        text_el = day_link.find_next_sibling('div', 'text')
        if text_el is None or 'text' not in text_el['class']:
            # Workaround for source bugs dayIndex === 55, 146, 156
            text_el = day_link.parent.find_next_sibling().select_one(':first-child')

            if not text_el or 'text' not in text_el.get('class', []):
                raise Exception(f'Text not found {day_book_ref}')

        el = text_el.select('.prp-pages-output')
        if len(el) == 0:
            print(f'Ignoring month index page {day_book_ref}')
            # raise Exception(f'Content element not found for {day_book_ref}')
            return None

        el = el[0]

        # Parallelize

        el = el.select('.heading')
        if len(el) == 0:
            print(f'Heading not found {day_book_ref}')
            return None

        el = el[0]

        # Print day name
        print(el.text.strip())

        el = el.find_next_sibling('hr')
        event_id = 1
        evs: list[Event] = []
        event, el = self.extract_event_content(el)
        event.id = self.gen_event_id(day_index, event_id)
        evs.append(event)

        while event is not None and el is not None:
            event, el = self.extract_event_content(el)

            if event is None or el is None:
                break

            event_id += 1
            event.id = self.gen_event_id(day_index, event_id)
            evs.append(event)

        return BookDay(events=evs,
                       julian=julian_day,
                       gregorian=julian_to_gregorian(julian_day))

    @staticmethod
    def gen_event_id(day_index, index):
        return f's-{day_index}-{index}'

    def extract_event_content(self, el) -> (Event, Tag):
        if el is None:
            return None, None

        def match_caps_heading(tag):
            classes = tag.get('class', [])
            return 'heading' in classes and 'h-caps' in classes

        hr = el
        if not match_caps_heading(el):
            el = el.find_next_sibling(match_caps_heading)

        header = None
        # id=314 try find combined header
        if el is None:
            # pass
            print('Searching combined header')
            el = hr.find_next_sibling()
            if el is None:
                print('Header not found')
                return None, None
            header = self.extract_text(el)
        else:
            h1 = []
            while el is not None and el.get('class') and 'heading' in el.get('class'):
                h1.append(self.extract_text(el))
                el = el.find_next_sibling()

            header = ' '.join(h1)

        if header is None:
            return None, None

        texts = []
        while (el is not None
               and (el.name == 'p' or el.name == 'span' or el.name == 'hr' or
                    (el.name == 'div' and 'epigraph2' in el.get('class', [])) or
                    ('heading' in el.get('class', [])
                     and 'h-caps' not in el.get('class', [])
                     and 'h-razr' not in el.get('class', [])
                    )
                    or 'lives-div' in el.get('class', []))):
            text = self.extract_text(el)
            if text:
                texts.append(text)

            el = el.find_next_sibling()

        hymns = self.extract_hymns(header, texts)

        return Event(header=self.clean_string(header), content=texts, hymns=hymns, id=''), el

    def extract_text(self, el):
        if not el:
            return ''

        drops = el.select('.dropinitial')
        if len(drops) > 0:
            for drop in drops:
                a = drop.select_one('a img')
                if a and len(a.get('alt', [])) > 0:
                    letter = a.get('alt')
                    drop.replace_with(letter)

        chu_texts = el.select('span.ponomar')
        if len(chu_texts) > 0:
            for text in chu_texts:
                ch = text.get('title')
                text.replace_with(ch)

        sups = el.select('sup')
        if len(sups) > 0:
            for sup in sups:
                sup.clear()

        return self.clean_string(el.text)

    def extract_hymns(self, header: str, texts: list[str]) -> HymnSet | None:
        if not texts or len(texts) == 0:
            return None

        hymns: list[Hymn] = []
        for idx in range(len(texts)):
            text = texts[idx]
            # for idx, text in enumerate(texts):
            if (text.startswith('Кондак')
                    or text.startswith('Другий кондак')
                    or text.startswith('Ин кондак')
                    or text.startswith('Тропарь')
                    or text.startswith('Другий тропарь')
                    or text.startswith('Ин тропарь')):
                h_type = HymnType.Troparion

                if (text.startswith('Кондак')
                        or text.startswith('Другий кондак')
                        or text.startswith('Ин кондак')):
                    h_type = HymnType.Kontakion

                echo: int = 0
                if m := re.match(r'.*, глас (\d):', text):
                    echo = int(m.group(1))

                hymns.append(Hymn(header=header,
                                  title=text,
                                  content=texts[idx + 1],
                                  type=h_type,
                                  echo=echo))

        return HymnSet(hymns=hymns, title=header)

    def clean_string(self, text: str) -> str:
        clean = text.replace('\n', ' ')

        clean = re.sub(r'\s+', ' ', clean)
        clean = clean.replace(u'\u200e', ' ')  # LRM

        # Fix
        clean = clean.replace('\\Хар', 'Хар')

        return clean.strip()
