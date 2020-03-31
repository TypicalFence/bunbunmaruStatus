import json
from .time import Time
from .battery import Battery
from .mpd_client import MPD
from .pulse import PulseAudio
from .wifi import Wifi


MODULES = {}
DEFAULT_PATTERN = "time"


class Status(object):
    def __init__(self, pattern=DEFAULT_PATTERN):
        self.modules = {}
        self.pattern = pattern
        self.config = self.pattern.split(" ")

    def _get_blocks(self):
        blocks = []
        for module_name in self.config:
            block = self.modules[module_name].get_block()
            block["separator"] = False
            blocks.append(block)
        return blocks

    def add_module(self, module):
        if module.get_name() in self.config:
            self.modules[module.get_name()] = module

    def get_status(self):
        blocks = self._get_blocks()
        return json.dumps(blocks)


def factory(status):
    config = status.config

    for module in config:
        MODULES[module]().register(status)


def _add_module(m):
    MODULES[m.get_name()] = m


_add_module(Time)
_add_module(Battery)
_add_module(MPD)
_add_module(PulseAudio)
_add_module(Wifi)
