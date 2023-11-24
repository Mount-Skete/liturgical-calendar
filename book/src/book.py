import locale
from calendar import monthrange
from datetime import datetime

from data import FeastsRepository, DailyHymns
from julian_calendar import calculate_echo_gregorian, gregorian_to_julian
from views.markdown import DayData, MonthData, Year, YearData, Pages, TemplateBase, Calendar


class Book:

    def __init__(self, year: int):
        self.__year = year

        locale.setlocale(locale.LC_ALL, locale.locale_alias['ru'])

    def create(self):

        year = self.__year
        feasts = FeastsRepository(year)
        feasts = feasts.read_all()

        print(f'Loaded {len(feasts)} feasts')

        cal = Calendar()
        cal.tofile(year, TemplateBase.get_md_calendar_output_path())

        wh = DailyHymns()

        m_data = []
        for m in range(1, 13):
            gregorian = datetime(year, m, 1)
            days_data = []
            for d in range(1, monthrange(year, m)[1] + 1):
                gregorian_date = datetime(year, m, d)
                ds = feasts.for_date(gregorian_date)

                if not ds:
                    print(f'No data for day g={gregorian} j={gregorian_to_julian(gregorian)}')
                    continue

                echo = calculate_echo_gregorian(gregorian_date)
                daily_hymn = wh.for_date(gregorian_date, echo)

                days_data.append(DayData(gregorian_date=gregorian_date,
                                         julian_date=gregorian_to_julian(gregorian_date),
                                         feasts=ds,
                                         echo=echo,
                                         daily_hymn=daily_hymn))

            m_data.append(MonthData(gregorian_date=gregorian, daysData=days_data))

        year_data = YearData(year, monthsData=m_data)
        year = Year()
        year.to_file(year_data)

        pages = Pages()
        pages.save_year_data(year_data)
