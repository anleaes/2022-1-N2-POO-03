class Agenda:
    def __init__(self, hora, sala, exame, medico):
        self._hora = hora
        self._sala = sala
        self._exame = exame
        self._medico = medico

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

    def getMedico(self):
        return self._especialidade
    def setMedico(self, medico):
        self._medico = medico

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

    def agendarExame(self, exame, medico, hora, sala):
        if self.verificarHorario(hora, sala) is True:
            if self.getExame() is not None and self.getExame() is exame:
                if self.getMedico() is not None and self.getMedico() is medico:
                    print(f"EXAME {self.getExame()} MARCADO AS: {self.getHora()} NA SALA: {self.getSala()}")
                else:
                    self.exameNaoMarcado()
            else:
                self.exameNaoMarcado()
        else:
            self.exameNaoMarcado()