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
    def get_text(self):
        return get_date() + " " + get_time()
    
    def get_name(self):
        return "time"