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

    def getEspecialidade(self):
        return self._especialidade
    def setEspecialidade(self, especialidade):
        self._especialidade = especialidade

    def horarioNaoVerificado(self):
        return print("CADASTRO NAO VERIFICADO")

    def verificarHorario(self, hora, sala):
        if self.getHora() is not None and self.getHora() is hora:
            if self.getSala() is not None and self.getSala() is sala:
                return True
            else:
                return False
                self.horarioNaoVerificado()
        else:
            return False
            self.horarioNaoVerificado()

    def agendarExame(self, exame, especialidade, hora, sala):
        if self.verificarHorario(hora, sala) is True:
            # marcar exame
            pass
        else:
            #nao marcar exame
            pass