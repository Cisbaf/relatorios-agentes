from typing import Optional, List
from src.domain.entities.register import Register


class Event:

    def __init__(self, registers: Optional[List[Register]]):
        self._regiters: List[Register] = []
        if registers:
            self._register_list_(registers)

    def _register_list_(self, registers: List[Register]):
        for register in registers:
            self.register(register)

    def validate(self, current: Register):
        return True
       
    
    def register(self, register: Register):
        if self.validate(register):
            self.analyze(register)
            self._regiters.append(register)

    def analyze(self, current: Register):
        raise NotImplementedError

    def to_json(self):
        raise NotImplementedError