from domain.enum.type import Type


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
