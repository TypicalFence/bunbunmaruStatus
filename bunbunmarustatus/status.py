import json
from .time import Time
from .battery import Battery

default_pattern = "time"

class Status(object):
    def __init__(self, pattern=default_pattern):
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
