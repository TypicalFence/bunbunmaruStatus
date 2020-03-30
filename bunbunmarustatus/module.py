from abc import ABC

class Module(ABC):
    def register(self, status):
        status.add_module(self)
    
    def get_block(self):
        raise NotImplementedError
    
    @staticmethod
    def name():
        raise NotImplementedError
