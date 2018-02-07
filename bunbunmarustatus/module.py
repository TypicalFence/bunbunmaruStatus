from abc import ABC

class Module(ABC):
    def register(self, status):
        status.add_module(self)
    
    def get_text(self):
        raise NotImplementedError
    
    def get_name(self):
        raise NotImplementedError