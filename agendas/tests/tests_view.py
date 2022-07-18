from consultas.models import Consulta
from medicos.models import Medico
from rest_framework.test import APIClient
from usuarios.models import Usuario


class AgendaTestView(APIClient):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.usuario1 = Usuario.objects.create(
            nome="teste1", email="cb@mail.com", password="1234"
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
        cls.agendaInfos = {
            "data_consulta": cls.consulta.data_da_consulta,
            "consulta_id": cls.consulta.id,
            "medico_id": cls.medico.id,
        }

    def test_create_consulta_without_token(self):
        response = self.client.post("/api/consultas/", data=self.agendaInfos)
        self.assertEqual(response.status_code, 405)

    def test_create_consulta_with_token(self):
        response = self.client.post(
            path="/api/login/", data={"email": "cb@mail.com", "password": "1234"}
        )
        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

        response_create = self.client.post("/api/agendas/", data=self.agendaInfos)
        self.assertEqual(response_create.status_code, 201)
