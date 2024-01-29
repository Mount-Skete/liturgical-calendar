import chevron

from data import Feast
from .TemplateBase import TemplateBase


class Page(TemplateBase):
    def render_one(self, feast: Feast):
        path = self.get_template_path('event')

        with open(path, 'r') as f:
            return chevron.render(f, feast)

    def render(self, feasts: list[Feast]):
        return [self.render_one(e) for e in feasts]
