from relatorios_agent.domain.status_ramal.entities.status_ramal import StatusRamal
from relatorios_agent.domain.status_ramal.entities.call import Call
from relatorios_agent.domain.status_ramal.entities.ringing import Ringing
from relatorios_agent.domain.status_ramal.entities.free import Free
from relatorios_agent.domain.status_event.entities.status_event import StatusEvent, TypeStatusRamal, TypeStatusAgent
from relatorios_agent.domain.exceptions import DomainException
from typing import List


class StatusRamalController:
    def __init__(self):
        self.prev_status: StatusRamal = None

    def get(self, status: StatusEvent) -> StatusRamal:
        status_ramal = None
        default_fields = {
            "id_object": status.id,
            "start": status.dt_status_ramal,
            "end": None
        }

        if status.status_ramal == TypeStatusRamal.LIVRE:
            status_ramal = Free(**default_fields)

        if status.status_ramal == TypeStatusRamal.RINGING:
            status_ramal = Ringing(**default_fields, number=status.number_call)

        if status.status_ramal == TypeStatusRamal.OCUPADO:
            status_ramal = Call(**default_fields, number=status.number_call, n_ch_acd=status.n_ch_acd)
            
        if self.prev_status:
            self.prev_status.end = status.dt_status_ramal

        self.prev_status = status_ramal

        return status_ramal
