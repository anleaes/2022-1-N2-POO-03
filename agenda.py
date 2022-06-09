class Agenda:
    def __init__(self, hora, sala, exame, especialidade):
        self._hora = hora
        self._sala = sala
        self._exame = exame
        self._especialidade = especialidade

    def getHora(self):
        return self._hora
    def setHora(self, hora):
        self._hora = hora

    def getSala(self):
        return self._sala
    def setSala(self, sala):
        self._sala = sala

    def getExame(self):
        return self._exame
    def setExame(self, exame):
        self._exame = exame

    def verificarHorario(self, hora, sala):
        pass

    def agendarExame(self, exame, especialidade):
        pass