

from typing import List, Tuple
from domain.entities import Register, TypeStatusAgent, Pause
from datetime import timedelta

class FreeController:

    def __init__(self):
        self.removeds: List[Tuple] = []
        self.last: Register = None
        self.last_ringing: Register = None

    def register(self, current: Register):
        if (self.last is not None
            and self.last.type_status_agent is TypeStatusAgent.IsOnBreak
            and current.type_status_agent is not TypeStatusAgent.IsOnBreak
            ):
            self.pauses.append(Pause(
                cod=self.last.cod_pause,
                start=self.last.dt_status_agent,
                end=current.dt_status_agent
            ))
        self.last = current
