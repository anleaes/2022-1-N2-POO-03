class CadastroPaciente:
    def __init__(self, cpf, endereco, telefone, paciente):
        self._cpf = cpf
        self._endereco = endereco
        self._telefone = telefone
        self._paciente = paciente

    def getCPF(self):
        return self._cpf
    def setCPF(self, cpf):
        self._cpf = cpf

    def getEndereco(self):
        return self._endereco
    def setEndereco(self, endereco):
        self._endereco = endereco

    def getTelefone(self):
        return self._telefone
    def setTelefone(self, telefone):
        self._telefone = telefone

    def getPaciente(self):
        return self._paciente
    def setPaciente(self, paciente):
        self._paciente = paciente

    def cadastroNaoVerificado(self):
        return print("CADASTRO NAO VERIFICADO")

    def verificaCadastro(self, paciente, cpf, endereco, telefone):
        if self.getPaciente() is not None and self.getPaciente() is paciente:
            # verifica se paciente não é nulo
            if self.getCPF() is not None and self.getCPF() > 0 and self.getCPF() is cpf:
                # verifica se cpf não é nulo e se é numero
                if self.getEndereco() is not None and self.getEndereco() is endereco:
                    # verifica se endereco não é nulo
                    if self.getTelefone() is not None and self.getTelefone() is telefone:
                        # verifica se telefone não é nulo
                        # sets
                        self.setPaciente(paciente)
                        self.setCPF(cpf)
                        self.setEndereco(endereco)
                        self.setTelefone(telefone)
                        print(f"PACIENTE: {paciente.getNome()} VERIFICADO")
                        self._cadastro = True
                    else:
                        self.cadastroNaoVerificado()
                else:
                    self.cadastroNaoVerificado()
            else:
                self.cadastroNaoVerificado()
        else:
            self.cadastroNaoVerificado()
