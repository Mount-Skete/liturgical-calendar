import re
from calendar import monthrange
from datetime import datetime, timedelta
from xml.etree.ElementTree import Element

from .Weekday import Weekday
from julian_calendar import (calculate_orthodox_easter_julian, julian_to_gregorian)


class DateXmlSerializer:

    @staticmethod
    def parse(xml: Element, year: int) -> datetime:
        if xml.find('julian') is not None:
            date = xml.find('julian').text
            julian = DateXmlSerializer.__parse_date(year, date)
        elif xml.find('easter') is not None:
            easter = calculate_orthodox_easter_julian(year)
            easter_el = xml.find('easter')
            days = int(easter_el.get('days', 0))

            julian = easter + timedelta(days=days)

            shift = easter_el.get('shift')
            if shift is not None:
                shift_match = re.fullmatch(r'(\d):(\w{3})', shift)
                shift_weeks = int(shift_match.groups()[0])
                shift_day = Weekday.from_value(shift_match.groups()[1])

                days_shift = shift_day.value - julian.weekday() + (shift_weeks - 1) * 7
                julian += timedelta(days=days_shift)
        else:
            raise NotImplementedError('Date format not supported')

        return julian

    @staticmethod
    def parse_to_gregorian(xml, year: int) -> datetime:
        return julian_to_gregorian(DateXmlSerializer.parse(xml, year))

    @staticmethod
    def __parse_date(year, date):
        parts = date.split('-')
        month = int(parts[0])
        day = int(parts[1])

        month_days = monthrange(year, month)[1]
        if day > month_days:
            # Skipping non-leap year
            return None

        return datetime(year, month, day)
