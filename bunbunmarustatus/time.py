import datetime
from .module import Module


def prepend_zero(s):
    if len(s) < 2:
        return str(0) + s
    return s


def get_date():
    today = datetime.date.today()
    return prepend_zero(str(today.day)) + "-" + prepend_zero(str(today.month))


def get_time():
    now = datetime.datetime.now()
    hour = prepend_zero(str(now.hour))
    minute = prepend_zero(str(now.minute))
    return hour + ":" + minute


class Time(Module):
    def get_block(self):
        text = get_date() + " " + get_time()
        return {"full_text": text}

    @staticmethod
    def get_name():
        return "time"
