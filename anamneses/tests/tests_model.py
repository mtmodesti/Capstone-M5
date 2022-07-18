from anamneses.models import Anamnese
from django.test import TestCase
from pacientes.models import Paciente


class TestAnamneseModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.paciente = Paciente.objects.create(
            nome="teste",
            cpf="12312312312",
            telefone="1231231212",
            data_nascimento="2000-01-01",
            data_cadastro="2020-10-10"
        )
        cls.anamnese = Anamnese.objects.create(
            paciente_id=cls.paciente.id, descricao="teste"
        )

    def test_anamnese_filds(self):
        self.assertEqual(self.anamnese.descricao, "teste")
        self.assertEqual(self.anamnese.paciente_id, self.paciente.id)

    def test_anamnese_relation(self):
        self.assertEqual(self.anamnese.paciente, self.paciente)
