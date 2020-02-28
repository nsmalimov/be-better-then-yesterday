from enum import Enum


class ButtonType(Enum):
    QUOTE = "Мотивирующая цитата"
    GOOD = "Сказать, что было хорошо"
    BAD = "Сказать, что было плохо"
    END = "Завершить"
    HELP = "Помощь"
    OPPORTUNITIES = "Возможности"


class User:
    def __init__(self, id=None):
        self.id = id

    def load_by_dict(self, **entries):
        self.__dict__.update(entries)


class Quote:
    def __init__(self, text=None, author=None):
        self.text = text
        self.author = author

    def load_by_dict(self, **entries):
        self.__dict__.update(entries)


class Record:
    def __init__(self, type=None, text=None, user_id=None):
        self.type = type
        self.text = text
        self.user_id = user_id

    def load_by_dict(self, **entries):
        self.__dict__.update(entries)
