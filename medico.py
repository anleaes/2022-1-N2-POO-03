class Medico():
    def __init__(self, nome, idade, crm):
        self._nome = nome
        self._idade = idade
        self._crm = crm

    def getNome(self):
        return self._nome
    def setNome(self, nome):
        self._nome = nome

    def getIdade(self):
        return self._idade

    def getCRM(self):
        return self._crm