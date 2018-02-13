from mpd import MPDClient
from .module import Module

client = MPDClient()

def get_current_song():
    try:
        client.connect("localhost", 6600)
        current = client.currentsong()
        client.close()
        client.disconnect()
        return current["title"] + " - " + current["artist"]

    except:
        return ""

class MPD(Module):
    def get_name(self):
        return "mpd"
    
    def get_block(self):
        return {"full_text": get_current_song() }