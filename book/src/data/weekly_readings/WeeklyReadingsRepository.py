import os
import xml.etree.ElementTree as ET

from .WeeklyReadingXmlSerializer import WeeklyReadingXmlSerializer
from .WeeklyReadings import WeeklyReadings


class WeeklyReadingsRepository:
    WEEKLY_READINGS_DATA_PATH = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        '..',
        '..',
        'data',
        'gospel-and-apostolic-readings-ru',
        'weekly-readings-index.xml'
    )

    weekly_readings: WeeklyReadings

    def __init__(self, path: str = WEEKLY_READINGS_DATA_PATH):
        self.load_all(path)

    def load_all(self, path: str):
        root = ET.parse(path).getroot()

        self.weekly_readings = WeeklyReadingXmlSerializer.parse_all(root)
