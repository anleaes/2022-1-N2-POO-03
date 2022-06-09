class Medico():
    def __init__(self, nome, crm, paciente):
        self._nome = nome
        self._crm = crm
        self._paciente = paciente

    def getNome(self):
        return self._nome
    def setNome(self, nome):
        self._nome = nome

    def getCRM(self):
        return self._crm
    def setCRM(self, crm):
        self._crm = crm

    def getPaciente(self):
        return self._paciente
    def setPaciente(self, paciente):
        self._paciente = paciente