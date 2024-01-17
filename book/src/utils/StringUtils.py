import re


class StringUtils:
    __rx_spaces = re.compile('\s+')
    __rx_newlines = re.compile('\n+')

    @staticmethod
    def clean(text):
        return StringUtils.__rx_spaces.sub(' ', text).strip()

    @staticmethod
    def clean_lines(text):
        return StringUtils.__rx_spaces.sub(' ', text).strip()

    @staticmethod
    def clean_all(text):
        return StringUtils.clean(StringUtils.clean_lines(text))
