from typing import List, Tuple
from domain.entities import Register, TypeStatusAgent
from datetime import timedelta

class RemovedController:

    def __init__(self):
        self.removeds: List[Tuple] = []
        self.last: Register = None
        self.last_ringing: Register = None

    def register(self, current: Register):
        if (current.type_status_agent is TypeStatusAgent.IsLoggedIn
            and current.type_status_ramal is TypeStatusAgent.RINGING
            ):
            self.last_ringing = current

        if current.type_status_agent is TypeStatusAgent.IsRemoved:
            self.removeds.append((self.last_ringing.number_call, current.dt_status_ramal))
     
