from domain.status_ramal.entities.call import Call
from domain.status_event.entities.status_event import StatusEvent, TypeStatusRamal, TypeStatusAgent
from domain.exceptions import DomainException

class CallUseCase:

    @classmethod
    def execute(cls, status: StatusEvent) -> Call:
        if status.status_agent != TypeStatusAgent.IsLoggedIn:
            raise DomainException("")
        if status.status_ramal != TypeStatusRamal.OCUPADO:
            raise DomainException("")
        return Call()