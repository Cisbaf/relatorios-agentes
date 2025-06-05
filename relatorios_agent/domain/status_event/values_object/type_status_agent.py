from enum import Enum


class TypeStatusAgent(Enum):
    IsLoggedOut = 0
    IsLoggedIn = 1
    IsUnavailable = 4
    IsOnBreak = 5
    IsRemoved = 6
    
    @classmethod
    def get(cls, status: int, default=None):
        """Retorna o membro da enumeração correspondente ao valor inteiro."""
        for member in cls:
            if member.value == status:
                return member
        return default