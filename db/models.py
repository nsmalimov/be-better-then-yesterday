from enum import Enum


class RecordTypes(Enum):
    GOOD = "good"
    BAD = "bad"


class UserStatuses(Enum):
    WAIT = "wait"
    SEND_GOOD = "send_good"
    SEND_BAD = "send_bad"


class User:
    def __init__(self, id=None, status=None):
        self.id = id
        self.status = status

    def load_by_dict(self, **entries):
        self.__dict__.update(entries)


class Quote:
    def __init__(self, text=None, author=None):
        self.text = text
        self.author = author

    def load_by_dict(self, **entries):
        self.__dict__.update(entries)


class Record:
    def __init__(self, type=None, text=None, user_id=None, count=None, created_at=None):
        self.type = type
        self.text = text
        self.user_id = user_id
        self.count = count
        self.created_at = created_at

    def load_by_dict(self, **entries):
        self.__dict__.update(entries)
