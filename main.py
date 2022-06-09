from agenda import Agenda
from sala import Sala
from exames import Exames
from medico import Medico
from clinica import Clinica
from especialidade import Especialidade
from paciente import Paciente
from cadastroPaciente import CadastroPaciente

clinica1 = Clinica("feldmann", "rua fulano de tal", 51995563241)
sala1 = Sala(1, 1, clinica1)
exame1 = Exames("sangue", "laboritorial")
paciente1 = Paciente("fabio", 24)
cadastroP1 = CadastroPaciente(11144477700, "rua ciclano de tal", 123456789, paciente1)
medico1 = Medico("luiz", 553992, paciente1)

agenda1 = Agenda("12:00", sala1, exame1, medico1)