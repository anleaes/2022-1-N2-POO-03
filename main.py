from paciente import Paciente
from medico import Medico
from especialidade import Especialidade

paciente1 = Paciente("fabio", 24, 000000000)
espec1 = Especialidade("neurologista")
medico1 = Medico("julio", 37, 11111, espec1)
