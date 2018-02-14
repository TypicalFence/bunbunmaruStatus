from .module import Module
from .status import Status
from .time import Time
from .battery import Battery
from .mpd_client import MPD
from .pulse import PulseAudio

modules = {}

def _add_module(m):
    modules[m().get_name()] = m

_add_module(Time)
_add_module(Battery)
_add_module(MPD)
_add_module(PulseAudio)

def factory(status):
    config = status.config

    for module in config:
        modules[module]().register(status)
    
