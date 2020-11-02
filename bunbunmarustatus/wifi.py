import subprocess
import ini
import wpa_status
from .module import Module


class Wifi(Module):
    def __init__(self):
        super().__init__()
        self._config = ini.parse(open("/etc/wpa_statusd.ini").read())
        self._client = wpa_status.Client(self._config["socket"])
        self._text_cache = ""

    def _get_text(self):
        text = ""
        running_resp = wpa_status.is_supplicant_running(self._client)
        running = running_resp.result["SupplicantRunning"]["running"]

        if running:
            status_resp = wpa_status.status(self._client)
            status = status_resp.result["Status"]
            if status["ssid"] is not None:
                ssid = status["ssid"]
                text = ssid
            else:
                text = "disconnected"
        else:
            text = "off"

        return text

    def get_block(self):
        text = self._text_cache

        try:
            text = self._get_text()
            self._text_cache = text
        # TODO: I dunno, it happens ;w;
        except:
            pass

        return {"full_text": text}

    @staticmethod
    def get_name():
        return "wifi"


class NetworkManagerWifi(Module):
    def __init__(self):
        super().__init__()
        self._text_cache = ""

    def _is_running(self):
        result = subprocess.run(
            ["nmcli", "radio", "wifi"],
            stdout=subprocess.PIPE
        )
        result_str = result.stdout.decode("utf-8")
        return result_str == "enabled\n"

    def _get_text(self):
        text = ""

        if self._is_running():
            result = subprocess.run(
                ["iwgetid", "-r"],
                stdout=subprocess.PIPE
            )
            result_str = result.stdout.decode("utf-8").strip("\n")

            if result_str == "":
                text = "disconnected"
            else:
                text = result_str
        else:
            text = "off"

        return text

    def get_block(self):
        text = self._text_cache

        text = self._get_text()
        self._text_cache = text

        return {"full_text": text}

    @staticmethod
    def get_name():
        return "nmwifi"
