from enum import Enum

class ButtonType(Enum):
    BAD = "bad"
    GOOD = "good"
    QUOTE = "quote"

class User:
    def __init__(self, **entries):
        self.__dict__.update(entries)

class Quote:
    def __init__(self, text, author):
        self.text = text
        self.author = author

class Record:
    def __init__(self, type, text):
        self.type = type
        self.text = text
