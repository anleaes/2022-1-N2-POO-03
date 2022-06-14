from agenda import Agenda
from sala import Sala
from exames import Exames
from medico import Medico
from clinica import Clinica
from especialidade import Especialidade
from paciente import Paciente
from cadastroPaciente import CadastroPaciente
from endereco import Endereco
from telefone import Telefone

endereco1 = Endereco("rua fulano de tal", 55, "centro", "cidade")
endereco2 = Endereco("rua ciclano de tal", 247, "barro sul", "cidade")

telefone1 = Telefone(51, 912345678)
telefone2 = Telefone(51, 987654321)

clinica1 = Clinica("feldmann", endereco1, telefone1)

sala1 = Sala(1, 1, clinica1)

exame1 = Exames("sangue", "laboratorial")

paciente1 = Paciente("fabio", 24)

cadastroP1 = CadastroPaciente(11144477700, endereco2, telefone2, paciente1)

medico1 = Medico("luiz", 553992, paciente1)

especialidade1 = Especialidade("neurologista", medico1)

agenda1 = Agenda("12:00", sala1, exame1, medico1)

print("\n")
cadastroP1.verificaCadastro(paciente1, 11144477700, endereco2, telefone2)
cadastroP1.verificaCadastro(paciente1, "11144477700", endereco2, telefone1)

print("\n")
agenda1.agendarExame(exame1, medico1, "12:00", sala1)
agenda1.agendarExame(exame1, medico1, "11:00", sala1) #supostamente errado