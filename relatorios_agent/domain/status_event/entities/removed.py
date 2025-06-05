from dataclasses import dataclass
from domain.status_agent.entities.status_agent import StatusAgent

@dataclass
class Removed(StatusAgent):
    number: str

