import time
import datetime
from mpd import MPDClient

mpd_client = MPDClient()

def get_current_song():
    try:
        mpd_client.connect("localhost", 6600)
        current = mpd_client.currentsong()
        mpd_client.close()
        mpd_client.disconnect()
        return current["title"] + " - " + current["artist"]
    except:
        return ""


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

def run(interval):
    while True:
        date = get_date()
        song = get_current_song()
        current_time  = get_time()
        
        print(song + " " + date + " " + current_time)
        time.sleep(interval)

if __name__ == "__main__":
    run(5)
