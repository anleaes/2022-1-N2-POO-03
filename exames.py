class Exames():
    def __init__(self, nome, tipoExame):
        self._nome = nome
        self._tipoExame = tipoExame

    def getNome(self):
        return self._nome
    def setNome(self, nomeExame):
        self._nome = nomeExame

    def getTipoExame(self):
        return self._tipoExame