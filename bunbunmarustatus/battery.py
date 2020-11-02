import subprocess
from .module import Module


def to_percentage(value):
    return str(value) + "%"


class Battery(Module):
    def get_block(self):
        result = subprocess.run("acpi", stdout=subprocess.PIPE)
        result_str = result.stdout.decode("utf-8")
        parsed = result_str.split(" ")
        status = parsed[2].split(",")[0]
        value = int(parsed[3].split("%")[0])

        color = None

        if status == "Discharging":
            if value < 15:
                color = "#FF0000"
            else:
                color = "#00EE00"
        elif status == "Charging":
            color = "#FFFF00"

        return {"full_text": to_percentage(value), "color": color}

    @staticmethod
    def get_name():
        return "battery"
