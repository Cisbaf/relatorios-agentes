from domain.enum.type import Type

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

