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

    def getNumero(self):
        return self._numero
    def setNumero(self, numero):
        self._numero = numero

    def getBairro(self):
        return self._bairro
    def setBairro(self, bairro):
        self._bairro = bairro

    def getCidade(self):
        return self._cidade
    def setCidade(self, cidade):
        self._cidade = cidade