from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from relatorios_agent.domain.status_event.values_object.type_status_agent import TypeStatusAgent
from relatorios_agent.domain.status_event.values_object.type_status_ramal import TypeStatusRamal


@dataclass
class StatusEvent:
    # obrigatorios
    id: str
    name_agent: str
    channel: str
    status_agent: TypeStatusAgent
    dt_status_agent: datetime
    status_ramal: TypeStatusRamal
    dt_status_ramal: datetime
    n_ch_acd: int
    # optionais
    cod_pause: Optional[int]
    uid: Optional[str]
    number_call: Optional[str]

    @classmethod
    def build_from_dict(cls, data: dict):

        return StatusEvent(
            id=data['id'],
            name_agent=data['n_agente'],
            channel=data['channel'],
            status_agent=TypeStatusAgent.get(int(data['status'])),
            dt_status_agent=datetime.strptime(data['date_status_dt'], '%d/%m/%Y, %H:%M:%S'),
            status_ramal=TypeStatusRamal.get(int(data['STATUS_'])),
            dt_status_ramal=datetime.strptime(data['last_date_dt'], '%d/%m/%Y, %H:%M:%S'),
            n_ch_acd=int(data['n_ch_acd']),
            cod_pause=int(data['tp_de_pausa']) if data['tp_de_pausa'] else None,
            uid=data['uid'] if data['uid'] else None,
            number_call=data['CALLERID_R_ANI'] if data['CALLERID_R_ANI'] else None
        )
