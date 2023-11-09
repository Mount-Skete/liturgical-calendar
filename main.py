import locale
from argparse import ArgumentParser
from datetime import datetime, timedelta
from calendar import monthrange
from julian_calendar import (calculate_echo_gregorian,
                             gregorian_to_julian,
                             calculate_orthodox_easter_gregorian)
from book.views.markdown import DayData, MonthData, Year, YearData, Calendar, Pages, TemplateBase
from book.sources import SaintsBook
from book.data import Event, HymnSet

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, locale.locale_alias['ru'])

    parser = ArgumentParser()
    parser.add_argument("--parse-sources",
                        dest="parse_sources",
                        required=False,
                        action="store_true")
    args = parser.parse_args()

    book = SaintsBook()
    if args.parse_sources:
        print("Parsing sources")
        book.read_book()
        book.save_book()

    cal = Calendar()
    cal.tofile(2023, TemplateBase.get_md_calendar_output_path())

    book = SaintsBook()
    days = book.read_book_xml()

    year = 2023

    easter = calculate_orthodox_easter_gregorian(year)
    trinity = easter + timedelta(days=49)
    whit = easter + timedelta(days=50)

    special_events = {
        easter.isoformat():
            Event(id="sp-1", header='Пасха', hymns=HymnSet([], 'Пасха'), content=[], is_special=True),
        trinity.isoformat():
            Event(id="sp-2", header='День Святой Троицы', hymns=HymnSet([], 'День Святой Троицы'), content=[],
                  is_special=True),
        whit.isoformat():
            Event(id="sp-3", header='День Святого Духа', hymns=HymnSet([], 'День Святого Духа'), content=[],
                  is_special=True)
    }

    m_data = []
    for m in range(1, 13):
        gregorian = datetime(year, m, 1)
        days_data = []
        for d in range(1, monthrange(year, m)[1] + 1):
            gregorian_date = datetime(year, m, d)
            ds = book.filter_days(days, gregorian_date)

            if not ds:
                print(f'No data for day {gregorian}')
                continue

            echo = calculate_echo_gregorian(gregorian_date)

            hymns = []

            if gregorian_date.isoformat() in special_events:
                ds.events.append(special_events[gregorian_date.isoformat()])

            if len(ds.events) > 0:
                for evt in ds.events:
                    if evt.hymns and len(evt.hymns.hymns) > 0:
                        hymns.append(evt.hymns)

            days_data.append(DayData(gregorian_date=gregorian_date,
                                     julian_date=gregorian_to_julian(gregorian_date),
                                     hymns=hymns,
                                     events=ds.events,
                                     echo=echo))

        m_data.append(MonthData(gregorian_date=gregorian, daysData=days_data))

    year_data = YearData(year, monthsData=m_data)
    year = Year()
    year.to_file(year_data)

    pages = Pages()
    pages.save_year_data(year_data)
