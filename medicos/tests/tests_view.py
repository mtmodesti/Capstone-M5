from rest_framework.test import APITestCase
from usuarios.models import Usuario
from medicos.models import Medico


class TestMedicoView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        user_data ={
            "nome":"Médico doutor estranho",
            "password":"1234",
            "email":"medico_joao2@mail.com",
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
        cls.medico = Medico.objects.create(**medico_data, usuario=cls.usuario)
        cls.login_data_medico = {
            "password":"1234",
            "email":"medico_joao2@mail.com",
        }


        cls.atendente = Usuario.objects.criar_usuario(**{
            "nome":"Atendente",
            "password":"1234",
            "email":"atendente_cris4@mail.com"
        })
        
        cls.login_data_atendente = {
            "password":"1234",
            "email":"atendente_cris4@mail.com"
        }
        cls.request_data_success = {
            "nome":"Médico doutor estranho",
            "password":"1234",
            "email":"medico_joao@mail.com",
            "especialidade":"Ortopedia",
            "telefone":"24998913388",
            "registro_profissional": "12345677"
        }
        cls.request_data_missing_keys = {}


    def test_create_without_token(self):
        response = self.client.post('/api/usuario/medico/criar/',self.request_data_success)
        self.assertEqual(response.status_code, 401)

    def test_create_without_permission(self):
        login = self.client.post('/api/login/', self.login_data_medico)
        token = login.data['access']
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)
        response = self.client.post('/api/usuario/medico/criar/',self.request_data_success)
        self.assertEqual(response.status_code, 403)
    
    def test_create_missing_keys(self):
        login = self.client.post('/api/login/', self.login_data_atendente)
        token = login.data['access']
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)
        response = self.client.post('/api/usuario/medico/criar/',self.request_data_missing_keys)
        self.assertEqual(response.status_code, 400)

    def test_create_medico(self):
        login = self.client.post('/api/login/', self.login_data_atendente)
        token = login.data['access']
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)
        response = self.client.post('/api/usuario/medico/criar/',self.request_data_success)
        self.assertEqual(response.status_code, 201)

    def test_list_medico(self):
        login = self.client.post('/api/login/', self.login_data_atendente)
        token = login.data['access']
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)
        response = self.client.get('/api/usuario/medico/listar/',self.request_data_success)
        self.assertEqual(response.status_code, 200)
        
