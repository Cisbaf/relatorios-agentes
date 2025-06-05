from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from domain.entities import Register
from domain.utils.type import get_type_status_agent

@dataclass
class Status:
    value: int
    registers: Optional[List[Register]]
    start: datetime
    end: Optional[datetime]
    finalised = False

    @property
    def duration(self):
        if self.end:
            return self.end - self.start
    
    @property
    def status(self):
        status_agent = get_type_status_agent(self.value).translate()
        
        if self.end:
            return f'{status_agent} Periodo: <{self.start.strftime("%H:%M")} á {self.end.strftime("%H:%M")}> Total: {self.duration}'
     
        return f'{status_agent} Estado Atual a {(datetime.now() - self.start)}'
    
    

    # def __repr__(self):
    #     return f'{get_type_status_agent(self.value).translate()}: Periodo({self.start.strftime("%H:%M")}, {self.end.strftime("%H:%M") if self.end else ''}) Tempo Total: {self.duration}'