import calendar
from datetime import datetime
from .CalendarUtils import CalendarUtils
from .TemplateBase import TemplateBase


class Calendar(calendar.TextCalendar):

    def __init__(self):
        self.setfirstweekday(0)
        
    def formatday(self, day, weekday, width):
        if day == 0:
            return ''

        day_formatted = super().formatday(day, weekday, width)
        # [1](  # date-2023-0-1)

        gregorian_date = datetime(self._current_year, self._current_month, day)
        day_link = TemplateBase.get_date_title_link(gregorian_date, day_formatted)

        return day_link

    def formatmonthname(self, theyear, themonth, width, withyear=...):
        return CalendarUtils.MONTH_NAMES_RU[themonth - 1]

    def formatweekheader(self, width):
        result = ' | '.join(self.formatweekday(i, width) for i in self.iterweekdays())
        return f'| {result} |'

    def formatweek(self, theweek, width):
        result = ' | '.join(self.formatday(d, wd, width) for (d, wd) in theweek)
        return f'| {result} |'

    # Refactor to pass year and month to day formatting
    _current_year: int
    _current_month: int

    def formatmonth(self, theyear, themonth, w=1, l=1):
        self._current_year = theyear
        self._current_month = themonth
        lines = super().formatmonth(theyear, themonth, w, l).splitlines()
        lines.insert(1, '\n')
        align_center_pattern = f'|{"|".join([":-:"] * 7)}|'
        lines.insert(3, align_center_pattern)
        result = '\n'.join(lines) + '\n'

        return result

    def formatyear(self, theyear, w=..., l=..., c=..., m=...):
        months = [self.formatmonth(theyear, m) for m in range(1, 13)]
        result = '\n'.join(months)

        # lines = super().formatyear(theyear, w, l, c, m).splitlines()
        # result = '\n'.join(line.strip() if line.startswith('|') else f'{line.strip()}\n' for line in lines)

        return result

    def tofile(self, year: int, path: str):
        result = self.formatyear(year, w=1, l=1, c=1, m=1)

        with open(path, 'w+') as f:
            return f.write(result)
