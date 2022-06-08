class Medico():
    def __init__(self, nome, idade, crm, especialidade):
        self._nome = nome
        self._idade = idade
        self._crm = crm
        self._especialidade = especialidade

    def getNome(self):
        return self._nome

    def getIdade(self):
        return self._idade

    def getCRM(self):
        return self._crm