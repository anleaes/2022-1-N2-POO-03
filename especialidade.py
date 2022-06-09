class Especialidade:
    def __init__(self, nome, medico):
        self._nome = nome
        self._medico = medico

    def getNome(self):
        return self._nome