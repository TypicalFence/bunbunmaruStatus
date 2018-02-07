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

    def _render(self):
        view = {}
        for module_name in self.modules:
            view[module_name] = self.modules[module_name].get_text()
        return view

    def add_module(self, module):
        if module.get_name() in self.config:
            self.modules[module.get_name()] = module

    def get_status(self):
        view = self._render()
        return pystache.render(self.pattern, view)
 
if __name__ == "__main__":
    print("fuck yeah")
    status = Status()
    Time().register(status)
    Battery().register(status)
    print(status.get_status())
