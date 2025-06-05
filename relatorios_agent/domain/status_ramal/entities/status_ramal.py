from dataclasses import dataclass
from datetime import datetime

@dataclass
class StatusRamal:
    id_object: str
    start: datetime
    end: datetime

    def duration(self):
        return self.end - self.start