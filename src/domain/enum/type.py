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
    