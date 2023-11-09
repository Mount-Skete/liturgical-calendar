import chevron
from .TemplateBase import TemplateBase
from book.data import Event
from .Page import Page
from book.views.markdown import YearData


class Pages(TemplateBase):

    def render(self, events: list[Event]):
        page = Page()
        pages = page.render(events)

        path = self.get_template_path('events')

        data = {
            'events': pages
        }
        with open(path, 'r') as f:
            return chevron.render(f, data)

    def to_file(self, events: list[Event]):
        text = self.render(events)

        path = self.get_md_pages_output_path()
        with open(path, 'w') as f:
            f.write(text)

    def save_year_data(self, year_data: YearData):
        events: list[Event] = []

        for month in year_data.monthsData:
            for day in month.daysData:
                events.extend(day.events)

        return self.to_file(events)
