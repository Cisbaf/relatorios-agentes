from enum import Enum


class Type(Enum):

    def __init__(self, value):
        super().__init__()
        self.translations = {}

    def translate(self):
        return self.translations.get(self.name, self.name)

    @classmethod
    def get(cls, status: int, default=None):
        """Retorna o membro da enumeração correspondente ao valor inteiro."""
        for member in cls:
            if member.value == status:
                return member
        return default
    

class TypeStatusAgent(Type):
    def __init__(self, value):
        super().__init__(value)
        self.translations = {
            'IsLoggedOut': 'Deslogado',
            'IsLoggedIn': 'Logado',
            'IsOnBreak': 'Em Pausa',
            'IsRemoved': 'Removido'
        }

    IsLoggedOut = 0
    IsLoggedIn = 1
    IsUnavailable = 4
    IsOnBreak = 5
    IsRemoved = 6


class TypeStatusRamal(Type):
    LIVRE = 0
    OCUPADO = 1
    OUT_OF_SERVICE = 4
    RINGING = 8


class TypePause(Type):
    def __init__(self, value):
        super().__init__(value)
        self.translations = {
            'LUNCH': 'ALMOÇO',
            'BATHROOM_BREAK': 'BANHEIRO'
        }
    
    """
    ALMOCO → LUNCH
    CAFÉ DA MANHÃ → BREAKFAST
    CAFÉ DA TARDE → AFTERNOON_COFFEE
    BANHEIRO → BATHROOM_BREAK
    JANTAR → DINNER
    DESCANSO NOTURNO → NIGHT_REST
    CONFERÊNCIA → CONFERENCE
    """    
    LUNCH = 1
    BREAKFAST = 2
    AFTERNOON_COFFEE = 3
    BATHROOM_BREAK = 5
    DINNER = 7
    NIGHT_REST = 8
    CONFERENCE = 9
