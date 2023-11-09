import os
from datetime import datetime


class TemplateBase:

    def get_template_path(self, name):
        return os.path.join(os.path.dirname(__file__), 'templates', f'{name}.md')

    def get_md_month_output_path(self, date: datetime):
        name = f'{date.month:02}'
        return os.path.join(os.path.dirname(__file__), '..', '..', '..', 'output_data', 'markdown', f'{name}.md')

    def get_md_pages_output_path(self):
        return os.path.join(os.path.dirname(__file__), '..', '..', '..', 'output_data', 'markdown', '100_pages.md')

    @staticmethod
    def get_md_calendar_output_path():
        return os.path.join(os.path.dirname(__file__), '..', '..', '..', 'output_data', 'markdown', '00_calendar_index.md')

    @staticmethod
    def get_date_link(date: datetime):
        return date.strftime('date-%Y-%m-%d')

    @staticmethod
    def get_date_title_link(date: datetime, title: str):
        date_link = TemplateBase.get_date_link(date)
        return f'[{title}](#{date_link})'
