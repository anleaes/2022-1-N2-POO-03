class Clinica:
    def __init__(self, nome, endereco, telefone):
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone

    def getNome(self):
        return self._nome