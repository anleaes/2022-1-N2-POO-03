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
        return print("HORARIO NAO VERIFICADO")

    def exameNaoMarcado(self):
        return print("EXAME NAO MARCADO")

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
            if self.getExame() is not None and self.getExame() is exame:
                if self.getEspecialidade() is not None and self.getEspecialidade() is especialidade:
                    print(f"EXAME {self.getExame()} MARCADO AS: {self.getHora()} NA SALA: {self.getSala()}")
                else:
                    self.exameNaoMarcado()
            else:
                self.exameNaoMarcado()
        else:
            self.exameNaoMarcado()
            pass