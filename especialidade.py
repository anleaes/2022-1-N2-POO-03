class Especialidade:
    def __init__(self, nome, medico):
        self._nome = nome
        self._medico = medico

    def getNome(self):
        return self._nome
    def setNome(self, nome):
        self._nome = nome

    def getMedico(self):
        return self._medico
    def setMedico(self, medico):
        self._medico = medico