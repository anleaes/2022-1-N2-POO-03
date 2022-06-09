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