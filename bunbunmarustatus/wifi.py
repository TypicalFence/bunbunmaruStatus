import wpa_status
from .module import Module


class Wifi(Module):
    def __init__(self):
        super().__init__()
        self._client = wpa_status.Client()

    def get_block(self):
        running_resp = wpa_status.is_supplicant_running(self._client)
        running = running_resp["result"]["SupplicantRunning"]["running"]

        if running:
            status_resp = wpa_status.status(self._client)
            status = status_resp["result"]["Status"]
            if "ssid" in status:
                ssid = status["ssid"]
                text = "wifi: " + ssid
            else:
                "wifi: disconnected"
        else:
            text = "wifi: off"

        return {"full_text": text}

    def get_name(self):
        return "wifi"
