from dataclasses import dataclass
from datetime import datetime

@dataclass
class Call:
    number: str
    start: datetime
    end: datetime
    n_ch_acd: int

    @property
    def duration(self):
        # Calcula a diferença de tempo
        return self.end - self.start

    def __repr__(self):
        return f'On Call > {self.number} | Start In {self.start} | End In {self.end} | Duration {self.duration} | Count ACD {self.n_ch_acd}'