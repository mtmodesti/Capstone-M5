from django.db.utils import IntegrityError
from medicos.models import Medico
from usuarios.models import Usuario
from django.test import TestCase


class TestMedicoModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        user_data ={
            "nome":"Médico doutor estranho",
            "password":"1234",
            "email":"medico_joao@mail.com",
            "especialidade":"Ortopedia",
            "telefone":"24998913388",
            "registro_profissional": "12345675"
        }
        medico_data = {
            "nome": user_data['nome'],
            "email": user_data['email'],
            "especialidade": user_data.pop("especialidade"),
            "registro_profissional": user_data.pop("registro_profissional"),
            "telefone": user_data.pop("telefone"),
        }
        cls.usuario = Usuario.objects.criar_agente_de_saude(**user_data)
        cls.medico1 = Medico.objects.create(**medico_data, usuario=cls.usuario)

    def test_medico_fields(self):
        self.assertEqual(self.medico1.nome, self.usuario.nome)
        self.assertEqual(self.medico1.email, self.usuario.email)
        self.assertEqual(self.medico1.usuario_id, self.usuario.id)
        self.assertEqual(self.medico1.especialidade, 'Ortopedia')
        self.assertEqual(self.medico1.telefone, '24998913388')
        self.assertEqual(self.medico1.registro_profissional, '12345675')

    def test_medico_with_same_registro_profissional(self):
        user_data2 ={
            "nome":"Médico doutor estranho 2",
            "password":"1234",
            "email":"medico_joao2@mail.com",
            "especialidade":"Ortopedia",
            "telefone":"24998913388",
            "registro_profissional": "12345675"
        }
        medico_data2 = {
            "nome": user_data2['nome'],
            "email": user_data2['email'],
            "especialidade": user_data2.pop("especialidade"),
            "registro_profissional": user_data2.pop("registro_profissional"),
            "telefone": user_data2.pop("telefone"),
        }
        with self.assertRaises(IntegrityError):
            self.usuario2 = Usuario.objects.criar_agente_de_saude(**user_data2)
            self.medico2 = Medico.objects.create(**medico_data2, usuario=self.usuario)