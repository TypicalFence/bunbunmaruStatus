import json
import pystache
from .time import Time
from .battery import Battery

default_pattern = "{{time}}"

# evil hacky hack
def get_mustache_keys(template):
    parsed_template = pystache.parse(template)
    keys = []
    parse_tree = parsed_template._parse_tree
    keyed_classes = ( pystache.parser._EscapeNode,
                      pystache.parser._LiteralNode,
                      pystache.parser._InvertedNode,
                      pystache.parser._SectionNode )
    for token in parse_tree:
        if isinstance(token, keyed_classes):
            keys.append(token.key)
    return list(set(keys))

class Status(object):
    def __init__(self, pattern=default_pattern):
        self.modules = {}
        self.pattern = pattern
        self.config = get_mustache_keys(self.pattern)

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
