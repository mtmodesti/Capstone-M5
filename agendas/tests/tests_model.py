from agendas.models import Agenda
from consultas.models import Consulta
from django.test import TestCase
from medicos.models import Medico
from usuarios.models import Usuario


class AgendaTestModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.usuario1 = Usuario.objects.create(
            nome="teste1", email="teste1@gmail.com", password="1234"
        )
        cls.usuario2 = Usuario.objects.create(
            nome="teste2", email="teste2@gmail.com", password="1234"
        )
        cls.medico = Medico.objects.create(
            usuario_id=cls.usuario2.id,
            nome="Teste1",
            especialidade="teste1",
            registro_profissional="teste1",
            telefone="teste1",
        )
        cls.consulta = Consulta.objects.create(
            usuario_id=cls.usuario1.id,
            medico_id=cls.medico.id,
            confirmado=False,
            compareceu=False,
            pago=False,
            data_da_consulta="2022-10-12 14:00",
        )
        cls.agenda = Agenda.objects.create(
            data_consulta=cls.consulta.data_da_consulta,
            consulta_id=cls.consulta.id,
            medico_id=cls.medico.id,
        )

    def test_agenda_fields_equal(self):
        self.assertEqual(self.agenda.data_consulta, self.consulta.data_da_consulta)
        self.assertEqual(self.agenda.consulta_id, self.consulta.id)
        self.assertEqual(self.agenda.consulta_id, self.consulta.id)

    def test_agenda_filds_relation(self):
        self.assertEqual(self.agenda.medico.id, self.medico.id)
        self.assertEqual(self.agenda.consulta.id, self.consulta.id)
