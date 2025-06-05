from dataclasses import dataclass
from datetime import datetime
from domain.utils.type import get_type_pause

@dataclass
class Pause:
    cod: int
    start: datetime
    end: datetime

    @property
    def type(self):
        return get_type_pause(self.cod)
    
    @property
    def duration(self):
        # Calcula a diferença de tempo
        return self.end - self.start

    def __repr__(self):
        return f'Pausa {self.type.translate()} | Start In {self.start} | End In {self.end} | Duration | {self.duration}'

