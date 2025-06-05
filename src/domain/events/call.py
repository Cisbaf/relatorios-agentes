from dataclasses import dataclass
from datetime import datetime

@dataclass
class Call:
    number: str
    start: datetime
    end: datetime
    dutation: datetime
    description: str
