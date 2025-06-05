from typing import List
from domain.entities import Register, Pause, TypeStatusAgent
from datetime import timedelta

class PauseController:

    def __init__(self):
        self.pauses: List[Pause] = []
        self.last: Register = None
   
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

    def get_time_in_pause(self):
        return sum((pause.duration for pause in self.pauses), timedelta())

    def __repr__(self):
        return f'Quantidade de Pausas: {len(self.pauses)} | Tempo Total em Pausa: {self.get_time_in_pause()}'