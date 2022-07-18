from django.db.utils import IntegrityError, DataError
from pacientes.models import Paciente
from django.test import TestCase
from django.utils import timezone


class PacienteTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.paciente1 = Paciente.objects.create(
            nome="paciente1",
            email="paciente1@mail.com",
            cpf="12345678912",
            telefone="1894621548",
            data_nascimento="2000-02-02",
            data_cadastro=timezone.now(),
        )
        cls.paciente2 = Paciente.objects.create(
            nome="paciente2",
            email="paciente2@mail.com",
            cpf="12345678911",
            telefone="1894621548",
            data_nascimento="2000-02-02",
            data_cadastro=timezone.now(),
        )
        cls.paciente3 = Paciente.objects.create(
            nome="paciente3",
            email="paciente3@mail.com",
            cpf="58545478569",
            telefone="1894621548",
            data_nascimento="2000-02-02",
            data_cadastro=timezone.now(),
        )

    def test_paciente_fields(self):
        self.paciente1.save()
        self.paciente2.save()

    def test_paciente_duplicated_cpf(self):
        with self.assertRaises(IntegrityError):
            self.paciente1.save()
            self.paciente2.cpf = "12345678912"
            self.paciente2.save()

    def test_paciente_invalid_cpf(self):
        with self.assertRaises(DataError):
            self.paciente3.cpf = "1234567896595"
            self.paciente3.save()
