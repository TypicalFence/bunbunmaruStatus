import subprocess
from termcolor import colored
from .module import Module

def to_percentage(value): 
    return str(value) + "%"

class Battery(Module):
    def get_text(self):
        result = subprocess.run("acpi", stdout=subprocess.PIPE)
        result_str = result.stdout.decode("utf-8")
        parsed = result_str.split(" ")
        status = parsed[2].split(",")[0]
        value = int(parsed[3].split("%")[0])

        if status == "Discharging":
            if value < 15:
                return colored(to_percentage(value), "red")
            else:
                return colored(to_percentage(value), "green")
        elif status == "Charging":
            return colored(to_percentage(value), "yellow")
        
        return to_percentage(value)

    def get_name(self):
        return "battery"
        

if __name__ == "__main__":
    bat = Battery()
    print(bat.get_text())