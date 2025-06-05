from dataclasses import dataclass
from relatorios_agent.domain.status_agent.entities.status_agent import StatusAgent
from relatorios_agent.domain.status_agent.values_object.type_pause import TypePause

@dataclass
class Pause(StatusAgent):
    type: TypePause
    
