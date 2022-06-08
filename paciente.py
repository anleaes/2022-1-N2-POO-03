class Paciente():
    def __init__(self, nome, idade, cpf):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf

    def marcarConsulta(self, Especialidade, dia, hora):
        if dia < 30 and dia > 0:
            print(f"CONSULTA MARCADA COM: {Especialidade.getNome()} / MARCADO dia {dia}, hora {hora}")
            pass # fim if
        pass # fim marcarConsulta
