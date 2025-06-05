from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from domain.utils import type as type_status

@dataclass
class Register:
    # obrigatorios
    id: str
    name_agent: str
    channel: str
    status_agent: int
    dt_status_agent: datetime
    status_ramal: int
    dt_status_ramal: datetime
    n_ch_acd: int
    # optionais
    cod_pause: Optional[int]
    uid: Optional[str]
    number_call: Optional[str]

    @property
    def type_status_agent(self):
        return type_status.get_type_status_agent(self.status_agent)

    @property
    def type_status_ramal(self):
        return type_status.get_type_status_ramal(self.status_ramal)

    @classmethod
    def build_from_dict(cls, data: dict):

        return Register(
            id=data['id'],
            name_agent=data['n_agente'],
            channel=data['channel'],
            status_agent=int(data['status']),
            dt_status_agent=datetime.strptime(data['date_status_dt'], '%d/%m/%Y, %H:%M:%S'),
            status_ramal=int(data['STATUS_']),
            dt_status_ramal=datetime.strptime(data['last_date_dt'], '%d/%m/%Y, %H:%M:%S'),
            n_ch_acd=int(data['n_ch_acd']),
            cod_pause=int(data['tp_de_pausa']) if data['tp_de_pausa'] else None,
            uid=data['uid'] if data['uid'] else None,
            number_call=data['CALLERID_R_ANI'] if data['CALLERID_R_ANI'] else None
        )
    
    @property
    def _repr_simply_(self):
        return f'Name: {self.name_agent} | StatusAgente: {self.status_agent} | StatusRamal: {self.status_ramal}'

    # def __repr__(self):
    #     return f'Name: {self.name_agent} | StatusAgente: {self.status_agent} | StatusRamal: {self.status_ramal}'
