class Sala:
    def __init__(self, numeroSala, andar, clinica):
        self._numeroSala = numeroSala
        self._andar = andar
        self._clinica = clinica

    def getNumeroSala(self):
        return self._numeroSala
    def setNumeroSala(self, numeroSala):
        self._numeroSala = numeroSala

    def getAndar(self):
        return self._andar
    def setAndar(self, andar):
        self._andar = andar