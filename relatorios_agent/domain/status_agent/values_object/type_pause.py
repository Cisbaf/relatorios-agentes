from enum import Enum


class TypePause(Enum):
    LUNCH = 1
    BREAKFAST = 2
    AFTERNOON_COFFEE = 3
    BATHROOM_BREAK = 5
    DINNER = 7
    NIGHT_REST = 8
    CONFERENCE = 9
    
    @classmethod
    def get(cls, status: int, default=None):
        """Retorna o membro da enumeração correspondente ao valor inteiro."""
        for member in cls:
            if member.value == status:
                return member
        return default