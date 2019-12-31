import ini
import wpa_status
from .module import Module


class Wifi(Module):
    def __init__(self):
        super().__init__()
        self._config = ini.parse(open("/etc/wpa_statusd.ini").read())
        self._client = wpa_status.Client(self._config["socket"])

    def _get_text(self):
        text = ""
        running_resp = wpa_status.is_supplicant_running(self._client)
        running = running_resp.result["SupplicantRunning"]["running"]

        if running:
            status_resp = wpa_status.status(self._client)
            status = status_resp.result["Status"]
            if status["ssid"] is not None:
                ssid = status["ssid"]
                text = "wifi: " + ssid
            else:
                text = "wifi: disconnected"
        else:
            text = "wifi: off"

        return text

    def get_block(self):
        text = ""

        try:
            text = self._get_text()
        # TODO: I dunno, it happens ;w;
        except:
            pass

        return {"full_text": text}

    def get_name(self):
        return "wifi"
