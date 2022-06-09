class Agenda:
    def __init__(self, hora, sala, exame):
        self._hora = hora
        self._sala = sala
        self._exame = exame

    def getHora(self):
        return self._hora
    def setHora(self, hora):
        self._hora = hora