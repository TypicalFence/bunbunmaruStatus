from mpd import MPDClient

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
