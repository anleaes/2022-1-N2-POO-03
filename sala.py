class Sala:
    def __init__(self, numeroSala, andar, clinica):
        self._numeroSala = numeroSala
        self._andar = andar
        self._clinica = clinica

    def getNumeroSala(self):
        return self._numeroSala