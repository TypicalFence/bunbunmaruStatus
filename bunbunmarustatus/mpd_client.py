from mpd import MPDClient
from .module import Module


class MPD(Module):
    def __init__(self):
        self._client = MPDClient()

    @staticmethod
    def get_name():
        return "mpd"

    def get_block(self):
        return {"full_text": self._get_current_song()}

    def _get_song_string(self):
        current = self._client.currentsong()
        return current["title"] + " - " + current["artist"]

    def _get_current_song(self):
        try:
            self._client.connect("localhost", 6600)

            state = self._client.status()["state"]
            output = self._get_song_string()

            self._client.close()
            self._client.disconnect()

            if state == "play":
                return output
            elif state == "pause":
                return "*" + output + "*"
            elif state == "stop":
                return ""

        except:
            return ""
