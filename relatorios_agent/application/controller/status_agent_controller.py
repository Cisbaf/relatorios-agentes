from relatorios_agent.domain.status_agent.entities.status_agent import StatusAgent
from relatorios_agent.domain.status_agent.entities.logged import Logged
from relatorios_agent.domain.status_agent.entities.removed import Removed
from relatorios_agent.domain.status_agent.entities.pause import Pause
from relatorios_agent.domain.status_event.entities.status_event import StatusEvent, TypeStatusAgent
from relatorios_agent.domain.status_agent.values_object.type_pause import TypePause
from relatorios_agent.domain.exceptions import DomainException
from typing import List


class StatusAgentController:
    def __init__(self):
        self.prev_status: StatusAgent = None

    def get(self, status: StatusEvent) -> StatusAgent:
        status_agent = None
        default_fields = {
            "id_object": status.id,
            "start": status.dt_status_agent,
            "end": None
        }

        if status.status_agent == TypeStatusAgent.IsLoggedIn and not isinstance(self.prev_status, Logged):
            status_agent = Logged(**default_fields)

        if status.status_agent == TypeStatusAgent.IsRemoved and not isinstance(self.prev_status, Removed):
            status_agent = Removed(**default_fields, number=status.number_call)
            
        if status.status_agent == TypeStatusAgent.IsOnBreak and not isinstance(self.prev_status, Pause):
            status_agent = Pause(**default_fields, type=TypePause.get(status.cod_pause))

        if self.prev_status:
            self.prev_status.end = status.dt_status_agent

        self.prev_status = status_agent

        return status_agent
