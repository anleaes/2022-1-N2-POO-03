class Endereco:
    def __init__(self, nomeRua, numero, bairro, cidade):
        self._nomeRua = nomeRua
        self._numero = numero
        self._bairro = bairro
        self._cidade = cidade

    def getNomeRua(self):
        return self._nomeRua
    def setNomeRua(self, nomeRua):
        self._nomeRua = nomeRua