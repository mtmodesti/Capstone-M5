import json
from rest_framework.test import APITestCase
import ipdb

from usuarios.models import Usuario


class TestUsuarioView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.usuario1 = {
            "nome": "test",
            "email": "test1@mail.com",
            "password": "1234",
        }
        cls.admin = Usuario.objects.create_superuser(
            email="leo@admin.com", password="1234", nome="Admin"
        )

    def test_create_usuario_without_token(self):
        response = self.client.post("/api/usuarios/", data=self.usuario1)
        self.assertEqual(response.status_code, 401)

    def test_authentication_token_generation(self):
        response = self.client.post(
            "/api/login/",
            data={"email": "leo@admin.com", "password": "1234"},
        )
        self.assertEqual(response.status_code, 200)

        # response_content = json.loads(response.content.decode("utf-8"))
        # token = response_content["access"]

        # self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

        # response = self.client.post(
        #     "/api/usuarios/",
        #     data=self.usuario1,
        # )
        # self.assertEqual(response.status_code, 201)
