class Paciente():
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def getNome(self):
        return self._nome