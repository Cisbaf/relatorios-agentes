from dataclasses import dataclass
from relatorios_agent.domain.status_ramal.entities.status_ramal import StatusRamal

@dataclass
class Call(StatusRamal):
    number: str
    n_ch_acd: int
