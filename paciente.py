class Paciente():
    def __init__(self, nome, idade, cpf):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf

    def marcarConsulta(self, Especialidade, dia, hora):
        print(f"CONSULTA MARCADA COM: {Especialidade.getNome()} / MARCADO EM: {dia} : {hora}")
        pass
