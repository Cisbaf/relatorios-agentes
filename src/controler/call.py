from typing import List, Dict
from domain.entities import Register, Call, TypeStatusAgent, TypeStatusRamal
from datetime import timedelta


class CallController:

    def __init__(self):
        self.calls: List[Call] = []
        self.last: Register = None
   
    def register(self, current: Register):
        if current.type_status_agent is not TypeStatusAgent.IsLoggedIn:
            return None
        if (self.last is not None
            and self.last.type_status_ramal is TypeStatusRamal.OCUPADO
            and current.type_status_ramal is TypeStatusRamal.LIVRE
            ):
            self.calls.append(Call(
                number=self.last.number_call,
                start=self.last.dt_status_ramal,
                end=current.dt_status_ramal,
                n_ch_acd=self.last.n_ch_acd
            ))
        self.last = current

    def register_all(self, registers: List[Register]):
        for register in registers:
            self.register(register)

    def get_time_in_call(self):
        return sum((call.duration for call in self.calls), timedelta())
    
    def __repr__(self):
        return f'Total de Ligações: {len(self.calls)} | Tempo total | {self.get_time_in_call()}'