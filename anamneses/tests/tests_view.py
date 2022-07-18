import ipdb
from pacientes.models import Paciente
from rest_framework.test import APITestCase
from usuarios.models import Usuario


class TestAnamneseView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.atendete = Usuario.objects.create_superuser(
            nome="teste1", email="cb@mail.com", password="1234"
        )

        cls.paciente = Paciente.objects.create(
            nome="teste",
            cpf="12312312312",
            telefone="1231231212",
            data_nascimento="2000-01-01",
            data_cadastro="2020-10-10",
        )

    def test_create_anamnese_whitout_token(self):
        response = self.client.post(
            f"/api/anamneses/criar/{self.paciente.id}/",
            data={"paciente_id": self.paciente.id, "descricao": "teste"},
        )
        self.assertEqual(response.status_code, 401)

    def test_create_anamnese_with_token(self):
        response = self.client.post(
            path="/api/login/", data={"email": "cb@mail.com", "password": "1234"}
        )
        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

        response = self.client.post(
            f"/api/anamneses/criar/{self.paciente.id}/",
            data={"paciente_id": self.paciente.id, "descricao": "teste"},
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["descricao"], "teste")
