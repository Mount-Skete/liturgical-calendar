import chevron
from .TemplateBase import TemplateBase
from book.data import Event


class Page(TemplateBase):
    def render_one(self, event: Event):
        path = self.get_template_path('event')

        with open(path, 'r') as f:
            return chevron.render(f, event)

    def render(self, events: list[Event]):
        return [self.render_one(e) for e in events]
