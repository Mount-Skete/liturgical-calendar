import re


class StringUtils:
    __rx = re.compile('\s+')

    @staticmethod
    def clean(text):
        return StringUtils.__rx.sub(' ', text).strip()
