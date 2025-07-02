from enum import Enum


class TypeStatusRamal(Enum):
    LIVRE = 0
    OCUPADO = 1
    OUT_OF_SERVICE = 4
    RINGING = 8

    @classmethod
    def get(cls, status: int, default=None):
        """Retorna o membro da enumeração correspondente ao valor inteiro."""
        for member in cls:
            if member.value == status:
                return member
        return default