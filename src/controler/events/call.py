from src.domain.repositories.event import Event
from src.domain.enum import TypeStatusAgent

class CallEvent(Event):

    def __init__(self, registers):
        super().__init__(registers)

    def validate(self, current):
        if(current.type_status_agent != TypeStatusAgent.IsLoggedIn):
            return False

    def analyze(self, current):
        return super().analyze(current)