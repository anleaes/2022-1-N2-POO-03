class Clinica:
    def __init__(self, nome, endereco, telefone):
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone

    def getNome(self):
        return self._nome
    def setNome(self, nomeClinica):
        self._nome = nomeClinica

    def getEndereco(self):
        return self._endereco
    def setEndereco(self, endereco):
        self._endereco = endereco

    def getTelefone(self):
        return self._telefone