import json
from rest_framework.test import APITestCase
import ipdb
from django.utils import timezone

from usuarios.models import Usuario


class PacienteTestView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # setup admin user
        cls.admin = Usuario.objects.create_superuser(
            email="leo@admin.com", password="1234", nome="Admin"
        )
        # paciente info
        cls.paciente = {
            "nome": "paciente1",
            "email": "paciente1@mail.com",
            "cpf": "12345678912",
            "telefone": "1894621548",
            "data_nascimento": "2000-02-02",
        }

    def test_create_paciente_without_token(self):
        response = self.client.post("/api/pacientes/", data=self.paciente)
        self.assertEqual(response.status_code, 401)

    def test_create_paciente_with_token(self):
        # setup token
        response = self.client.post(
            "/api/login/",
            data={"email": "leo@admin.com", "password": "1234"},
        )
        response_content = json.loads(response.content.decode("utf-8"))
        token = response_content["access"]

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

        response_create = self.client.post("/api/pacientes/", data=self.paciente)
        self.assertEqual(response_create.status_code, 201)
