class Telefone:
    def __init__(self, ddd, numero):
        self._ddd = ddd
        self._numero = numero

    def getDDD(self):
        return self._ddd
    def setDDD(self, ddd):
        self._ddd = ddd

    def getNumero(self):
        return self._numero
    def setNumero(self, numero):
        self._numero = numero